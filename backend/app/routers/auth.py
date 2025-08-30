from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..schemas import LoginRequest, Token, UserCreate, UserOut
from ..security import verify_password, create_access_token, hash_password


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
	user = db.query(User).filter(User.username == payload.username).first()
	if not user or not verify_password(payload.password, user.password_hash):
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
	token = create_access_token(subject=user.username)
	return Token(access_token=token)


@router.post("/register", response_model=UserOut)
def register(payload: UserCreate, db: Session = Depends(get_db)):
	exists = db.query(User).filter(User.username == payload.username).first()
	if exists:
		raise HTTPException(status_code=400, detail="Username already exists")
	user = User(
		username=payload.username,
		full_name=payload.full_name,
		password_hash=hash_password(payload.password),
		is_admin=payload.is_admin,
		branch_id=payload.branch_id,
	)
	db.add(user)
	db.commit()
	db.refresh(user)
	return user

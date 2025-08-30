from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Branch
from ..schemas import BranchCreate, BranchOut
from ..deps import require_admin


router = APIRouter(prefix="/branches", tags=["branches"]) 


@router.get("/", response_model=list[BranchOut])
def list_branches(db: Session = Depends(get_db)):
	return db.query(Branch).order_by(Branch.id).all()


@router.post("/", response_model=BranchOut, dependencies=[Depends(require_admin)])
def create_branch(payload: BranchCreate, db: Session = Depends(get_db)):
	exists = db.query(Branch).filter(Branch.name == payload.name).first()
	if exists:
		raise HTTPException(status_code=400, detail="Branch already exists")
	branch = Branch(name=payload.name)
	db.add(branch)
	db.commit()
	db.refresh(branch)
	return branch


@router.delete("/{branch_id}", dependencies=[Depends(require_admin)])
def delete_branch(branch_id: int, db: Session = Depends(get_db)):
	branch = db.get(Branch, branch_id)
	if not branch:
		raise HTTPException(status_code=404, detail="Branch not found")
	db.delete(branch)
	db.commit()
	return {"ok": True}

from pydantic import BaseModel, Field
from typing import Optional


class BranchCreate(BaseModel):
	name: str = Field(min_length=2, max_length=100)


class BranchOut(BaseModel):
	id: int
	name: str
	is_active: bool

	class Config:
		from_attributes = True


class UserCreate(BaseModel):
	username: str = Field(min_length=3, max_length=64)
	full_name: Optional[str] = None
	password: str = Field(min_length=6, max_length=128)
	is_admin: bool = False
	branch_id: Optional[int] = None


class UserOut(BaseModel):
	id: int
	username: str
	full_name: Optional[str] = None
	is_admin: bool
	branch_id: Optional[int] = None

	class Config:
		from_attributes = True


class Token(BaseModel):
	access_token: str
	token_type: str = "bearer"


class LoginRequest(BaseModel):
	username: str
	password: str

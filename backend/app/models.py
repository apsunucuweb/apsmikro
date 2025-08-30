from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base


class Branch(Base):
	__tablename__ = "branches"

	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
	is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

	users: Mapped[list["User"]] = relationship("User", back_populates="branch")


class User(Base):
	__tablename__ = "users"

	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
	full_name: Mapped[str | None] = mapped_column(String(120))
	password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
	is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
	branch_id: Mapped[int | None] = mapped_column(ForeignKey("branches.id"), nullable=True)

	branch: Mapped[Branch | None] = relationship("Branch", back_populates="users")

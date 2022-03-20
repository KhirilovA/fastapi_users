from typing import List

from fastapi import (
	Depends,
	HTTPException,
	status,
	Response
	)
from sqlalchemy.orm import Session

from ..schemas.users import (
	UserCreate,
	PasswordUpdate
	)
from ..models.users import User
from ..db.session import get_session


class UserServices():
	def __init__(self, session: Session = Depends(get_session)):
		self.session = session

	def get_list(self) -> List[User]:
		users = (
			self.session
			.query(User).
			all()
		)
		return users

	def get(self, user_id: int) -> User:
		user = (
			self.session
			.query(User)
			.filter_by(id=user_id)
			.first()
		)
		if not user:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
		return user

	def create(self, user_data: UserCreate) -> User:
		user = User(**user_data.dict())
		self.session.add(user)
		self.session.commit()
		return user

	def update_password(self, user_id: int, password_data: PasswordUpdate):
		user = self.get(user_id)
		password_data = password_data.dict()

		# Checking if new password isn't the same as old password
		if password_data['old_password'] == password_data['new_password']:
			raise HTTPException(
				status_code=status.HTTP_404_NOT_FOUND,
				detail={'detail': 'Your password should differ from the old one'}
			)

		# Checking if user confirms his password 
		if password_data['new_password'] != password_data['confirm_password']:
			raise HTTPException(
				status_code=status.HTTP_404_NOT_FOUND,
				detail={'detail': 'passwords does not match'}
			)

		# Checking if user knows his old password
		if password_data['old_password'] != user.password:
			raise HTTPException(
				status_code=status.HTTP_404_NOT_FOUND,
				detail={'detail': 'past the right old password'}
			)

		setattr(user, 'password', password_data['new_password'])
		self.session.commit()
		return user

	def delete_user(self, user_id: int):
		user = self.get(user_id)
		self.session.delete(user)
		self.session.commit()
		return Response(status_code=status.HTTP_204_NO_CONTENT)

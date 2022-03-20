from typing import List

from fastapi import (
	APIRouter,
	Body,
	Depends,
	Response
	)
from sqlalchemy.orm import Session

from ..schemas.users import (
	UserCreate,
	User,
	PasswordUpdate
	)
from ..services.users import UserServices


router = APIRouter()

@router.post('/create-user', response_model=User)
def user_create(
	user_data: UserCreate,
	service: UserServices = Depends()
):
	return service.create(user_data)


@router.get('/get-user-list', response_model=List[User])
def user_list(
	service: UserServices = Depends()
):
	return service.get_list()


@router.get('/search/{user_id}', response_model=User)
def user_search(
	user_id: int,
	service: UserServices = Depends()
):
	return service.get(user_id)


@router.put('/update-password/{user_id}', response_model=UserCreate)
def user_update_password(
	user_id: int,
	password_data: PasswordUpdate,
	service: UserServices = Depends()
):
	return service.update_password(
		user_id,
		password_data
	)


@router.delete('/delete-user/{user_id}')
def user_delete(
	user_id: int,
	service: UserServices = Depends()
):
	return service.delete_user(user_id)

	
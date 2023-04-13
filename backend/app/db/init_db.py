import logging

from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core.config import Settings
from app.schemas.user import UserCreateModel


from app.crud.user import create_init_user


settings = Settings()
logger = logging.getLogger('recipebox')


def init_db(db: Session):
    create_user(db)


def create_user(db: Session):
    user = settings.INIT_USER
    try:
        db_user = UserCreateModel(
            username=user['username'],
            email=user['email'],
            password=user['password'],
            is_active=user['is_active'],
            role_id=user['role_id']
        )
    except ValidationError as e:
        logger.error(f"An error occur while creating model {e}")
    else:
        create_init_user(db, db_user)
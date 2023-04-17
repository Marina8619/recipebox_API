from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.mixin import Timestamp

from .user import User
from .ingredient import Ingredient


class Recipe(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(120), nullable=False)
    difficulty = Column(Integer)
    instructions = Column(String(120), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    ingredients = relationship("RecipeIngredient", back_populates='recipe')
    user = relationship("User", back_populates='receipt')
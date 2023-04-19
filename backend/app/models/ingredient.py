from sqlalchemy import Column, Integer, Float, ForeignKey, Text, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.mixin import Timestamp
from app.models.recipe_ingredient import RecipeIngredient

class Ingredient(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(30), unique=True, index=True)
    units = Column(String(10), nullable=True)

    recipes = relationship("RecipeIngredient", back_populates="ingredient")
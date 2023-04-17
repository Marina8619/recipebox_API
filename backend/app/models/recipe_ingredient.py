from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app.db.base_class import Base
from app.models.mixin import Timestamp
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from .recipe import Recipe
from .ingredient import Ingredient


class RecipeIngredient(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredient.id"))
    quantity = Column(Float, nullable=False, default=1)
    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipes")




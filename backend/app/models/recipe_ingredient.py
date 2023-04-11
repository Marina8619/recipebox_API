from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base_class import Base
from app.models.mixin import Timestamp
from sqlalchemy.orm import relationship
#from app.models.recipe import Recipe


class RecipeIngredient(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredient.id"))
    quantity = Column(String(50), nullable=False)

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipes")


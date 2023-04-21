from sqlalchemy import Column, Integer, ForeignKey
from app.db.base_class import Base
from app.models.mixin import Timestamp
from sqlalchemy.orm import relationship

from sqlalchemy.ext.associationproxy import association_proxy


class RecipeIngredient(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredient.id"))
    quantity = Column(Integer, nullable=False, default=1)

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipes")

    ingredient_name = association_proxy(target_collection='ingredient', attr='name')
    ingredient_units = association_proxy(target_collection='ingredient', attr='units')



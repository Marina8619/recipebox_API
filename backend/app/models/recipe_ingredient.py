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

    # ingredient_name = association_proxy(target_collection='ingredient', attr='name')
    # units = association_proxy(target_collection='ingredient', attr='units')
    # recipe_ingredient = association_proxy(target_collection='ingredient', attr='recipes')


# from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
# from app.db.base_class import Base
# from sqlalchemy.ext.associationproxy import association_proxy
#
# from .order import Order
# from .book import Book
#
#
# class OrderBook(Base):
#     id = Column(Integer, primary_key=True, nullable=False)
#     amount = Column(Integer, nullable=False, default=1)
#     order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
#     book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
#
#     order = relationship("Order", back_populates="books")
#     book = relationship("Book", back_populates="order")
#
#     book_title = association_proxy(target_collection='book', attr='title')
#     book_description = association_proxy(target_collection='book', attr='description')
#     book_price = association_proxy(target_collection='book', attr='price')
#     book_author_id = association_proxy(target_collection='book', attr='author_id')
#     book_author = association_proxy(target_collection='book', attr='author')
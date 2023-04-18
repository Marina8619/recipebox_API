from fastapi import APIRouter

from .endpoints import recipe, ingredient, recipe_ingredient


api_router = APIRouter()

api_router.include_router(
    recipe.recipe_router
)

api_router.include_router(
    ingredient.ingredient_router, prefix='/ingredients'
)

api_router.include_router(
    recipe_ingredient.rec_ing_router
)

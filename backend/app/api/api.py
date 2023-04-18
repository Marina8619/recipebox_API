from fastapi import APIRouter

from .endpoints import recipe, ingredient


api_router = APIRouter()

api_router.include_router(
    recipe.recipe_router
)

api_router.include_router(
    ingredient.ingredient_router
)

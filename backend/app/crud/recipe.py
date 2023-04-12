import logging
from typing import List

from sqlalchemy.orm import Session
from app.models.recipe import Recipe
from app.models.recipe_ingredient import RecipeIngredient


logger = logging.getLogger("recipebox")


def create_init_recipe(db: Session, recipe: Recipe) -> Recipe:
    db_recipe = Recipe(
        name=recipe.name,
        description=recipe.description,
        difficulty=recipe.difficulty,
        instructions=recipe.instructions,
        user_id=recipe.user_id
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    logger.info(f'Created book {db_recipe}')
    return db_recipe


def get_recipe_by_id(db: Session, recipe_id: int) -> Recipe:
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()


def get_recipe_list(db: Session) -> List[Recipe]:
    return db.query(Recipe).all()
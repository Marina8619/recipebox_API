import logging
from typing import List

from sqlalchemy.orm import Session, joinedload
from app.models.recipe import Recipe


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


def create_add_recipe(db: Session, recipe: Recipe) -> Recipe:
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

    logger.info(f'New entry in the recipe book {db_recipe}')
    return db_recipe


def get_recipe_by_id(db: Session, id_: int):
    return db.query(Recipe).options(joinedload(Recipe.ingredients)).where(Recipe.id == id_).first()


def get_recipe_list(db: Session) -> List[Recipe]:
    return db.query(Recipe).all()


def get_recipe_by_name(db: Session, name_: str):
    return db.query(Recipe).options(joinedload(Recipe.ingredients)).where(Recipe.name == name_).first()



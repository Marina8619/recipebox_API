import logging.config

from fastapi import FastAPI

from app.core.config import Settings
from app.core.config import LOGGING_CONFIG
from app.api.api import api_router


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("recipebox")


def start_application(config: Settings):
    application = FastAPI(
        debug=True,
        title=config.PROJECT_NAME,
        version=config.PROJECT_VERSION,
        description="Recipebox store emulator"
    )
    return application


settings = Settings()

app = start_application(settings)
app.include_router(api_router)


# @app.get("/")
# async def root():
#     logger.debug("Start application")
#     return {"message": "Hello FastAPI"}

# def start_application(config: Settings):
#     application = FastAPI(
#         debug=True,
#         title=config.PROJECT_NAME,
#         version=config.PROJECT_VERSION,
#         description="Recipebox store emulator",
#     )
#     return application
#
#
# settings = Settings()
# app = start_application(settings)
# app.include_router(api_router)

# import logging.config
#
# from fastapi import FastAPI
# from app.core.config import Settings
# from app.core.config import LOGGING_CONFIG
# from app.api.api import api_router
#
#
# logging.config.dictConfig(LOGGING_CONFIG)
# logger = logging.getLogger("recipebox")
#
#
# def start_application(config: Settings):
#     application = FastAPI(
#         debug=True,
#         title=config.PROJECT_NAME,
#         version=config.PROJECT_VERSION,
#         description="Book store emulator"
#     )
#     return application
#
#
# settings = Settings()
#
# app = start_application(settings)
# app.include_router(api_router)
#
#
# @app.get("/")
# async def root():
#     logger.debug("Start application")
#     return {"message": "Hello FastAPI"}

# import logging.config
#
# from fastapi import FastAPI
# from app.core.config import Settings
# from app.core.config import LOGGING_CONFIG
# from app.api.api import api_router
#
#
# logging.config.dictConfig(LOGGING_CONFIG)
# logger = logging.getLogger("recipebox")
#
#
# def start_application(config: Settings):
#     application = FastAPI(
#         debug=True,
#         title=config.PROJECT_NAME,
#         version=config.PROJECT_VERSION,
#         description="Book store emulator"
#     )
#     return application
#
#
# settings = Settings()
#
# app = start_application(settings)
# app.include_router(api_router)
#
#
# @app.get("/")
# async def root():
#     logger.debug("Start application")
#     return {"message": "Hello FastAPI"}
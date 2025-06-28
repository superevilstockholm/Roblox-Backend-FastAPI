from fastapi import FastAPI

from api import ping, test, playerjoin

class Router:
    def __init__(self, app: FastAPI):
        self.app: FastAPI = app

        self.__register_router__()

    def __register_router__(self):
        self.app.include_router(ping.router)
        self.app.include_router(test.router)
        self.app.include_router(playerjoin.router)
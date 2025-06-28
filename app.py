from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

import os
from dotenv import load_dotenv

from aiomysql import create_pool

from router import Router

class Core():
    def __init__(self):
        load_dotenv()
        self.app: FastAPI = FastAPI()

        # Middlewares
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.app.add_middleware(GZipMiddleware, minimum_size=1000)

        # Events
        self.app.add_event_handler("startup", self.startup_event)
        self.app.add_event_handler("shutdown", self.shutdown_event)

    async def startup_event(self):
        self.app.state.db_pool = await create_pool(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            db=os.getenv('DB_NAME'),
            autocommit=True
        )
        Router(app=self.app)

    async def shutdown_event(self):
        if self.db_pool:
            self.db_pool.close()
            await self.db_pool.wait_closed()

app = Core().app
# python -m uvicorn app:app --reload --port=23237
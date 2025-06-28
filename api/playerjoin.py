from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

import aiohttp

from models.ResponseModel import BaseResponse

from typing import Union

router = APIRouter(prefix='/api', tags=["player-join"])

async def register_user(user_id: Union[str, int]):
    pass

@router.post("/player-join/{username}", response_class=JSONResponse, response_model=BaseResponse, response_model_exclude_unset=True)
async def ping(request: Request, username: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(url="https://users.roblox.com/v1/usernames/users", json={"usernames": [username], "exclude_banned_users": False}) as response:
            if response.status == 200:
                print(await response.json())
                return {"status": True, "message": "Success"}
            else:
                return {"status": False, "message": f"Failed to fetch users: {response.status}"}
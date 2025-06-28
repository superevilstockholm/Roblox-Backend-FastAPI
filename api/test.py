from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from asyncio import sleep
from time import perf_counter

from models.ResponseModel import BaseResponse

router = APIRouter(prefix='/api/test', tags=["testing"])

@router.get("/async/{delay}", response_class=JSONResponse, response_model=BaseResponse, response_model_exclude_unset=True)
async def test_async_io_request(request: Request, delay: int | str):
    """Test long async io task to see if it works"""
    start = perf_counter()
    await sleep(int(delay))
    end = perf_counter() - start
    return {
        "status": True,
        "message": f"Success. Server time needed: {end}s",
        "data": {
            "delay": delay,
            "server_time": end,
            "host": request.client.host
        }
    }
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from models.ResponseModel import BaseResponse

router = APIRouter(prefix='/api', tags=["other"])

@router.get("/ping", response_class=JSONResponse, response_model=BaseResponse, response_model_exclude_unset=True)
async def ping(request: Request):
    return {
        "status": True,
        "message": "Pong"
    }
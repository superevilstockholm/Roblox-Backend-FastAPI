from pydantic import BaseModel
from typing import Optional, Union, Any

class BaseResponse(BaseModel):
    status: bool
    message: Optional[Union[str, int]] = None
    data: Optional[dict[str, Any]] = None
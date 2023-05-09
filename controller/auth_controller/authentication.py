from datetime import datetime,timedelta
from typing import Optional
from pydantic import BaseModel
from template import logging

from fastapi import APIRouter,HTTPException,Request,Response,status
from jose import JWTError,jwt
from starlette.responses import RedirectResponse,JSONResponse
from face_auth import logging


router =APIRouter(
    prefix="/auth",
    tags=['auth'],
    responses={"401":{'description':'Not Authorized!!!'}}
)


class Login(BaseModel):
    "base model for login"
    email_id :str
    password : str


@router.get('/auth',response_class=JSONResponse)
async def authentication_page(request:Request):
    try:
        response = JSONResponse(status_code=status.HTTP_200_OK,
                                content={'message':'Authentication Page!!!'})
        
        return response
    except Exception as e:
        logging.exception(e)


@router.post('/',response_class=JSONResponse)
async def login(request: Request,login:Login):
    try:

        pass
    except Exception as e:
        logging.exception(e)

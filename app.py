import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette import status
# from starlette.middleware.sessions import SessionMiddleware
from controller.auth_controller import authentication
from face_auth import logging


app = FastAPI()



@app.get('/')
def read_root():
    return RedirectResponse(url='/auth',status_code=status.HTTP_302_FOUND)

app.include_router(authentication.router)


if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=800)
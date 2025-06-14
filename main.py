from fastapi import FastAPI
#from chainlit.utils import mount_chainlit



import functools
import importlib
import inspect
import os
from asyncio import CancelledError
from typing import Callable

# import click
# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# from packaging import version
# from starlette.middleware.base import BaseHTTPMiddleware

from chainlit.auth import ensure_jwt_secret
# from chainlit.context import context
# from chainlit.logger import logger
# from chainlit.message import ErrorMessage



app2 = FastAPI(root_path="/")
              
@app2.get("/app")
def read_main():
    return {"message": "Hello World from main app"}

#mount_chainlit(app=app2, target="my_cl_app.py", path="/chainlit")
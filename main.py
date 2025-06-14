from fastapi import FastAPI
#from chainlit.utils import mount_chainlit



import functools
import importlib
import inspect
import os
from asyncio import CancelledError
from typing import Callable

import click
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from packaging import version
from starlette.middleware.base import BaseHTTPMiddleware

from chainlit.auth import ensure_jwt_secret
from chainlit.context import context
from chainlit.logger import logger
from chainlit.message import ErrorMessage

def mount_chainlit(app: FastAPI, target: str, path="/chainlit"):
    from chainlit.config import config, load_module
    from chainlit.server import app as chainlit_app

    config.run.debug = os.environ.get("CHAINLIT_DEBUG", False)
    os.environ["CHAINLIT_ROOT_PATH"] = path

    api_full_path = path

    if app.root_path:
        parent_root_path = app.root_path.rstrip("/")
        api_full_path = parent_root_path + path
        os.environ["CHAINLIT_PARENT_ROOT_PATH"] = parent_root_path

    #check_file(target)
    # Load the module provided by the user
    config.run.module_name = target
    load_module(config.run.module_name)

    ensure_jwt_secret()

    class ChainlitMiddleware(BaseHTTPMiddleware):
        """Middleware to handle path routing for submounted Chainlit applications.

        When Chainlit is submounted within a larger FastAPI application, its default route
        `@router.get("/{full_path:path}")` can conflict with the main app's routing. This
        middleware ensures requests are only forwarded to Chainlit if they match the
        designated subpath, preventing routing collisions.

        If a request's path doesn't start with the configured subpath, the middleware
        returns a 404 response instead of forwarding to Chainlit's default route.
        """

        async def dispatch(self, request: Request, call_next):
            if not request.url.path.startswith(api_full_path):
                return JSONResponse(status_code=404, content={"detail": "Not found"})

            return await call_next(request)

    chainlit_app.add_middleware(ChainlitMiddleware)

    app.mount(path, chainlit_app)








app2 = FastAPI(root_path="/")
              
@app2.get("/app")
def read_main():
    return {"message": "Hello World from main app"}

mount_chainlit(app=app2, target="my_cl_app.py", path="/chainlit")
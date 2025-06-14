from fastapi import FastAPI
#from chainlit.utils import mount_chainlit



app = FastAPI(routepath="/api")
              
@app.get("/app")
def read_main():
    return {"message": "Hello World from main api app"}

@app.get("/")
def chainie():  
    return {"message": "Hello World  from /api/app or /api/chainlit"}

@app.get("/api2")
def chainies():  
    return {"message": "Hello World  from /api/api2"}

#mount_chainlit(app=app, target="my_cl_app.py", path="/chainlit")
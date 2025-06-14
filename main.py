from fastapi import FastAPI
#from chainlit.utils import mount_chainlit



app = FastAPI()
              
@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}

@app.get("/")
def chainie():  
    return {"message": "Hello World /app or /chainlit"}

@app.get("/apichain")
def chainiee():  
    return {"message": "Hello World apichain"}

#mount_chainlit(app=app, target="my_cl_app.py", path="/chainlit")
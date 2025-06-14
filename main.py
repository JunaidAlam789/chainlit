from fastapi import FastAPI



app = FastAPI()
              
@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}

@app.get("/chainlit")

def chainie():
    from chainlit.utils import mount_chainlit
    mount_chainlit(app=app, target="my_cl_app.py", path="/chainlit")
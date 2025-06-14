from fastapi import FastAPI
#from chainlit.utils import mount_chainlit


app2 = FastAPI(root_path="/")
              
@app2.get("/app")
def read_main():
    return {"message": "Hello World from main app"}

#mount_chainlit(app=app2, target="my_cl_app.py", path="/chainlit")
from fastapi import FastAPI, Header, Body
app = FastAPI()
@app.get("/hi")
def greet():
    return f"Hello? World? hie"

# url
@app.get("/hi/{who}")
def greet(who):
    return f"Hello? {who}?"

# query params
@app.get("/hit")
def greet(who):
    return f"Hello? {who}?"

# Header
@app.post("/hihead")
def greet(who:str = Header()):
    return f"greetings {who}"

# Body
@app.post("/hibody")
def greet(who:str = Body(embed=True)):
    return f"greetings {who}"


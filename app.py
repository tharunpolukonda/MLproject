from fastapi import FastAPI
app=FastAPI()

@app.get('/')#decorater
def sampleProgram():
    return "Hello THARUN THIS IS FASTAPI"
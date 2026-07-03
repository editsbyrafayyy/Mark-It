from fastapi import FastAPI

app = FastAPI() # create an instance of FastAPI to use
@app.get("/")

async def root():
	return {"message": "hello world!"}

from fastapi import FastAPI
import uvicorn
import json
app = FastAPI()

announcement_dict = dict()
@app.get("/")
async def root():
    return announcement_dict

index = 0
@app.get("/add/{announcement}")
async def add_item(announcement: str):
    global index
    index += 1
    announcement_dict[index] = announcement
    return "OK"

@app.get("/del/{id}")
async def delete_item(id: int):
    global index
    if id in announcement_dict:
        del announcement_dict[id]
        return "200"
    else:
        return "201"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)

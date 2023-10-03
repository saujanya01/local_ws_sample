import uvicorn
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Hello World"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
	await websocket.accept()
	while True:
		data = await websocket.receive_text()
		await websocket.send_text(f"Message received: {data}")


def main():
	uvicorn.run(
		app=app,
		host="0.0.0.0",
		port=8000,
	)

main()
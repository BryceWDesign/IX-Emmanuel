"""
IX-Emmanuel REST API Server

Provides HTTP access to the mathematics and logic query processor.
Enables communication with IX-Gibson orchestrator and external clients.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from core.query_processor import IXEmmanuelQueryProcessor

app = FastAPI()
query_processor = IXEmmanuelQueryProcessor()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def handle_query(request: QueryRequest):
    if not request.query or request.query.strip() == "":
        raise HTTPException(status_code=400, detail="Query must not be empty.")
    try:
        answer = query_processor.process_query(request.query)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8004)

"""
IX-Emmanuel REST API Server

Exposes HTTP endpoints for querying philosophical and psychological
frameworks via the IX-Emmanuel reasoning engine.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from core.query_processor import IXEmmanuelQueryProcessor

app = FastAPI()
query_engine = IXEmmanuelQueryProcessor()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def process_query(request: QueryRequest):
    if not request.query or request.query.strip() == "":
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    try:
        result = query_engine.process_query(request.query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8060)

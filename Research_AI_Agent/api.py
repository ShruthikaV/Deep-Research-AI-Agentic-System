from fastapi import FastAPI
from langchain_setup import process_query

app = FastAPI()

@app.get("/query/")
def query_endpoint(user_input: str):
    """Run agents on user query"""
    result = process_query(user_input)
    return {"response": result["response"]}  # Ensure correct format

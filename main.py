from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Allow CORS from any origin (customize later if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class TextInput(BaseModel):
    text: str

@app.post("/embed")
def generate_embedding(data: TextInput):
    embedding = model.encode(data.text).tolist()
    return { "embedding": embedding }

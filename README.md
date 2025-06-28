# 🧠 Embedding API - Dockerized FastAPI Service

This project is a **Dockerized FastAPI API** that generates **sentence embeddings** using [Hugging Face's Sentence Transformers](https://www.sbert.net/). It is built to support **text similarity** features in applications like question-answer platforms, recommendation engines, and duplicate detection.

> **Model used:** `all-MiniLM-L6-v2` (384-dimensional sentence embeddings)

---

## 🚀 Features

- Generates embeddings from input text
- Uses HuggingFace's `sentence-transformers`
- FastAPI-based HTTP API
- Fully containerized with Docker
- CORS enabled for frontend/backend integration

---

## 🛠 Prerequisites

Before you begin, make sure you have the following installed:

- [Docker](https://www.docker.com/get-started) (required)
- [Git](https://git-scm.com/) (for cloning)

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/embedding-api.git
cd embedding-api
```

### 2. Build the Docker Image

```bash
docker build -t embedding-api .
```

> **Note:** This may take a few minutes on the first build as it installs Python packages and the transformer model.

### 3. Run the Docker Container

You can run the Embedding API Docker container using **either** of the following commands:

#### 🔹 Option 1: Run in Foreground (until closed)
```bash
docker run -p 8000:8000 embedding-api
```

* Runs the container in the **foreground**.
* Stops when you close the terminal or press `Ctrl + C`.
* Ideal for quick testing or development.

#### 🔹 Option 2: Run in Background (auto-restart on reboot)

```bash
docker run -d --restart always -p 8000:8000 --name embedding-api embedding-api
```

* Runs the container in **detached mode** (in the background).
* Automatically **restarts** the container if it stops or after a system reboot.
* Recommended for production or persistent usage.

---

**Flags explained:**

* `-d`: Run container in the background (detached mode).
* `--restart always`: Ensure the container restarts automatically on system reboot or crash.
* `-p 8000:8000`: Maps port `8000` of the container to port `8000` on your host machine.
* `--name embedding-api`: Names the container `embedding-api` for easier management.

---

## 📨 API Usage

### POST /embed

Generates an embedding from a given piece of text.

#### 🔸 Request

```http
POST /embed
Content-Type: application/json
```

```json
{
  "text": "How to connect MongoDB with Mongoose?"
}
```

#### 🔸 Response

```json
{
  "embedding": [0.0481, 0.0510, -0.0670, "..."]
}
```

> **Note:** The response contains a 384-dimensional vector array.

---

## 🧪 Test Locally

You can test the API using curl:

```bash
curl -X POST http://localhost:8000/embed \
  -H "Content-Type: application/json" \
  -d '{"text": "Your input text here"}'
```

---

## 🧠 How to Use Embeddings - Cosine Similarity

Embeddings convert human language into vectors that capture semantic meaning. To measure similarity between texts, you calculate the **cosine similarity** between their embedding vectors.

### 🐍 Python Implementation

```python
import numpy as np
import requests
from scipy.spatial.distance import cosine

def get_embedding(text):
    """Get embedding from the API"""
    response = requests.post(
        "http://localhost:8000/embed",
        json={"text": text}
    )
    return np.array(response.json()["embedding"])

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors"""
    # Using scipy (1 - cosine_distance = cosine_similarity)
    return 1 - cosine(vec1, vec2)

def cosine_similarity_manual(vec1, vec2):
    """Manual cosine similarity calculation"""
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)

# Example usage
if __name__ == "__main__":
    # Get embeddings for two texts
    text1 = "How to connect to MongoDB database?"
    text2 = "MongoDB connection setup guide"
    text3 = "How to bake a chocolate cake?"
    
    embed1 = get_embedding(text1)
    embed2 = get_embedding(text2)
    embed3 = get_embedding(text3)
    
    # Calculate similarities
    similarity_1_2 = cosine_similarity(embed1, embed2)
    similarity_1_3 = cosine_similarity(embed1, embed3)
    
    print(f"Similarity between text1 and text2: {similarity_1_2:.4f}")
    print(f"Similarity between text1 and text3: {similarity_1_3:.4f}")
    
    # Find most similar text
    if similarity_1_2 > similarity_1_3:
        print("Text1 is more similar to Text2 (MongoDB related)")
    else:
        print("Text1 is more similar to Text3")
```

### 🌐 JavaScript Implementation

```javascript
// Function to get embedding from API
async function getEmbedding(text) {
    const response = await fetch('http://localhost:8000/embed', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text })
    });
    
    const data = await response.json();
    return data.embedding;
}

// Calculate cosine similarity between two vectors
function cosineSimilarity(vecA, vecB) {
    // Calculate dot product
    let dotProduct = 0;
    for (let i = 0; i < vecA.length; i++) {
        dotProduct += vecA[i] * vecB[i];
    }
    
    // Calculate magnitudes
    let magnitudeA = 0;
    let magnitudeB = 0;
    
    for (let i = 0; i < vecA.length; i++) {
        magnitudeA += vecA[i] * vecA[i];
        magnitudeB += vecB[i] * vecB[i];
    }
    
    magnitudeA = Math.sqrt(magnitudeA);
    magnitudeB = Math.sqrt(magnitudeB);
    
    // Return cosine similarity
    return dotProduct / (magnitudeA * magnitudeB);
}

// Example usage
async function findSimilarTexts() {
    const texts = [
        "How to connect to MongoDB database?",
        "MongoDB connection setup guide", 
        "How to bake a chocolate cake?",
        "Database connection troubleshooting"
    ];
    
    // Get embeddings for all texts
    const embeddings = [];
    for (const text of texts) {
        const embedding = await getEmbedding(text);
        embeddings.push(embedding);
    }
    
    // Compare first text with others
    const baseText = texts[0];
    console.log(`Comparing "${baseText}" with:`);
    
    for (let i = 1; i < texts.length; i++) {
        const similarity = cosineSimilarity(embeddings[0], embeddings[i]);
        console.log(`"${texts[i]}": ${similarity.toFixed(4)}`);
    }
    
    // Find most similar text
    let maxSimilarity = -1;
    let mostSimilarIndex = -1;
    
    for (let i = 1; i < embeddings.length; i++) {
        const similarity = cosineSimilarity(embeddings[0], embeddings[i]);
        if (similarity > maxSimilarity) {
            maxSimilarity = similarity;
            mostSimilarIndex = i;
        }
    }
    
    console.log(`\nMost similar text: "${texts[mostSimilarIndex]}" (${maxSimilarity.toFixed(4)})`);
}

// Run the example
findSimilarTexts().catch(console.error);
```

### 🎯 Practical Use Cases

#### 1. **Duplicate Question Detection**
```python
def is_duplicate_question(new_question, existing_questions, threshold=0.85):
    new_embedding = get_embedding(new_question)
    
    for question in existing_questions:
        existing_embedding = get_embedding(question['text'])
        similarity = cosine_similarity(new_embedding, existing_embedding)
        
        if similarity > threshold:
            return True, question, similarity
    
    return False, None, 0
```

#### 2. **Content Recommendation**
```javascript
async function recommendSimilarContent(userQuery, contentDatabase, topK = 5) {
    const queryEmbedding = await getEmbedding(userQuery);
    const similarities = [];
    
    for (const content of contentDatabase) {
        const contentEmbedding = await getEmbedding(content.text);
        const similarity = cosineSimilarity(queryEmbedding, contentEmbedding);
        
        similarities.push({
            content: content,
            similarity: similarity
        });
    }
    
    // Sort by similarity and return top K
    return similarities
        .sort((a, b) => b.similarity - a.similarity)
        .slice(0, topK);
}
```

#### 3. **Search with Semantic Understanding**
```python
def semantic_search(query, documents, top_k=10):
    query_embedding = get_embedding(query)
    results = []
    
    for doc in documents:
        doc_embedding = get_embedding(doc['content'])
        similarity = cosine_similarity(query_embedding, doc_embedding)
        
        results.append({
            'document': doc,
            'similarity': similarity
        })
    
    # Sort by similarity and return top results
    return sorted(results, key=lambda x: x['similarity'], reverse=True)[:top_k]
```

### 📊 Similarity Score Interpretation

- **0.9 - 1.0**: Very high similarity (likely duplicates or paraphrases)
- **0.7 - 0.9**: High similarity (related content)
- **0.5 - 0.7**: Moderate similarity (some relationship)
- **0.3 - 0.5**: Low similarity (weak relationship)
- **0.0 - 0.3**: Very low similarity (unrelated)

---

## 🌐 CORS

This API is CORS-enabled to support cross-origin requests (e.g., from your frontend at `localhost:4000`).

---

## 📂 Project Structure

```
embedding-api/
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧼 Useful Docker Commands

| Task | Command |
|------|---------|
| View running containers | `docker ps` |
| Stop container | `docker stop embedding-api` |
| Start container | `docker start embedding-api` |
| Rebuild after code change | `docker build -t embedding-api .` |
| View logs | `docker logs -f embedding-api` |
| Open container shell | `docker exec -it embedding-api sh` |

---

## 🧠 Why Use Embeddings?

Embeddings convert human language into vectors that capture meaning. You can use cosine similarity on these vectors to:

- Detect duplicate or similar questions
- Recommend related posts or content
- Power search or clustering features
- Build intelligent chatbots and Q&A systems
- Create content classification systems
- Enable semantic search capabilities

---

## 📝 License

This project is open-source and free to use.

---

## 💬 Questions or Feedback?

Feel free to open an issue or reach out if you have any questions or suggestions.

---

**Want to extend this project?** Consider adding:
- Docker Compose support
- Pre-built images on Docker Hub or GitHub Container Registry
- Additional embedding models
- Batch processing endpoints
- Built-in similarity calculation endpoints
- Vector database integration (Pinecone, Weaviate, etc.)
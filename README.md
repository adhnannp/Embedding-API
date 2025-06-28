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

Sure! Here's the improved markdown version of that section, with a clear explanation that users can choose either of the two commands based on their needs:


### 3. Run the Docker Container

You can run the Embedding API Docker container using **either** of the following commands:

#### 🔹 Option 1: Run in Foreground (until closed)
```bash
docker run -p 8000:8000 embedding-api
````

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

## 🌐 CORS

This API is CORS-enabled to support cross-origin requests (e.g., from your frontend at `localhost:4000`).

---

## 🧪 Test Locally

You can test the API using curl:

```bash
curl -X POST http://localhost:8000/embed \
  -H "Content-Type: application/json" \
  -d '{"text": "Your input text here"}'
```

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
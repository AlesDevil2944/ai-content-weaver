# AI Content Weaver 🤖

AI Content Weaver is a full-stack web application that uses Google's Gemini AI to generate high-quality content. It provides a simple dashboard to draft informative blog posts, promotional articles, and creative writing pieces, complete with built-in SEO analysis.

This project was built with a **FastAPI (Python)** backend and a **React (Vite)** frontend.

---

## 🌟 Features

* **AI-Powered Content:** Generates three distinct content types using Google's `gemini-1.0-pro` model.
* **Simple Dashboard:** An easy-to-use form to submit a brief, tone, and length.
* **Built-in SEO Analysis:**
    * Generates an SEO-friendly **Meta Title**.
    * Generates a compelling **Meta Description**.
    * Calculates a **Flesch-Kincaid Readability Score** for on-page optimization.
* **Export Function:** Download the generated content as either HTML or Markdown.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python, Uvicorn
* **Frontend:** React, Vite, JavaScript, CSS
* **AI:** Google Gemini API (`google-generativeai`)
* **Analysis:** `textstat` (for readability), `markdownify` (for HTML-to-MD)

---

## 🚀 Setup and Installation

Follow these steps to run the project locally.

### Prerequisites

* Python 3.9+
* Node.js 18+
* A Google AI Studio API Key

### 1. Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create
    python -m venv venv
    
    # Activate (macOS/Linux)
    source venv/bin/activate
    
    # Activate (Windows)
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create your environment file:**
    * Create a file named `.env` in the `/backend` directory.
    * Add your API keys (the OpenAI one is not used but required by the config):
    ```
    OPENAI_API_KEY="key_not_used"
    GOOGLE_API_KEY="your_google_api_key_here"
    ```

5.  **Run the backend server:**
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```
    The API will be running at `http://localhost:8000/docs`.

### 2. Frontend Setup

1.  **Open a new terminal** and navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Run the frontend server:**
    ```bash
    npm run dev
    ```
    The dashboard will be available at `http://localhost:5173`.
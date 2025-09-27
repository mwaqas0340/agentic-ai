# 🤖 Gemini AI Assistant using Chainlit & OpenAI Agent SDK

This project is an AI assistant powered by Google's Gemini 2.0 Flash model using OpenAI's Agent SDK. It is integrated into a Chainlit frontend to provide real-time, streaming responses.

---

## 🚀 Features

- 🧠 Gemini 2.0 Flash model support
- 💬 Chainlit UI for live chat
- 📡 Real-time message streaming
- 🔐 Environment-based API key management
- ⚙️ OpenAI Agent SDK for modular logic

---

## 📁 Project Structure

your-project/
│
├── main.py # Main Chainlit app
├── agents/ # Agent, Runner, and model classes
├── .env # Environment file with API key
├── requirements.txt # Project dependencies
└── README.md # This file


---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chainlit-gemini-assistant.git
cd chainlit-gemini-assistant
2. Create a virtual environment (recommended)

python -m venv venv
.venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
3. Install dependencies using uv

uv install -r requirements.txt
If requirements.txt is not available, use:


uv install chainlit openai-agents python-dotenv
🔐 Setup Environment Variables
Create a .env file in your project root:

GEMINI_API_KEY=your_gemini_api_key_here


▶️ Running the App

chainlit run main.py -w
Open in your browser: http://localhost:8000




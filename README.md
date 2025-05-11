# AI Chatbot with LangGraph

---

# 🧠 Climate-Aware LangGraph Chatbot

This project is a simple **LangGraph-based chatbot** that uses Google's Gemini (`gemini-2.0-flash`) model to simulate a conversational agent. It demonstrates how to structure a **stateful chatbot with streaming outputs** using LangChain's new graph-based framework, `LangGraph`.

---

## 🚀 Features

* 🔁 **Stateful conversation flow** using `StateGraph`
* 💬 **Streaming responses** from Gemini model
* 🧱 **Modular graph nodes**, ready for extension
* 🧠 **LLM backend:** Google Gemini 2.0 Flash
* 🔒 **Secure key management** via environment variables

---

## 📦 Requirements

* Python 3.9+
* [LangChain](https://github.com/langchain-ai/langchain)
* [LangGraph](https://github.com/langchain-ai/langgraph)
* `google-generativeai` access and API Key

---

## 🔧 Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/langgraph-chatbot.git
   cd langgraph-chatbot
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Google API Key:**
   Create a `.env` file or export the environment variable:

   ```bash
   export GOOGLE_API_KEY="your-google-api-key"
   ```

4. **Run the chatbot:**

   ```bash
   python chatbot.py
   ```

---

## 🛠️ How It Works

### 🔁 LangGraph Flow

* The chatbot is built using a **state graph**, where:

  * `State` holds the ongoing messages.
  * The `chatbot` node processes user input and appends the LLM's response.
  * The conversation state is streamed using `graph.stream(...)`.

### 🧠 LLM Invocation

* The `gemini-2.0-flash` model from Google's GenAI suite is used via `langchain.chat_models`.

---

## 🧪 Example Interaction

```bash
User: Tell me about LangGraph.
Assistant: LangGraph is a library for building stateful, multi-step workflows with LangChain...
```

---

## 📁 Project Structure

```
.
├── chatbot.py        # Main logic and streaming loop
├── requirements.txt  # Dependencies
└── README.md         # This file
```

---

## 📌 Notes

* This example uses a **single node graph**, but you can easily add more nodes like sentiment analysis, logging, or weather decision logic.
* Ideal as a base to integrate **image inputs**, **self-driving logic**, or **climate-aware decisions**.

---

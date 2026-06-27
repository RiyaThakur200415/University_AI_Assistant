🎓 University AI Assistant
A Multi-Agent University AI Assistant built using LangGraph, LangChain, Ollama, Streamlit, and SQLite. The assistant intelligently routes student queries to specialized AI agents for Admission, Hostel, Academics, Placements, Profile Management, and Memory.

The project demonstrates multi-agent architecture, state management, persistent conversation memory, and LLM-powered intent classification.

🚀 Features
🤖 Multi-Agent Architecture using LangGraph

🎓 Dedicated Agents for:

Admission

Hostel

Academics

Placements

Profile Management

Memory

General Conversation

🧠 Persistent Memory using SQLite Checkpointer

👤 Automatic Student Profile Extraction

🛣️ Intelligent Query Routing

💬 Modern Streamlit Chat Interface

🦙 Local LLM using Ollama (Qwen2.5:3B)

📚 Modular Knowledge Base

⚡ Fast Local Inference

# 🏗️ System Architecture

The **University AI Assistant** follows a **Modular Multi-Agent Architecture** powered by **LangGraph**. Instead of processing every query through a single chatbot, the system intelligently classifies the user's intent and routes it to a specialized AI agent responsible for a specific university service.

---

## 🌐 Architecture Overview

```text
                              👨‍🎓 Student
                                   │
                                   ▼
                        🖥️ Streamlit Frontend
                                   │
                                   ▼
                       ⚙️ LangGraph Workflow Engine
                                   │
             ┌─────────────────────┴─────────────────────┐
             ▼                                           ▼
     👤 Profile Extractor                      🧠 Intent Classifier
             │                                           │
             └─────────────────────┬─────────────────────┘
                                   ▼
                            🚦 Agent Router
                                   │
 ┌─────────────┬────────────┬────────────┬────────────┬────────────┬────────────┬────────────┐
 ▼             ▼            ▼            ▼            ▼            ▼            ▼
🎓 Admission 🏠 Hostel 📚 Academic 💼 Placement 👤 Profile 🧠 Memory 💬 General
   Agent        Agent        Agent        Agent        Agent        Agent        Agent
       │            │            │            │
       └────────────┴────────────┴────────────┴───────────────┐
                                                              ▼
                                                     🤖 Ollama (Qwen2.5:3B)
                                                              │
                                                              ▼
                                                     💬 AI Response
                                                              │
                                                              ▼
                                                💾 SQLite Conversation Memory
```

---

# 📦 Core Components

## 🖥️ 1. Streamlit Frontend

The frontend provides an intuitive chat interface where students can interact with the AI assistant.

### ✨ Responsibilities

* 💬 Accept user queries
* 📜 Display conversation history
* 🔑 Manage Session IDs
* 🎯 Send requests to LangGraph
* 📥 Display AI responses

---

## ⚙️ 2. LangGraph Workflow

LangGraph orchestrates the complete execution flow of the chatbot.

### 🔄 Workflow Steps

* 👤 Profile Extraction
* 🧠 Intent Classification
* 🚦 Agent Routing
* 🤖 AI Response Generation
* 💾 Memory Checkpointing

This modular workflow keeps every component independent and easy to maintain.

---

## 👤 3. Profile Extraction Node

Before classifying a query, the system checks whether the user is sharing personal information.

### ✅ Extracted Information

* 👤 Student Name
* 🆔 Register Number
* 🎓 Department

### 📝 Examples

* My name is Riya
* My register number is 23BCE7730
* I'm from CSE

---

## 🧠 4. Intent Classifier

The classifier predicts the user's intent and categorizes the query into one of the supported domains.

### 📂 Supported Categories

* 🎓 Admission
* 🏠 Hostel
* 📚 Academic
* 💼 Placement
* 👤 Profile
* 🧠 Memory
* 💬 General

The system combines **rule-based classification** with **LLM-based fallback** for improved accuracy.

---

## 🚦 5. Agent Router

The Agent Router forwards the classified query to the appropriate specialized AI agent.

This modular design follows the **Single Responsibility Principle (SRP)**, where every agent handles only its own domain.

---

# 🤖 Specialized AI Agents

## 🎓 Admission Agent

Handles admission-related questions.

### Examples

* 💰 Fees
* 📋 Eligibility
* 📚 Courses
* 📝 Admission Process
* 🏆 Entrance Examination

**Knowledge Source:** `admission_kb.py`

---

## 🏠 Hostel Agent

Handles hostel-related queries.

### Examples

* 🛏️ Room Types
* 📡 Wi-Fi
* 🍽️ Mess
* 🧺 Laundry
* ⏰ Curfew
* 🏋️ Gym

**Knowledge Source:** `hostel_kb.py`

---

## 📚 Academic Agent

Provides academic information.

### Examples

* 📅 Attendance
* 📖 Credits
* 🎯 GPA
* 📝 Semester
* 📑 Backlogs

**Knowledge Source:** `academic_kb.py`

---

## 💼 Placement Agent

Handles placement-related queries.

### Examples

* 🏢 Companies
* 💰 Salary Packages
* 👨‍💻 Internships
* ✅ Placement Eligibility

**Knowledge Source:** `placement_kb.py`

---

## 👤 Profile Agent

Stores user information shared during the conversation.

### Stores

* 👤 Name
* 🆔 Register Number
* 🎓 Department

This allows the chatbot to personalize future interactions.

---

## 🧠 Memory Agent

Retrieves previously stored user information.

### Examples

* ❓ What is my name?
* ❓ Do you remember my department?
* ❓ What do you know about me?

---

## 💬 General Agent

Handles casual conversations.

### Examples

* 👋 Hello
* 🙏 Thank You
* 😊 Nice
* 👋 Goodbye

---

# 🤖 Ollama (Qwen2.5:3B)

The chatbot uses **Qwen2.5:3B** running locally through **Ollama**.

### Responsibilities

* 🧠 Natural Language Understanding
* ✨ Response Generation
* 🏷️ Intent Classification

### Benefits

* ⚡ Fast local inference
* 🔒 Privacy
* 🌐 Offline support
* 💸 No API cost

---

# 💾 Conversation Memory

Persistent conversation memory is implemented using **SQLite Checkpointer**.

Each user conversation is associated with a unique **Thread ID**, allowing the assistant to remember information across multiple interactions.

### Stored Information

* 👤 Student Name
* 🆔 Register Number
* 🎓 Department
* 💬 Conversation State

---

# 🔄 End-to-End Data Flow

```text
👨‍🎓 User
      │
      ▼
🖥️ Streamlit Frontend
      │
      ▼
👤 Profile Extraction
      │
      ▼
🧠 Intent Classification
      │
      ▼
🚦 Agent Routing
      │
      ▼
🤖 Specialized AI Agent
      │
      ▼
🦙 Ollama (Qwen2.5:3B)
      │
      ▼
💾 SQLite Memory
      │
      ▼
💬 Response to User
```

---

# ✨ Design Highlights

* 🧩 Modular Multi-Agent Architecture
* 🚀 LangGraph Workflow Orchestration
* 🧠 Persistent Conversation Memory
* 👤 Automatic Profile Extraction
* 🎯 Intelligent Intent Classification
* 💬 Context-Aware Responses
* 🔒 Local LLM Inference with Ollama
* 📦 Easily Extensible Architecture for New Agents
* 🖥️ Interactive Streamlit User Interface

This architecture makes it easy to add future modules such as **📚 Library**, **💳 Finance**, **📝 Examination**, or **🚌 Transport** without modifying the existing workflow.

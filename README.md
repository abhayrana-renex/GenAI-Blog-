# ⚡️ GenAI Blog Generator

> ✨ *An intelligent blog creation tool powered by LLaMA and Streamlit — designed to craft engaging, professional, and SEO-ready blog posts with AI precision.*

---

## 🚀 **Overview**

**GenAI Blog Generator** allows you to effortlessly generate blog posts using advanced **LLaMA-based language models**.  
Just provide your **topic, style, tone, word count**, and the app crafts a **structured, well-researched, and formatted blog post** — complete with headings, sources, and professional writing tone.

---

## 🎨 **Key Features**

- 🧠 **AI-Powered Blog Generation** — Uses LLaMA (TinyLlama / Local LLM) via LangChain’s `CTransformers`.
- 🎨 **Sleek Streamlit UI** — Clean, responsive, and easy to use.
- ✍️ **Smart Prompts** — Generates articles with APA-style formatting, citations, and improved phrasing.
- 🧾 **Custom Inputs** — Define blog length, tone, and target audience.
- 🪄 **Instant Output** — Get formatted blog text directly in your browser.

---

## 💻 **Tech Stack**

| Component | Description |
|------------|-------------|
| 🦙 **LLaMA Model** | Local lightweight LLM (TinyLlama-1.1B or similar GGUF) |
| 🧩 **LangChain** | LLM orchestration framework |
| 🧠 **CTransformers** | Efficient model loader for GGUF-based LLaMA models |
| 🖥 **Streamlit** | Web app framework for AI-powered tools |
| 🐍 **Python 3.10+** | Core programming language |

---

## ⚙️ **Installation & Setup**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/abhayrana-renex/GenAI-Blog-.git
cd GenAI-Blog-

### 2️⃣ Create Virtual Environment

### 3️⃣ Install Dependencies

### 4️⃣ Run the App

🧩 Project Structure

GenAI-Blog-/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Dependencies list
├── models/                 # (ignored) Local GGUF models
├── .gitignore              # Ignore unnecessary files
└── README.md               # Project documentation

📸 Interface Preview

📦 Model Configuration

llm = CTransformers(
    model="models/TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf",
    model_type="llama",
    config={"max_new_tokens": 512, "temperature": 0.7}
)

🪄 Example Output Snippet

Title: The Future of Artificial Intelligence in Content Creation

Artificial Intelligence (AI) has redefined how businesses approach digital marketing.
According to Gartner (2024), over 60% of global organizations are projected to use AI for content generation by 2026.

“AI is not replacing creativity — it’s amplifying it.”
— Harvard Business Review (2023)

⸻

🧰 Future Enhancements
	•	📚 Add model selection dropdown (TinyLlama, Mistral, Phi-2)
	•	🗣 Add text-to-speech blog narration
	•	🌍 Add export to PDF / DOCX option
	•	🎯 Add SEO keyword optimization module


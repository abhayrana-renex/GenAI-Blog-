import streamlit as st
from langchain_community.llms import CTransformers

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="AI Blog Generator 🧠",
    page_icon="✍️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------- CUSTOM STYLING -------------------
st.markdown("""
    <style>
    /* Background and text */
    body {
        background-color: #0e1117;
        color: #f5f5f5;
    }
    .stApp {
        background: linear-gradient(145deg, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Inter', sans-serif;
    }

    /* Title */
    h1 {
        text-align: center;
        color: #00e0ff;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.5em;
    }

    /* Input boxes */
    .stTextInput > div > div > input {
        background-color: #1c1f25;
        color: white;
        border: 1px solid #00e0ff;
        border-radius: 10px;
    }

    /* Dropdown */
    .stSelectbox > div > div {
        background-color: #1c1f25;
        color: white;
        border: 1px solid #00e0ff;
        border-radius: 10px;
    }

    /* Buttons */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00e0ff, #00b3b3);
        color: black;
        border-radius: 15px;
        height: 3em;
        width: 10em;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #00ffc6, #00e0ff);
        transform: scale(1.05);
    }

    /* Output */
    .output {
        background-color: #1c1f25;
        border-left: 4px solid #00e0ff;
        padding: 1.5em;
        border-radius: 12px;
        margin-top: 1em;
        color: #f5f5f5;
        box-shadow: 0 0 15px rgba(0, 224, 255, 0.2);
    }

    /* Subtle glow animation */
    @keyframes glow {
        0% { text-shadow: 0 0 5px #00e0ff; }
        50% { text-shadow: 0 0 20px #00e0ff; }
        100% { text-shadow: 0 0 5px #00e0ff; }
    }
    h1 {
        animation: glow 3s infinite ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------- LLM MODEL -------------------
llm = CTransformers(
    model="/Users/abhayrana/Downloads/llamamodels/models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf",
    model_type="llama",
    config={"max_new_tokens": 512, "temperature": 0.8}
)

# ------------------- APP TITLE -------------------
st.markdown("<h1>AI Blog Generator ✍️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#ccc;'>Generate high-quality, research-backed blogs using the power of LLaMA.</p>", unsafe_allow_html=True)

# ------------------- INPUT SECTION -------------------
col1, col2 = st.columns(2)

with col1:
    topic = st.text_input("🧠 Blog Topic", placeholder="e.g., Large Language Models")
with col2:
    words = st.text_input("📝 Word Count", placeholder="e.g., 500")

audience = st.selectbox(
    "🎯 Audience Type",
    ["Researchers", "Students", "Professionals", "General Audience"]
)

# ------------------- HIDDEN INSTRUCTION -------------------
instruction = (
    "Use appropriate headings, subheadings, bullet points, and quotes. "
    "Make sure that the blog post is written in a clear and concise style. "
    "The language used should be formal but not stiff. "
    "Include at least 5 reliable sources. Proofread and edit for errors and "
    "improve word choices, phrasing, and flow to improve clarity and persuasiveness. "
    "Use bolding and emphasis techniques for effective message delivery."
)

# ------------------- GENERATE FUNCTION -------------------
def generate_blog(topic, words, audience):
    prompt = (
        f"Write a blog post on the topic '{topic}' for {audience}. "
        f"The blog should be approximately {words} words long. "
        f"Follow these professional writing guidelines:\n\n{instruction}"
    )
    response = llm.invoke(prompt)
    return response

# ------------------- GENERATE BUTTON -------------------
center_button = st.columns(3)[1]
with center_button:
    generate = st.button("🚀 Generate")

# ------------------- OUTPUT -------------------
if generate:
    if not topic.strip() or not words.strip():
        st.warning("⚠️ Please enter both topic and word count before generating.")
    else:
        with st.spinner("✨ Generating your blog..."):
            output = generate_blog(topic, words, audience)
            st.markdown("<div class='output'>", unsafe_allow_html=True)
            st.markdown("### 🧾 Generated Blog", unsafe_allow_html=True)
            st.markdown(output, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
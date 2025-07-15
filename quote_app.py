import streamlit as st
import openai

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="AI-Powered Quote Generator",
    layout="wide"
)


# --- Custom CSS Styling ---
st.markdown("""
    <style>
        body, .stApp {
            background-color: #f8f8f8;
    
        }

        /* Hide all anchor links globally */
a[href^="#"] {
    display: none !important;
}

header [data-testid="stMarkdownContainer"] a,
section [data-testid="stMarkdownContainer"] a {
    display: none !important;
}

        .block-container {
            padding-top: 2rem;
        }
        h1, h2, h3, h4, h5, h6 {
            display: block;
        }
        .animated-title {
            font-size: 40px;
            font-weight: bold;
            color: #004d4d;
            text-align: center;
            margin-top: 40px;
            animation: bounceIn 1s ease-out;
        }
        @keyframes bounceIn {
            0% {
                transform: scale(0.8);
                opacity: 0;
            }
            60% {
                transform: scale(1.05);
                opacity: 1;
            }
            100% {
                transform: scale(1);
            }
        }
        .subtitle {
            text-align: center;
            font-size: 1.1rem;
            color: #003333;
            margin-bottom: 2rem;
        }
        .stTextInput > div > div > input,
        .stSelectbox > div > div {
            background-color: #ffffff !important;
            color: #000000;
            border-radius: 5px;
            border: 1px solid #cccccc;
        }
        .stButton>button {
            background-color: #009999;
            color: white;
            font-weight: bold;
            border-radius: 5px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #007777;
        }
        .feedback-box {
            background-color: #e0f7f7;
            padding: 1.5rem;
            border-radius: 10px;
            width: 400px;
            margin: 2rem auto;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        }
        .feedback-box textarea {
            width: 100%;
            height: 100px;
            border-radius: 5px;
        }
        label[data-testid="stMarkdownContainer"] > div > a {
            display: none;
        }
    </>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown('<h1 class="animated-title">AI-POWERED QUOTE GENERATOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Try basic and structured prompts to see how well-crafted inputs transform GenAI responses.</p>', unsafe_allow_html=True)

# --- OpenAI API Key ---
api_key = st.secrets["OPENAI_API_KEY"]

# --- Two Column Layout ---
col1, col2 = st.columns(2)

# --- Basic Prompt ---
with col1:
    st.subheader("BASIC PROMPT")
    basic_prompt = st.text_input("Mood or Theme (e.g., courage, success)", key="basic_input")
    if st.button("Generate", key="generate_basic"):
        if not basic_prompt:
            st.warning("Please enter a theme.")
        else:
            with st.spinner("Generating quote..."):
                try:
                    client = openai.OpenAI(api_key=api_key)
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a quote generator."},
                            {"role": "user", "content": f"Give me a motivational quote about {basic_prompt}."}
                        ]
                    )
                    quote = response.choices[0].message.content.strip()
                    st.success("Here's your quote:")
                    st.markdown(f'<p style="color:#004d4d; font-size:18px;">💬 {quote}</p>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {e}")

# --- Structured Prompt ---
with col2:
    st.subheader("STRUCTUREC PROMPT")
    mood = st.text_input("Mood (e.g., resilience, creativity)", key="mood")
    audience = st.text_input("Audience (optional, e.g., students, founders)", key="audience")

    tone_options = ["Warm", "Bold", "Empowering", "Professional", "Other"]
    tone = st.selectbox("Tone", tone_options, key="tone")
    custom_tone = st.text_input("Enter custom tone", key="custom_tone") if tone == "Other" else tone

    style_options = ["Inspirational", "Reflective", "Actionable", "Other"]
    style = st.selectbox("Style", style_options, key="style")
    custom_style = st.text_input("Enter custom style", key="custom_style") if style == "Other" else style

    if st.button("Generate", key="generate_structured"):
        if not mood:
            st.warning("Please enter a mood.")
        else:
            with st.spinner("Generating quote..."):
                try:
                    final_tone = custom_tone if tone == "Other" else tone
                    final_style = custom_style if style == "Other" else style
                    prompt = f"Write a {final_tone.lower()} and {final_style.lower()} motivational quote about being {mood.lower()}."
                    if audience:
                        prompt += f" Tailor it for {audience.lower()}."
                    client = openai.OpenAI(api_key=api_key)
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a skilled motivational quote generator."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    quote = response.choices[0].message.content.strip()
                    st.success("Here’s your crafted quote:")
                    st.markdown(f'<p style="color:#004d4d; font-size:18px;">💬 {quote}</p>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {e}")

# Feedback Section
st.markdown("""
    <style>
    .feedback-card {
        background-color: #f5f5f5;
        padding: 30px 25px 20px 25px;
        border-radius: 10px;
        width: 500px;
        margin: 40px auto;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
    .feedback-card h3 {
        margin-bottom: 10px;
        font-size: 22px;
        color: #333333;
    }
    .feedback-card p {
        font-size: 14px;
        color: #666666;
        margin-bottom: 15px;
    }
    .feedback-box textarea {
        width: 100% !important;
        height: 100px !important;
        border-radius: 5px;
        border: 1px solid #cccccc;
        padding: 10px;
        font-size: 14px;
        resize: vertical;
        background-color: #ffffff;
        Text color: #000000;
    }
    .feedback-btn button {
        background-color: #009999;
        color: white;
        font-weight: bold;
        padding: 8px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    .feedback-btn button:hover {
        background-color: #007777;
    }
    </style>
    <div class="feedback-card">
        <h3> Share Your Feedback</h3>
        <p>If you have any suggestions or feedback, feel free to drop them here. I’d love to hear your thoughts!</p>
        <form action="https://formspree.io/f/xanbwkle" method="POST">
            <div class="feedback-box">
                <textarea name="feedback" placeholder="Your feedback here..." required></textarea>
            </div>
            <br/>
            <div class="feedback-btn">
                <button type="submit">Send</button>
            </div>
        </form>
    </div>
""", unsafe_allow_html=True)
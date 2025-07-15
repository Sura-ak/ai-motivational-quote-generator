import streamlit as st
import openai

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="AI-Powered Quote Generator",
    layout="wide"
)

# --- Custom CSS Styling (light + dark mode) ---
st.markdown("""
<style>
    /* --- Base Light Mode Styles --- */
    body, .stApp {
        background-color: #f8f8f8;
    }
    a[href^="#"],
    header [data-testid="stMarkdownContainer"] a,
    section [data-testid="stMarkdownContainer"] a,
    label[data-testid="stMarkdownContainer"] > div > a {
        display: none !important;
    }
    .block-container {
        padding-top: 2rem;
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
        0% { transform: scale(0.8); opacity: 0; }
        60% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(1); }
    }
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #003333;
        margin-bottom: 2rem;
    }
    .custom-box {
        background-color: #e0f7f7;
        padding: 25px;
        border-radius: 10px;
        margin: 10px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div,
    .feedback-box textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 5px;
        border: 1px solid #cccccc;
    }
    .stButton>button,
    .feedback-btn button {
        background-color: #009999 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover,
    .feedback-btn button:hover {
        background-color: #007777 !important;
    }
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
                height: 160px !important;
                padding: 14px;
                font-size: 14px;
                color: #000000;
                resize: vertical;
                background-color: #ffffff;
                border-radius: 5px;
                border: 1px solid #cccccc;
            }
    .feedback-box textarea::placeholder {
        color: #666666 !important;
    }
            .quote-text{
            color: #004d4d !important;
            font-size: 18px !important;
            line-height: 1.4;
            }

    /* --- Dark Mode Overrides --- */
    @media (prefers-color-scheme: dark) {
        body, .stApp {
            background-color: #121212 !important;
        }
            .quote-text{
                color: #ffffff !important;
            }
            .feedback-card {
                background-color: #1e1e1e !important;
            }
            .feedback-card h3 {
                color: #ffffff !important;
            }
            .feedback-card p {
                color: #dddddd !important;
            }
            .feedback-box textarea {
                background-color: #1e1e1e !important;
                color: #ffffff !important;
                border: 1px solid #444444 !important;
                height:160px !important;
                width: 100% !important;
            }

        /* Text, labels, markdown, headers, and alert messages */
        h1, h2, h3, h4, h5, h6,
        .subtitle, .animated-title, .custom-box,
        label, .stTextInput label, .stSelectbox label,
        .stMarkdown, .stSubheader,
        .stSuccess, .stWarning, .stError,
        .feedback-card h3, .feedback-card p {
            color: #dddddd !important;
        }

        /* Inputs, textareas, selectboxes */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div {
            background-color: #1e1e1e !important;
            color: #ffffff !important;
            border: 1px solid #444444 !important;}
        .feedback-box textarea {
            background-color: #1e1e1e !important;
            color: #ffffff !important;
            border: 1px solid #444444 !important;
            height:160px !important;
            width: 100% !important;
        }

        /* Placeholder text everywhere */
        ::placeholder,
        .stTextInput > div > div > input::placeholder,
        .stTextArea > div > div > textarea::placeholder,
        .feedback-box textarea::placeholder {
            color: #bbbbbb !important;
        }

        /* Buttons */
        .stButton>button,
        .feedback-btn button {
            background-color: #007777 !important;
            color: #ffffff !important;
        }
        .stButton>button:hover,
        .feedback-btn button:hover {
            background-color: #005f5f !important;
        }
    }
</style>
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
# Tone and Style options
tone_options = ["Empowering", "Reflective", "Motivational", "Other"]
style_options = ["Inspirational", "Humorous", "Narrative", "Other"]
with col2:
    st.subheader("STRUCTURED PROMPT")
    mood = st.text_input("Mood (e.g., resilience, creativity)", key="mood")
    audience = st.text_input("Audience (optional, e.g., students, founders)", key="audience")

    tone = st.selectbox("Tone", tone_options, key="tone")
    custom_tone = st.text_input("Enter custom tone", key="custom_tone") if tone == "Other" else ""

    style = st.selectbox("Style", style_options, key="style")
    custom_style = st.text_input("Enter custom style", key="custom_style") if style == "Other" else ""

    format_options = ["One-liner", "Poetic", "Short Paragraph", "Custom"]
    quote_format = st.selectbox("Quote Format", format_options, key="quote_format")
    custom_format = st.text_input("Describe custom format", key="custom_format") if quote_format == "Custom" else ""

    if st.button("Generate", key="generate_structured"):
        if not mood:
            st.warning("Please enter a mood.")
        else:
            with st.spinner("Generating quote..."):
                try:
                    final_tone = custom_tone if tone == "Other" else tone
                    final_style = custom_style if style == "Other" else style
                    final_format = custom_format if quote_format == "Custom" else quote_format

                    prompt = f"Write a {final_format.lower()} motivational quote in a {final_tone.lower()} and {final_style.lower()} tone about being {mood.lower()}."
                    if audience:
                        prompt += f" It should resonate with {audience.lower()}."
                    prompt += "\nKeep it concise and meaningful. Avoid clichés."

                    client = openai.OpenAI(api_key=api_key)
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are an expert motivational quote writer."},
                            {"role": "user", "content": prompt}
                        ]
                    )

                    quote = response.choices[0].message.content.strip()
                    st.success("Here’s your crafted quote:")
                    st.markdown(f'<p style="color:#004d4d; font-size:18px;">💬 {quote}</p>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Something went wrong while generating the quote: {e}")

# --- Feedback Section ---
st.markdown("""
<div class="feedback-card">
    <h3>Share Your Feedback</h3>
    <p>If you have any suggestions or feedback, feel free to drop them here. I’d love to hear your thoughts!</p>
    <form action="https://formspree.io/f/xanbwkle" method="POST">
        <div class="feedback-box">
            <textarea name="feedback" placeholder="Your feedback here..." required></textarea>
        </div><br/>
        <div class="feedback-btn">
            <button type="submit">Send</button>
        </div>
    </form>
</div>
""", unsafe_allow_html=True)

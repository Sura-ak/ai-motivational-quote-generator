import streamlit as st
import openai

# Set up Streamlit page
st.set_page_config(page_title="AI Motivational Quote Generator")
st.title("💭 AI Motivational Quote Generator")
st.write("Enter a theme or feeling and let AI inspire you!")


api_key = st.secrets["OPENAI_API_KEY"]

# Input: User's theme or mood
user_input = st.text_input("What's your mood or theme? (e.g., focus, fear, growth)")

if st.button("Generate Quote"):
    if not user_input:
        st.error("Please enter a theme or feeling.")
    else:
        try:
            # Initialize OpenAI client
            client = openai.OpenAI(api_key=api_key)

            response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.9,  # 🔥 Add randomness for variety
    messages=[
        {
            "role": "system",
            "content": "You are a wise and creative motivational quote generator. Each quote should be short, powerful, and emotionally inspiring."
        },
        {
            "role": "user",
            "content": f"Give me a motivational quote about {user_input}."
        }
    ]
)


            quote = response.choices[0].message.content
            st.success("Here's your quote:")
            st.write(f"💡 *{quote}*")
        except Exception as e:
            st.error(f"Error: {e}")

import streamlit as st
import openai

st.set_page_config(page_title="AI Motivational Quote Generator")
st.title("💭 AI Motivational Quote Generator")
st.write("Enter a theme or feeling and let AI inspire you!")

# Input: OpenAI API Key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Input: User theme
user_input = st.text_input("What's your mood or theme? (e.g., focus, fear, growth)")

if st.button("Generate Quote"):
    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not user_input:
        st.error("Please enter a theme or feeling.")
    else:
        try:
            # Connect to OpenAI using the new method
            client = openai.OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a motivational quote generator."},
                    {"role": "user", "content": f"Give me a motivational quote about {user_input}."}
                ]
            )

            quote = response.choices[0].message.content
            st.success("Here's your quote:")
            st.write(f"💡 *{quote}*")
        except Exception as e:
            st.error(f"Error: {e}")

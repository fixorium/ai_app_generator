import streamlit as st
from models.text_generator import TextGenerator

def main():
    st.title("AI App Generator")
    st.write("Create your own AI-powered text generator app!")

    # Get user input
    prompt = st.text_input("Enter a prompt:", "")

    # Initialize the text generator model
    model = TextGenerator()

    # Generate text based on the prompt
    if st.button("Generate Text"):
        generated_text = model.generate_text(prompt)
        st.write(generated_text)

if __name__ == "__main__":
    main()

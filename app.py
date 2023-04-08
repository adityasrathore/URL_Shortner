import streamlit as st
import pyshorteners

# Function to generate short URL
def generate_short_url(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)  # Shorten URL using TinyUrl with pyshorteners
    return short_url

# Streamlit app
def main():
    st.title("URL Shortener")
    long_url = st.text_input("Enter the long URL:")
    if st.button("Generate Short URL"):
        if long_url:
            short_url = generate_short_url(long_url)
            st.success(f"Short URL: {short_url}")
        else:
            st.warning("Please enter a long URL.")

if __name__ == "__main__":
    main()
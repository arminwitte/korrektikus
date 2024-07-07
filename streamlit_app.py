# streamlit_app.py

import streamlit as st
import requests

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

def run_gemini_api():
  """Simulates a Gemini API call using requests (for demo purposes only).

  **Important:** Due to security constraints, Streamlit apps deployed to production
  cannot directly make external API calls. This function simulates the call
  for demonstration purposes only.

  Args:
      text: The user-provided text to send to the simulated Gemini API.

  Returns:
      A string containing a simulated Gemini API response.
  """
  text = st.session_state.input
  # Replace with your actual Gemini API endpoint and authorization
  url = "https://your-gemini-api-endpoint/path/to/resource"
  # headers = {"Authorization": f"Bearer {st.secrets('API_KEY')}"} # Replace with your API key

  # Simulate API request (cannot directly call in Streamlit)
  # response = requests.post(url, headers=headers, json={"text": text})
  st.session_state["output"] = text



if check_password():
    st.session_state["output"] = "Here comes the *output*"
    st.header("Korrektikus")
    col1, col2 = st.columns(2)
    col1.text_area("Enter Text Here", height=250, key="input")
    st.button("correct", on_click=run_gemini_api)
    col2.markdown(st.session_state["output"])


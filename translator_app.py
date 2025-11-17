
import streamlit as st
import requests

# ------------------------------
# Azure Translator credentials
# ------------------------------
subscription_key = "M4Ay1YQqVN7EJtvMYQ4raak3WIhilvb9BryUUMGXqpriyWCFDf1aJQQJ99BKAC3pKaRXJ3w3AAAbACOGfLV0"
endpoint = "https://api.cognitive.microsofttranslator.com/"  # e.g., https://YOUR_RESOURCE_NAME.cognitiveservices.azure.com/translator/text/v3.0/translate
location = "eastasia"  # e.g., "eastus"

# ------------------------------
# Supported languages
# ------------------------------
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh-Hans",
    "Japanese": "ja",
    "Korean": "ko"
}

# ------------------------------
# Translate function
# ------------------------------
def translate_text(text, from_lang, to_lang):
    url = endpoint + "/translate?api-version=3.0"
    params = f"&from={from_lang}&to={to_lang}"
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json'
    }
    body = [{'text': text}]
    response = requests.post(url + params, headers=headers, json=body)
    result = response.json()
    translated_text = result[0]['translations'][0]['text']
    return translated_text

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🌐 Azure Translator")

input_text = st.text_area("Enter text to translate:")

col1, col2 = st.columns(2)
with col1:
    input_lang = st.selectbox("Input Language", list(languages.keys()))
with col2:
    output_lang = st.selectbox("Output Language", list(languages.keys()))

if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        translated = translate_text(
            input_text,
            from_lang=languages[input_lang],
            to_lang=languages[output_lang]
        )
        st.success("Translated Text:")
        st.write(translated)

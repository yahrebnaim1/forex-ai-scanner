
import streamlit as st
import openai
from PIL import Image
import base64

st.set_page_config(page_title="Forex AI Scanner", layout="centered")

st.markdown(
    "<h2 style='text-align: center; color: white;'>📈 Forex AI Scanner</h2>",
    unsafe_allow_html=True,
)

st.markdown("Sube tus 4 capturas (1D, 1H, 15M, 5M) del mismo par de Forex para recibir un análisis profesional basado en IA.")

api_key = st.text_input("🔑 Ingresa tu OpenAI API Key", type="password")
uploaded_files = st.file_uploader("📤 Sube las 4 imágenes (1D, 1H, 15M, 5M)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

def image_to_base64(image):
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

if st.button("🔍 Analizar"):
    if not api_key:
        st.error("Por favor, ingresa tu clave de API.")
    elif len(uploaded_files) != 4:
        st.error("Debes subir exactamente 4 imágenes.")
    else:
        openai.api_key = api_key
        images = [Image.open(f) for f in uploaded_files]

        with st.spinner("Analizando con IA..."):
            base_prompt = open("prompt_template.txt", "r").read()
            image_messages = [{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_to_base64(img)}"}} for img in images]

            response = openai.ChatCompletion.create(
                model="gpt-4-vision-preview",
                messages=[
                    {"role": "system", "content": base_prompt},
                    {"role": "user", "content": image_messages},
                ],
                max_tokens=1000
            )
            st.success("✅ Análisis completado")
            st.markdown(f"### Resultado de la IA:

{response.choices[0].message['content']}")

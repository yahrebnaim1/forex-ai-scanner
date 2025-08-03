
# Forex AI Scanner - Versión automática con clave API en entorno

1. Crea un Web Service en https://render.com
2. En Environment Variables, agrega:
   - NAME: OPENAI_API_KEY
   - VALUE: tu clave API de OpenAI
3. Build Command: pip install -r requirements.txt
4. Start Command: streamlit run app.py --server.port=10000 --server.address=0.0.0.0

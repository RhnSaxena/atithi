cd ./chatbot && ./load_kb.sh && cd ..
python -m chatbot build
export TWILIO_AUTH_TOKEN=5ddce2ecc4d80adcd103bd742bcac3d1
export TWILIO_ACCOUNT_SID=ACee88cc6b6cf96910936801fa3726ccb5
python whatsapp_bot_server.py
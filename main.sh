cd ./chatbot && ./load_kb.sh && cd ..
python -m chatbot build
export TWILIO_AUTH_TOKEN="AUTH TOKEN"
export TWILIO_ACCOUNT_SID="ACCOUNT SID"
python whatsapp_bot_server.py

cd ./chatbot && ./load_kb.sh && cd ..
python -m chatbot build
export TWILIO_AUTH_TOKEN=36418b6fe7615bd068ad13f614bdc19d
export TWILIO_ACCOUNT_SID=ACc47f3cc342412b7097ad6f6c6fe19398
python whatsapp_bot_server.py
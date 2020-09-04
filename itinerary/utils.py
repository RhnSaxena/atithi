import pyrebase
from twilio.rest import Client
from config import firebase_config, twilio_config

def get_iternary_info(id):
    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()
    res = db.child("user").child(id).child('itenary').get()
    return res.val()

def send_to_whatsapp(url,id,image_url):
    if(image_url is None):
        image_url="https://rohansaxena.in/images/logo.png"
    client = Client(twilio_config["account_sid"],twilio_config["auth_token"])
    try:
        client.messages.create(
            media_url=image_url,
            body="Please find the iternary.\n\n {url}".format(url=url),
            from_="whatsapp:+14155238886",
            to="whatsapp:+"+id
        )
        return {
            "success":True,
            "message":"Message sent successfully."
        }
    except Exception as e:
        return {
            "success":False,
            "message":"Error while sending message. {error}".format(error=str(e))
        }
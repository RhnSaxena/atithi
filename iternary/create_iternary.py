import uuid
import cloudinary
import cloudinary.uploader
import cloudinary.api
from datetime import date
from twilio.rest import Client
from utils import create_pdf,create_image, get_iternary_info, create_docx
from config import cloudinary_config, twilio_config


def create_iternary(id):

    data = get_iternary_info(id)
    data["id"]=id
    data["date"]=date.today()
    file_name="img_{}".format(str(uuid.uuid4())) 
    create_docx(data,file_name)
    # create_pdf(data,file_name)
    # create_image(file_name)
    # url=upload_to_cloudinary(file_name)
    # send_to_whatsapp(url,id)
    # return url

    
def upload_to_cloudinary(file_name):
    cloudinary.config(
        cloud_name = cloudinary_config["cloud_name"], 
        api_key =cloudinary_config["api_key"], 
        api_secret = cloudinary_config["api_secret"] 
    )
    stat=cloudinary.uploader.upload("{file}.{extention}".format(file=file_name,extention="jpeg"),  
    public_id = file_name,
    pages = True,
    overwrite = True, 
    resource_type = "image")
    return stat['secure_url']

def send_to_whatsapp(image_url,id):
    client = Client(twilio_config["account_sid"],twilio_config["auth_token"])
    client.messages.create(
        media_url=image_url,
        body="Please find the iternary.",
        from_="whatsapp:+14155238886",
        to="whatsapp:+"+id
    )

print(create_iternary(id="918527129869"))

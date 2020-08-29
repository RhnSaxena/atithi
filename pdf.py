from fpdf import FPDF 
import cloudinary
import cloudinary.uploader
import cloudinary.api
file_name="itenary.pdf"
import pyrebase
import time
from datetime import date

config = {
  "apiKey": "AIzaSyBiv6ZNCNcoHDiOkAhq9vHKiG0AqE2VjFY",
  "authDomain": "atithi-sih-2020.firebaseapp.com",
  "databaseURL": "https://atithi-sih-2020.firebaseio.com/",
  "storageBucket": "atithi-sih-2020.appspot.com"
}

config = config
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def function_for_image_to_cloud():

    res = db.child("user").child("918527129869").child('itenary').get()
    message = res.val()
    pdf = FPDF() 
    pdf.add_page() 
    pdf.set_font("Arial", size = 15) 
    string_gaps="\n\n"
    # USe Message string here
    pdf.cell(200, 10, txt = "Your Itenary",  
            ln = 1, align = 'C') 
    
    # add another cell 
    for key in message.keys():
        pdf.cell(200, 10, txt = str(key),  
            ln = 2, align = 'C') 
        for value in message[key].keys():
            pdf.cell(70, 10, txt = "{message_string}:{message_cost} ".format(message_string=value,message_cost=message[key][value]),ln = 3, align = 'C') 
            
        pdf.cell(200, 10, txt = string_gaps, ln = 2, align = 'C') 
    pdf.output(file_name)    
    from pdf2image import convert_from_path
    pages = convert_from_path(file_name, 500)
    for page in pages:
        page.save('out.jpg', 'JPEG')
    cloudinary.config( 
    cloud_name = "dhycsbaoz", 
    api_key = "275326527586643", 
    api_secret = "ZS22T8oxHfvFJagdHjTu67vDLjU" 
    )
    stat=cloudinary.uploader.upload("out.jpg", 
    #   folder = "pdfs/", 
    public_id = "id_1",
    pages = True,
    overwrite = True, 
    notification_url = "https://mysite.example.com/notify_endpoint", 
    resource_type = "image")
    return stat['secure_url']

print(function_for_image_to_cloud())
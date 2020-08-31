import pyrebase
import time
from fpdf import FPDF 
from pdf2image import convert_from_path
from config import firebase_config
from docxtpl import DocxTemplate



def create_docx(context,file_name):
    doc = DocxTemplate("template.docx")
    doc.render(context)
    doc.save(file_name+".docx")

def get_iternary_info(id):
    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()
    res = db.child("user").child(id).child('itenary').get()
    return res.val()

def create_pdf(message,file_name):
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
   
    pdf.output("{file}.{extention}".format(file=file_name,extention="pdf"))


def create_image(file_name):
    pages = convert_from_path("{file}.{extention}".format(file=file_name,extention="pdf"), 500)
    for page in pages:
        page.save("{file}.{extention}".format(file=file_name,extention="jpeg"), 'JPEG')
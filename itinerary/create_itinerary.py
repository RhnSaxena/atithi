import uuid
import os
from datetime import date
from utils import get_iternary_info, send_to_whatsapp
from templating import create_pdf,create_image, create_docx 
from cloud import upload_to_S3, upload_to_cloudinary

def create_iternary(id):

    data = get_iternary_info(id)
    data["id"]=id
    data["date"]=date.today()
    file_name="iternary_{}".format(str(uuid.uuid4())) 
    create_docx(data,"{file}.{extention}".format(file=file_name,extention="docx"))
    # create_pdf(data,"{file}.{extention}".format(file=file_name,extention="pdf"))
    # create_image(file_name)
    response=upload_to_S3(file_name, "docx")
    # response=upload_to_cloudinary(file_name, ".jpeg")
    os.remove("{file}.{extention}".format(file=file_name,extention="docx"))
    if(response["success"] is True):
        return send_to_whatsapp(url=response["message"],id=id,image_url=None)
    else: 
        return response["message"]

    


print(create_iternary(id="918527129869"))

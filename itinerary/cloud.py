import boto3
import cloudinary
import cloudinary.uploader
import cloudinary.api
from config import aws_config, aws_bucket, cloudinary_config


def upload_to_S3(file_name,extention):

    s3 = boto3.client('s3', **aws_config)
    bucket=aws_bucket["bucket_name"]
    
    try: 
        res = s3.upload_file(
            "{file}.{extention}".format(file=file_name,extention=extention), 
            bucket,  
            "{file}.{extention}".format(file=file_name,extention=extention), 
            ExtraArgs={'ACL': 'public-read'}
        )
        return {
                "success":True,
                "message":"https://{bucket}.s3.amazonaws.com/{file_name}.{extention}".format(
                    bucket=bucket,
                    file_name=file_name,
                    extention=extention
                )
        }
    except Exception as e:
        return {
                "success": False,
                "message": "Error while uploading to aws.\n{error}".format(error=str(e))
        }


def upload_to_cloudinary(file_name,extention):
    cloudinary.config(
        cloud_name = cloudinary_config["cloud_name"], 
        api_key =cloudinary_config["api_key"], 
        api_secret = cloudinary_config["api_secret"] 
    )
    try:
        response=cloudinary.uploader.upload(
            "{file}.{extention}".format(file=file_name,extention=extention),  
            public_id = file_name,
            pages = True,
            overwrite = True, 
            resource_type = "image"
        )
    
        return {
            "success":True,
            "message":response['secure_url']
        }

    except Exception as e:
        return {
                "success": False,
                "message":"Error while uploading to cloudinary.\n{error}".format(error=str(e))
        }

from twilio.rest import Client
import time
class remainderHelper:
	def __init__(self, f):
		self.firebase = f
		
	def start(self, data):
		
		for d in data:
			if(int(round(time.time() * 1000))) > d["time"]:
				self.sendMessage(d)
				self.firebase.removeReminder(d["created_at"])
			time.sleep(5)


	def sendMessage(self, v):
		client = Client()
		client.messages.create(media_url=['https://image.shutterstock.com/image-vector/reminder-red-square-sticker-isolated-260nw-274255889.jpg'],
								body=v["message"],
								from_="whatsapp:+14155238886",
								to="whatsapp:+"+str(v["to"]))
		print("Sending to", v["to"])

import os

class Config:
    API_ID = int(os.getenv("API_ID","23080322"))
    API_HASH = os.getenv("API_HASH", "b3611c291bf82d917637d61e4a136535")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6931048916:AAEiwn5cej-PVBw95cqsGskW-BEGx95o4jY")

import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    # Cental configration class
    # Feteches secrects and configration from Environment variables

    BASE_URL_UI = os.getenv("BASE_URL", "https://saurcedemo.com")
    BASE_URL_API = os.getenv("BASE_URL_API", "https://reqres.in/api")

    #browser cnfig
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    TIMEOUT = int(os.getenv("TIMEOUT", 30000))

    #credentials
    USERNAME = os.getenv("USERNAME", "standard_user")
    PASSWORD = os.getenv("PASSWORD", "secret_sauce")
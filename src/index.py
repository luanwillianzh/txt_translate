import requests
from fastapi import FastAPI
from googletrans import Translator

t = Translator()
app = FastAPI()

@app.get("/")
def index(url: str=""):
  if url == "":
    return "Hello World!"
  else:
    txtify = requests.get(f"https://txtify.luanwillianzh04.workers.dev/{url}").text
    trad = [ i.text for i in t.translate(txtify.split("\n\n"), dest="pt") ]
    return "\n\n".join(trad)

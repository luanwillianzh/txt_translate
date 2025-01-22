import requests
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from googletrans import Translator
from random import choice


app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def index(url: str=""):
  t = Translator()
  ua = requests.get("https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt").text.split("\n")
  if url == "":
    return "Hello World!"
  else:
    txtify = requests.get(f"https://txtify.luanwillianzh04.workers.dev/{url}", headers={"User-Agent": choice(ua)}).text
    trad = [ i.text for i in t.translate(txtify.split("\n\n"), dest="pt") ]
    return "\n\n".join(trad)

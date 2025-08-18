import requests
r= requests.get("https://www.facebook.com/")
with open("data.txt","w", encoding="utf-8") as f:
    f.write(r.text)
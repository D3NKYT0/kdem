import json

with open("data/default.json", encoding="utf-8") as default:
    default = json.load(default)

with open("data/login.json", encoding="utf-8") as login:
    login = json.load(login)

with open("data/announce.json", encoding="utf-8") as announce:
    announce = json.load(announce)

data = {
    "default": default,
    "login": login,
    "announce": announce
}
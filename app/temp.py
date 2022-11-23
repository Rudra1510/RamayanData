import json

with open("app/data/ramayan2.json","r") as f:
    d = json.load(f)

with open("app/data/ramayan.json","w+") as f:
    json.dump(d,f)


# a = "तपःस्वाध्यायनिरतं तपस्वी वाग्विदां वरम् |\nनारदं परिपप्रच्छ वाल्मीकिर्मुनिपुङ्गवम् || १-१-१"


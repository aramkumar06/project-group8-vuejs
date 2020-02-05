import json

# python manage.py dumpdata dataServer.video --indent 1 > video.json

with open('video.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('video2.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent='\t', ensure_ascii=False)
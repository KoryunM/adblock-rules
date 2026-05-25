import json
import urllib.request

print("Downloading EasyList rules...")
url = "https://easylist.to/easylist/easylist.txt"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
lines = response.read().decode('utf-8').split('\n')

rules = []
for line in lines:
    # Ищем стандартные правила блокировки доменов (например: ||ads.google.com^)
    if line.startswith('||') and '^' in line:
        domain = line[2:line.find('^')]
        # Исключаем сложные регулярные выражения для стабильности Safari
        if '*' not in domain and '/' not in domain:
            rules.append({
                "trigger": { "url-filter": ".*" + domain.replace('.', '\\\\.') + ".*" },
                "action": { "type": "block" }
            })

print(f"Successfully converted {len(rules)} rules to Safari format!")

with open('blockerList.json', 'w') as f:
    json.dump(rules, f, separators=(',', ':'))

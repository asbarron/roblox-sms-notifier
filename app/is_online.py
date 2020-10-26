import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

# Bool check if player is online
def is_online(playerId):
    headers = {'User-Agent': 'Python'}
    url = f"https://api.roblox.com/users/{playerId}/onlinestatus/"
    req = urllib.request.Request(url, data=None, headers=headers, origin_req_host=None)
    try:
        with urllib.request.urlopen(req) as f:
            content = f.read()
            data = json.loads(content.decode('utf8'))
            if data["IsOnline"] == True:
                return True
            else:
                return False
    except:
        print("Invalid Player")⏎    

from is_online import is_online
from send_sms import send_sms
import time
# Players to get notified on
playerids = [""]

online = [""]
offline = [""]

print("---Initial Check ---")
for playerid in playerids:
    if is_online(playerid):
        print(f"Player {playerid} is online")
        send_sms(playerid)
        online.append(playerid)
    else:
        print(f"Player {playerid} is offline")
        offline.append(playerid)
print("--- Initial Check done ---")

while True:
    for playerid in playerids:
        if playerid in offline:
            if is_online(playerid):
                print(f" Player {playerid} was offline and is now online")
                send_sms(playerid)
                offline.remove(playerid)
                online.append(playerid)
            else:
                print(f"Player {playerid} was offline and is still offline")
                pass
        else:
            if is_online(playerid) == False:
                print(f"Player {playerid} was online and is now offline")
                online.remove(playerid)
                offline.append(playerid)
            else:
                print(f"Player {playerid} was online and is still online")
                pass

    time.sleep(5)
    print("--- Next round ---")

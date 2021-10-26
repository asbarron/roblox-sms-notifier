from is_online import is_online
from send_sms import send_sms
from time import sleep

# Players to get notified on
playerIds = [""]
lastStatus = {}

while True:
    for playerId in playerIds:
        isOnline = is_online(playerId)
        if isOnline != lastStatus.get(playerId, False):
            status = "online" if isOnline else "offline"
            print(f"Player {playerId} is {status}")
            send_sms(playerId, status)
        lastStatus[playerId] = isOnline
    sleep(5)

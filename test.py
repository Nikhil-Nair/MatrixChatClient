import requests, json
requests.packages.urllib3.disable_warnings()

def sendMessage(roomKeys,accessToken, message):
    d = {"msgtype":"m.text", "body": message}
    for rKey in roomKeys:
        url = "https://matrix.org/_matrix/client/r0/rooms/%21{0}/send/m.room.message?access_token={1}".format(rKey, access_key)
        req = requests.post(url, data = json.dumps(d))
        print(req.content,req.status_code)
    user_data_url = "https://matrix.org/_matrix/client/r0/sync?access_token={}".format(access_key)
    # user_data_req = requests.get(user_data_url)
    # print(user_data_req.json()["rooms"]["join"].keys())

message = input("Enter the message")
room_keys = ["uxDBdZPYtvacXYNYUJ:matrix.org", "fPCYiApwrypdAIUFFJ:matrix.org", "AbBCCRYxHlyiiJydmA:matrix.org"]
key_file = open('taskData.txt', 'r')
access_key = key_file.read().rstrip()
key_file.close()
sendMessage(room_keys, access_key, message)

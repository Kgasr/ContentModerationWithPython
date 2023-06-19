import json
import requests

def receive(apiurl):
    url = apiurl
    resposne = requests.get(url)
    print(resposne.json())
    filtered_response = [item for item in resposne.json() if item['msg_moderate_status'] == False]
    unread_msgs = json.dumps(filtered_response)
    print(unread_msgs)
    unread_msgs_list = []
    #for obj in unread_msgs:
        #print(obj)
        #new_dict={obj['msg_id']:obj['msg_desc']}
        #unread_msgs_list.append(new_dict)
    return unread_msgs

receive('http://127.0.0.1:8080/djangoapi/apisample/')
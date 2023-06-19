import os
import json

def receive(filepath):
    lines = []
    with open(filepath, "r") as file:
        lines = []
        for line in file:
            lines.append(line.strip())
    json_list = [{key: value} for key, value in [elem.split(': ') for elem in lines]]
    json_str = json.dumps(json_list)
    print(json_str)
    return json_str

#receive("../TestData/data.json")
receive("TestData/messages.txt")
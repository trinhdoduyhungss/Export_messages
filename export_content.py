import os
import json
friends = os.listdir('./data/messages_1/inbox')
full_data_conversations = ""
def parse_obj(obj):
    for key in obj:
        if isinstance(obj[key], str):
            obj[key] = obj[key].encode('latin_1').decode('utf-8')
        elif isinstance(obj[key], list):
            obj[key] = list(map(lambda x: x if type(x) != str else x.encode('latin_1').decode('utf-8'), obj[key]))
        pass
    return obj
for f in friends:
    data = open('./data/messages_1/inbox/'+f+'/message_1.json','r', encoding='utf-8')
    data = json.loads(data.read(), object_hook=parse_obj)
    friend = data["participants"][0]["name"]
    user = data["participants"][1]["name"]
    messages_arr = data["messages"]
    size_messages_arr = len(messages_arr)
    for i in range(1,size_messages_arr):
        data_item = messages_arr[i*-1]
        try:
            if  'https' not in data_item["content"]:
                full_data_conversations += data_item["content"].strip() +"\n"
        except:
            pass

if len(full_data_conversations) > 0:
    save_file = open('export_data_conversations.txt', 'w', encoding='utf-8')
    save_file.write(full_data_conversations)
    save_file.close()

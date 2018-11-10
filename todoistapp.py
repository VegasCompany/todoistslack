import requests
import json
import uuid
import config

headers = {
    "Content-Type": "application/json",
    "X-Request-Id": str(uuid.uuid4()),
    'Authorization':'Bearer ' + config.CONFIG['apikey']
}



def createtask(content, due_string):
    data = json.dumps({
            "content": content,
            "due_string": due_string,
            "due_lang": "en",
            "priority": 4
        })
    urltask = 'https://beta.todoist.com/API/v8/tasks'
    mypost = requests.post(urltask, data=data,headers=headers).json()
    print(mypost)

createtask("test", "tomorrow at 14")
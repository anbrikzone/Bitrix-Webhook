import requests
import json
from dotenv import load_dotenv

load_dotenv()

res = requests.get('https://b24-s88plv.bitrix24.kz/rest/1/2d3gkim8xg4mu97u/crm.contact.list/')
response = json.loads(res.content)
# print(response)
print(json.dumps(response, indent=2))
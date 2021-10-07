import requests
import json
from pprint import pprint
# Задаем имя пользователя github
username = "tyrrannt"
token = ""
# формируем url для запроса
github_data_url = f"https://api.github.com/users/{username}"
# запрашиваем данные в json
github_user_data = requests.get(github_data_url).json()
result_dict = dict()
result_dict['author'] = github_user_data['name']
result_dict['repository'] = []
github_repository_data = requests.get(github_user_data['repos_url']).json()

for item in github_repository_data:
    result_dict['repository'].append(item['html_url'])

with open(f'{username}.json', 'w') as outfile:
    json.dump(result_dict, outfile)

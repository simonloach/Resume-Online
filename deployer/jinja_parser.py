import requests
import os

from jinja2 import Template

def deployer():
    token = open('token','r').read().replace('\n','')
    response = requests.get(
        'https://api.github.com/user/repos', 
        headers = {
            'Authorization':f'Bearer {token}',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 YaBrowser/16.3.0.7146 Yowser/2.5 Safari/537.36',
            'Accept':'application/vnd.github.v3+json'
            }
        )

    repos = list()
    print('yeet')
    for el in response.json():
        if not el.get('private'):
            repo = {
                'description': el.get('description', ""),
                'name': el.get('name', ""),
                'url': el.get('html_url', ""),
                'topics': el.get('topics', []),
            }
            if repo['description'] and repo['topics'] and len(repo['description']) > 30 and len(repo['topics']) > 0:
                if len(repo['description']) > 150:
                    repo['description']=repo['description'][:151] + "..."
                repos.append(repo)
    with open('index.jinja') as f:
        tmpl = Template(f.read())

    with open('/html/index.html','w') as f:
        f.write(
            tmpl.render(
                repos = repos
                )
            )
    return repos

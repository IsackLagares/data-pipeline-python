import requests
import base64

class RepoCreation:

    def __init__(self, username):
        self.username = username
        self.access_token = ''
        self.api_url = 'https://api.github.com'
        self.headers = {'Authorization': 'Bearer ' + self.access_token, 'X-GitHub-Api-Version': '2022-11-28'}

    def create_repos(self, repo_name):
        data= {
            'name': repo_name,
            'description': 'Linguagens Utilizadas nos Repositórios',
            'private': False
        }

        reposnse = requests.post(f'{self.api_url}/user/repos',
                                    json=data, headers=self.headers)
            
        print(f'Status Criação do Repositório: {reposnse.status_code}')

    def add_file(self, repo_name, file_name, path_name):
        # Encoding
        with open(path_name, 'rb') as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)

        # Upload
        url = f'{self.api_url}/repos/{self.username}/{repo_name}/contents/{file_name}'
        data = {
            'message': f'new file',
            'content': encoded_content.decode('utf-8')
        }

        reponse = requests.put(url, json=data, headers=self.headers)
        print(f'Status do Commit: {reponse.status_code}')
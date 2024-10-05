import requests
import pandas as pd
from math import ceil

class RepoManipulation:
    
    def __init__(self, owner):
        self.owner = owner
        self.access_token = ''
        self.api_url = 'https://api.github.com'
        self.headers = {'Authorization': 'Bearer ' + self.access_token, 'X-GitHub-Api-Version': '2022-11-28'}

    def list_repos(self):
        repos_list = []
        response = requests.get(f'https://api.github.com/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30)

        for page_num in range(1, num_pages+1):
            try:
                url_page = f'{self.api_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url_page, self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        return repos_list

    def list_repos_name(self, repos_list):
        repos_name = []

        for page in repos_list:
            for repo in page:
                repos_name.append(repo['name'])
        return repos_name
    
    def list_repos_language(self, repos_list):
        repos_language = []

        for page in repos_list:
            for repo in page:
                repos_language.append(repo['language']) 
        return repos_language
    
    def create_dataframe(self):
        repository =  self.list_repos()
        names = self.list_repos_name(repository)
        languages = self.list_repos_language(repository)

        data_frame = pd.DataFrame()
        data_frame['repository_names'] = names
        data_frame['repository_languages'] = languages

        data_frame.to_csv(f'pipeline_dados_api/data_frame/languages_{self.owner}.csv')

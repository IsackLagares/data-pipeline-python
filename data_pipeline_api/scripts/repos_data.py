from repos_manipulation import RepoManipulation
from repos_creation import RepoCreation

# Languages Amazon
amazon_repos = RepoManipulation('amzn')
language_amazon = amazon_repos.create_dataframe()

# Languages Netflix
netflix_repos = RepoManipulation('netflix')
language_netflix = netflix_repos.create_dataframe()

# Languages Spotify
spotify_repos = RepoManipulation('spotify')
language_spotify = spotify_repos.create_dataframe()

# Username GitHub
github_name = RepoCreation('IsackLagares')

# Repository Name
repository_name = 'csv-repository-languages'
github_name.create_repos(repository_name)

# Commit 
github_name.add_file(repository_name, 'languages_amzn.csv', 'pipeline_dados_api/data_frame/languages_amzn.csv')
github_name.add_file(repository_name, 'languages_netflix.csv', 'pipeline_dados_api/data_frame/languages_netflix.csv')
github_name.add_file(repository_name, 'languages_spotify.csv', 'pipeline_dados_api/data_frame/languages_spotify.csv')


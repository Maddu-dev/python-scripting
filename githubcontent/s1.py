from github import Github
#provide token
token = ""
g = Github(token)

user = g.get_user()
print(user.login)
print(user.public_repos)
print(user.followers)

for repo in user.get_repos():
    print(repo)
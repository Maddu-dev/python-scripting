import subprocess

repo_url = "https://github.com/Maddu-dev/gitops-eks-observability-hub.git"

clone_url = "/workspaces/python-scripting/githubcontent/repo"

subprocess.run(["git", "clone", repo_url, clone_url])


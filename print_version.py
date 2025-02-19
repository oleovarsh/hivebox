import git 
repo = git.Repo("C:\\Users\\varsh\\Documents\\hivebox")
tags = repo.git.ls_remote("--tags", "origin")

print(tags.split('\n')[-1].split('/')[-1])
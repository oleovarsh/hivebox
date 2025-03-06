import git 
repo = git.Repo.clone_from('https://github.com/oleovarsh/hivebox.git','/tmp/hivebox')
tags = repo.git.ls_remote("--tags", "origin")

print(tags.split('\n')[-1].split('/')[-1])
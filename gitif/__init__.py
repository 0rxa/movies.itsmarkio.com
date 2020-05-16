from git import Repo
import os

basedir = os.environ.get("PWD")
basedir = basedir + "/../infrastructure/"

class Git():
    repos = [ 'web', 'relay' ]
    def __init__(self, repo_name):
        self.repo = Repo(basedir + repo_name)


    def pull(self, branch='master'):
        self.repo.remotes.origin.pull(branch)

        

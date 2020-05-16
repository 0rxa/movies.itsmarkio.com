from git import Repo
from config import Config

import os
import hashlib
import hmac
import base64

class Git():
    basedir = Config.basedir
    key = Config.key

    def __init__(self, repo_name):
        self.repo = Repo(self.basedir + repo_name)

    def pull(self, branch='master'):
        self.repo.remotes.origin.pull(branch)

    def verify(self, signature, payload):
        result = str(hmac.new(bytes(self.key, 'utf-8'), payload, hashlib.sha1).hexdigest())
        print(result)
        return hmac.compare(signature, result)

from model.GitHubUser import GitHubUser


class GitHubPullBranch:
    label = str()
    ref = str()
    sha = str()
    user = GitHubUser
    repo = object()

    def getLabel(self):
        return self.label

    def getRef(self):
        return self.ref

    def getSha(self):
        return self.sha

    def getUser(self):
        return self.user

    def getRepo(self):
        return self.repo

    def __init__(self):
        return self

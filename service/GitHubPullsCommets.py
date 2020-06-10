import requests
from requests.auth import HTTPBasicAuth
from model.GitHubPullsCommets import GitHubPullsCommets
from model.GithubAuth import GithubAuth

class GitHubPullsCommetsServis:
    pullNumber = []
    url = GithubAuth.url
    username = GithubAuth.username
    password = GithubAuth.password
    gitHubCommets = GitHubPullsCommets
    gitHubCommetsArray = []
    def __init__(self, pullNumber):
        self.pullNumber = self.pullNumber
        self.url = self.url
        self.username = self.username
        self.password = self.password
        self.gitHubCommets = self.gitHubCommets

        return self


    def listCommentsOnPullRequest(self, owner, repo, pullNumber = []):
        # /repos/$owner/$repo/pulls/$number/comments
        for i in pullNumber:
            pullComment = self.url + "/repos/" + owner + "/" + repo + "/pulls/ " + str(i) + "/comments"
            if requests.get(pullComment, auth=HTTPBasicAuth(self.username, self.password)).status_code == 200:
                gitHubCommets = requests.get(pullComment, auth=HTTPBasicAuth(self.username, self.password)).json()
                self.gitHubCommetsArray.append(gitHubCommets)
            else:
                print("Giriş Yapılamadı.")
                return 0
        return self.gitHubCommetsArray







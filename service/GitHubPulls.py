from requests.auth import HTTPBasicAuth
from model.GithubAuth import GithubAuth
from model.GitHubPull import GitHubPull
import requests
import json
class GitHubPulls:
    url = GithubAuth.url
    username = GithubAuth.username
    password = GithubAuth.password
    def _repr(self):
        return "<GitHubPulls [{0}]>".format(self.path)

    def __init__(self):
        self.url = self.url
        self.username = self.username
        self.password = self.password
        return self

    def listPullLinkRequests(self, owner, repo, pagePer):
        pullGet = self.url + "/repos/" + owner + "/" + repo + "/pulls?page=" + str(pagePer)
        if requests.get(pullGet, auth=HTTPBasicAuth(self.username, self.password)).status_code == 200:
            link = requests.get(pullGet, auth=HTTPBasicAuth(self.username, self.password)).links
            print("Giriş yapıldı.")
            return link
        else:
            print("Giriş yapılamadı")
            return 0
    def projectControl(self,owner,repo):
        pullGet = self.url + "/repos/" + owner + "/" + repo
        if requests.get(pullGet, auth=HTTPBasicAuth(self.username, self.password)).status_code == 200:
            link = requests.get(pullGet, auth=HTTPBasicAuth(self.username, self.password)).links
            print("Proje Bulundu.")
            return 1
        else:
            print("Proje Bulunamadı.")
            return 0
    def listPullGetNumber(self, owner, repo, page, size):
        git = GitHubPull
        jsonVeri = []
        pullJsonNumber = []
        pullNumber = self.url + "/repos/" + owner + "/" + repo + "/pulls?page=" + str(page)
        if requests.get(pullNumber, auth=HTTPBasicAuth(self.username, self.password)).status_code == 200:
            if int(size) != 0:
                for i in range(1, int(size) + 1):
                    r = self.url + "/repos/" + owner + "/" + repo + "/pulls?page=" + str(i)
                    if requests.get(r, auth=HTTPBasicAuth(self.username, self.password)).status_code == 200:
                        git = requests.get(r, auth=HTTPBasicAuth(self.username, self.password)).json()
                        jsonVeri.append(git)
                    else:
                        return "Serviste Bir Hata Oluştu"
            else:
                r = self.url + "/repos/" + owner + "/" + repo + "/pulls"
                if requests.get(r, auth=HTTPBasicAuth(self.username, self.password)).status_code == 200:
                    git = requests.get(r, auth=HTTPBasicAuth(self.username, self.password)).json()
                    jsonVeri.append(git)
                else:
                    return "Serviste Bir Hata Oluştu"
            for i in jsonVeri:
                for k in i:
                    pullJsonNumber.append(k["number"])
            return pullJsonNumber
        else:
            print("Giriş yapılamadı")
            return 0

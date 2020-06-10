
class GitHubUser:
    login = str()
    id = str()
    avatar_url = str()
    gravatar_id = str()
    url = str()
    html_url = str()

    def getLogin(self):
        return self.login

    def getId(self):
        return self.id

    def getAvatarUrl(self):
        return self.avatar_url

    def getGravatarId(self):
        return self.gravatar_id

    def getUrl(self):
        return self.url

    def getHtmlUrl(self):
        return self.html_url

    def __init__(self):
        return self
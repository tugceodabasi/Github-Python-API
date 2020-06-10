from model.GitHubUser import GitHubUser

class GitHubFullUser :
    login = str()
    name = str()
    company = str()
    blog = str()
    location = str()
    email = str()
    hireable = bool()
    bio = str()
    public_repos = int()
    public_gists = int()
    followers = int()
    following = int()
    html_url = str()
    created_at = str()
    type = str()
    avatar_url = str()

    def getLogin(self):
        return self.login
    def getName(self):
        return self.name
    def getCompany(self):
        return self.company
    def getLocation(self):
        return self.location
    def getEmail(self):
        return self.email
    def getHireable(self):
        return self.hireable
    def getBio(self):
        return self.bio
    def getPublicRepos(self):
        return self.public_repos
    def getPublicGists(self):
        return self.public_gists
    def getFollowes(self):
        return self.followers
    def getFollowing(self):
        return self.following
    def getHtmlUrl(self):
        return self.html_url
    def getCreatedAt(self):
        return self.created_at
    def getType(self):
        return self.type
    def getAvatarUrl(self):
        return self.avatar_url
    def __init__(self):
        return self




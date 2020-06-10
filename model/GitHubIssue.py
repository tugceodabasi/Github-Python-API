class GitHubIssue:
    url = str()
    html_url = str()
    number = int()
    state = str()
    title = str()
    body = str()
    user = object()
    assignee = object()
    milestone = object()
    comments = int()
    closed_at = str()
    created_at = str()
    updated_at = str()
    pull_request = object()

    def getUrl(self):
        return self.url

    def getHtmlUrl(self):
        return self.html_url

    def getNumber(self):
        return self.number

    def getState(self):
        return self.state

    def getTitle(self):
        return self.title

    def getBody(self):
        return self.body

    def getUser(self):
        return self.user

    def getAssignee(self):
        return self.assignee

    def getMilestone(self):
        return self.milestone

    def getComments(self):
        return self.comments

    def getClosedAt(self):
        return self.closed_at

    def getCreatedAt(self):
        return self.created_at

    def getUpdatedAt(self):
        return self.updated_at

    def getPullRequest(self):
        return self.pull_request

    def __init__(self):
        return self

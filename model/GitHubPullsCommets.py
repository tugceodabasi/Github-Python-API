from model.GitHubUser import GitHubUser
from model.GitHubPullLinks import GitHubPullLinks


class GitHubPullsCommets:
    url = str
    id = str
    node_id = str
    pull_request_review_id = int
    diff_hunk = str
    path = str
    position = int
    original_position = int
    commit_id = str
    original_commit_id = str
    in_reply_to_id = int
    user = GitHubUser
    body = str
    created_at = str
    updated_at = str
    html_url = str
    pull_request_url = str
    author_association = str
    _links = GitHubPullLinks
    start_line = int
    original_start_line = int
    start_side = str
    line = int
    original_line = int
    side = str

    def getUrl(self):
        return self.url

    def getId(self):
        return self.id

    def getNodeId(self):
        return self.node_id

    def getPRequestReviewId(self):
        return self.pull_request_review_id

    def getDiffHunk(self):
        return self.diff_hunk

    def getPath(self):
        return self.path

    def getPosition(self):
        return self.position

    def getOrjPosition(self):
        return self.original_position

    def getCommitId(self):
        return self.commit_id

    def getOrjCommitId(self):
        return self.original_commit_id

    def getReplyId(self):
        return self.in_reply_to_id

    def getUser(self):
        return self.user

    def getBody(self):
        return self.body

    def getCreatedAt(self):
        return self.created_at

    def getUpdatedAt(self):
        return self.updated_at

    def getHtmlUrl(self):
        return self.html_url

    def getPullRequestUrl(self):
        return self.pull_request_url

    def getAuthorAssociation(self):
        return self.author_association

    def getLinks(self):
        return self._links

    def getStartLine(self):
        return self.start_line

    def getOrjStartLine(self):
        return self.original_start_line

    def getStartSide(self):
        return self.start_side

    def getLine(self):
        return self.line

    def getOrjLine(self):
        return self.original_line

    def getSide(self):
        return self.side

    def __init__(self):
        return self


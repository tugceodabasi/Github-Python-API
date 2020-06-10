
from __future__ import unicode_literals
class GitHubPull:
    id = int()
    url = str()
    html_url = str()
    diff_url = str()
    patch_url = str()
    issue_url = str()
    commits_url = str()
    review_comments_url = str()
    review_comment_url = str()
    comments_url = str()
    statuses_url = str()
    number = int()
    state = str()
    title = str()
    body = str()
    created_at = str()
    updated_at = str()
    closed_at = str()
    merged_at = str()
    user = object()
    _links = object()
    head = object()
    base = object()
    mergeable = bool()
    commets = object()

    def getCommets(self):
        return self.commets

    def getId(self):
        return self.id

    def getUrl(self):
        return self.url

    def getHtmlUrl(self):
        return self.html_url

    def getDiffUrl(self):
        return self.diff_url

    def getPatchUrl(self):
        return self.patch_url

    def getIssueUrl(self):
        return self.issue_url

    def getCommitsUrl(self):
        return self.commits_url

    def getReviewCommentsUrl(self):
        return self.review_comments_url

    def getReviewCommentUrl(self):
        return self.review_comment_url

    def getCommentsUrl(self):
        return self.comments_url

    def getStatusesUrl(self):
        return self.statuses_url

    def getNumber(self):
        return self.number

    def getState(self):
        return self.state

    def getTitle(self):
        return self.title

    def getBody(self):
        return self.body

    def getCreatedAt(self):
        return self.created_at

    def getUpdatedAt(self):
        return self.updated_at

    def getClosedAt(self):
        return self.closed_at

    def getMergedAt(self):
        return self.merged_at

    def getUser(self):
        return self.user

    def getLinks(self):
        return self._links

    def getHead(self):
        return self.head

    def getBase(self):
        return self.base

    def isMergeable(self):
        return self.merged_at

    def __init__(self):
        return self

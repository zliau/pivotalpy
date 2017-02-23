import json
from project import Project

class Story(Project):
    def __init__(self, pivotal):
        self.pivotal = pivotal
        self.stories_url = pivotal.base_url + 'projects/{}/stories/{}'

    # Get stories matching the query in @params
    def getAll(self, project_id, params=None):
        print "Getting all stories in " + str(project_id) + " with params: " + json.dumps(params)
        url = self.stories_url.format(project_id, '')
        r = self.pivotal.makeAPIRequest(url, 'GET', params=params)
        return r.json()

    # Create new story with @data
    def create(self, project_id, data):
        url = self.stories_url.format(project_id, '')
        r = self.pivotal.makeAPIRequest(url, 'POST', data=data)
        return r.json()

    # Get story specified by @story_id
    def get(self, project_id, story_id):
        url = self.project_url.format(project_id, story_id)
        r = self.pivotal.makeAPIRequest(url, 'GET')
        return r.json()

    # Update story specified by @story_id
    def update(self, project_id, story_id, data):
        url = self.project_url.format(project_id, story_id)
        r = self.pivotal.makeAPIRequest(url, 'PUT', data=data)
        return r.json()

    # Post comment on story specified by @story_id
    def postComment(self, project_id, story_id, data):
        url = self.project_url.format(project_id, story_id)
        r = self.pivotal.makeAPIRequest(url, 'POST', data=data)
        return r.json()

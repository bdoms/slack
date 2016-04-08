import json

try:
    from urllib import urlencode
    from urllib2 import HTTPError, Request, urlopen
except ImportError:
    from urllib.error import HTTPError
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen


# this is for working with an incoming web hook: https://api.slack.com/incoming-webhooks
class Slack(object):

    def __init__(self, url):
        self.url = url

    def postMessage(self, text, attachments=None):
        params = {'text': text}
        if attachments:
            params['attachments'] = attachments
        self.makeRequest(params)

    def makeRequest(self, params):
        payload = json.dumps(params)

        data = urlencode({"payload": payload}).encode('utf-8')

        request = Request(self.url)

        try:
            response = urlopen(request, data=data)
        except HTTPError as e:
            print(e)
            print(e.read())
            result = None
        else:
            result = response.read().decode('utf-8')

        return result

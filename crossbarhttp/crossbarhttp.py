import json
import urllib2


class ClientBaseException(Exception):
    """
    Catch all Exception for this class
    """
    pass


class ClientNoCalleeRegistered(ClientBaseException):
    """
    Exception thrown when no callee was registered
    """
    pass


class ClientBadUrl(ClientBaseException):
    """
    Exception thrown when the URL is invalid
    """
    pass


class ClientBadHost(ClientBaseException):
    """
    Exception thrown when the host name is invalid
    """
    pass


class Client(object):

    def __init__(self, url, verbose=False):
        """
        Creates a client to connect to the HTTP bridge services
        :param url: The URL to connect to to access the Crossbar
        :param verbose: True if you want debug messages printed
        :return: Nothing
        """
        assert url is not None

        self.url = url
        self.verbose = verbose

    def publish(self, topic, *args, **kwargs):
        """
        Publishes the request to the bridge service
        :param topic: The topic to publish to
        :param args: The arguments
        :param kwargs: The key/word arguments
        :return: The ID of the publish
        """
        assert topic is not None

        params = {
            "topic": topic,
            "args": args,
            "kwargs": kwargs
        }

        response = self.make_api_call("POST", self.url, json_params=params)
        return response["id"]

    def call(self, procedure, *args, **kwargs):
        """
        Calls a procedure from the bridge service
        :param topic: The topic to publish to
        :param args: The arguments
        :param kwargs: The key/word arguments
        :return: The response from calling the procedure
        """
        assert procedure is not None

        params = {
            "procedure": procedure,
            "args": args,
            "kwargs": kwargs
        }

        response = self.make_api_call("POST", self.url, json_params=params)
        if "args" in response and len(response["args"]) > 0:
            value = response["args"][0]

            if isinstance(value, (str, unicode)) and "no callee registered" in value:
                raise ClientNoCalleeRegistered(value)

            return value
        else:
            return None

    def make_api_call(self, method, url, json_params=None):

        if self.verbose is True:
            print "Making web request: "+url

        if json_params is not None:
            encoded_params = json.dumps(json_params)
            headers = {'Content-Type': 'application/json'}
        else:
            encoded_params = None
            headers = {}

        if encoded_params is not None and self.verbose is True:
            print "Params: "+encoded_params

        try:
            request = urllib2.Request(url, encoded_params, headers)
            request.get_method = lambda: method
            response = urllib2.urlopen(request).read()
            return json.loads(response)
        except urllib2.HTTPError, e:
            raise ClientBadUrl(str(e))
        except urllib2.URLError, e:
            raise ClientBadHost(str(e))

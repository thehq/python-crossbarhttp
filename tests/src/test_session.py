from autobahn.twisted.wamp import ApplicationSession
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep


class TestSession(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):

        def add_something(x, y, offset=0):
            print "Add was called"
            return x+y+offset

        self.register(add_something, "test.add")

        def subscribe_something(x, y, event=None, **kwargs):
            print "Publish was called with event %s" % event

        self.subscribe(subscribe_something, "test.publish")

        while True:
            yield sleep(1)

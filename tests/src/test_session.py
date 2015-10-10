from autobahn.twisted.wamp import ApplicationSession


class TestSession(ApplicationSession):

    def onJoin(self, details):

        def add_something(x, y, offset=0):
            print "Add was called"
            return x+y+offset

        self.register(add_something, "test.add")

        def throw_exception():
            print "Exception"
            raise Exception()

        self.register(throw_exception, "test.exception")

        def subscribe_something(x, y, event=None, **kwargs):
            print "Publish was called with event %s" % event

        self.subscribe(subscribe_something, "test.publish")


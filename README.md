#Crossbar HTTP

Module that provides methods for accessing Crossbar.io HTTP Bridge Services

Build Status: [![Circle CI](https://circleci.com/gh/thehq/python-crossbarhttp/tree/master.svg?style=svg)](https://circleci.com/gh/thehq/python-crossbarhttp/tree/master)

#Call
To call a Crossbar HTTP bridge, do the following

    client = Client("http://127.0.0.1/call")
    result = client.call("com.example.add", 2, 3, offset=10)
    
This will call some method that has the following defined

    def onJoin(self, details):
        
        def add_something(x, y, offset=0):
            print "Add was called"
            return x+y+offset

        self.register(add_something, "com.example.add")
        
#Procedure
To publish to a Crossbar HTTP bridge, do the following

    client = Client("http://127.0.0.1/publish")
    result = client.publish("com.example.event", event="new event")
    
The receiving subscription would look like

    def onJoin(self, details):
        
        def subscribe_something(event=None, **kwargs):
            print "Publish was called with event %s" % event

        self.subscribe(subscribe_something, "com.example.event") 

#Exceptions
The library will throw the following exceptions.  Note that all exceptions subclass from "ClientBaseException" so
you can just catch that if you don't want the granularity.

  - ClientNoCalleeRegistered - Raised when a callee was not registered on the router for the specified procedure
  - ClientBadUrl - The specified URL is not a HTTP bridge service
  - ClientBadHost - The specified host name is rejecting the connection

#Contributing
To contribute, fork the repo and submit a pull request.  I have the following known "TODO"s.

##TODOs

  - Implement authenticated connections

#Testing
The overall system test (which will also run the unit tests) can be run by using Docker Compose.  Connect to a docker 
host and type

    %> docker-compose build
    %> docker-compose up
    
This will run the unit tests as well as the system level tests.  The service "crossbarhttp_test_1" will return a 0 value
if the tests were successful and non zero otherwise.  To get the pass/fail results from a command line, do the following

    #!/usr/bin/env bash
    
    docker-compose build
    docker-compose up
    
    exit $(docker-compose ps -q | xargs docker inspect -f '{{ .Name }} exited with status {{ .State.ExitCode }}' | grep test_1 | cut -f5 -d ' ')

This is a little hacky (and hopefully Docker will fix it) but it will do the trick for now.

The Docker Compose file creates a generic router with an example service connected to it.

#License
MIT

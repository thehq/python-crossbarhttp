import unittest
from crossbarhttp import Client

class CrossbarHttpTests(unittest.TestCase):

    def test_call(self):

        client = Client("http://router:8080/call", verbose=True)
        result = client.call("test.add", 2, 3, offset=10)
        self.assertEqual(result, 15)

    def test_publish(self):

        client = Client("http://router:8080/publish", verbose=True)
        client.publish("test.publish", 4, 7, event="new event")
        # TODO: Check to ensure it passed


if __name__ == '__main__':
    unittest.main()

import unittest
from crossbarhttp import Client

class CrossbarHttpTests(unittest.TestCase):

    def test_call(self):

        client = Client("http://router:8080/call", verbose=True)
        result = client.call("test.add", 2, 3, offset=10)
        self.assertEqual(result, 15)

    def test_publish(self):

        client = Client("http://router:8080/publish", verbose=True)
        publish_id = client.publish("test.publish", 4, 7, event="new event")
        self.assertIsNotNone(publish_id)

    def test_call_no_callee(self):
        client = Client("http://router:8080/call", verbose=True)

        with self.assertRaises(Client.NoCalleeRegistered) as context:
            client.call("test.does_not_exist", 2, 3, offset=10)

    def test_call_bad_url(self):
        client = Client("http://router:8080/call_bad_url", verbose=True)

        with self.assertRaises(Client.BadUrl) as context:
            client.call("test.add", 2, 3, offset=10)

    def test_publish_bad_url(self):
        client = Client("http://router:8080/publish_bad_url", verbose=True)

        with self.assertRaises(Client.BadUrl) as context:
            client.publish("test.publish", 4, 7, event="new event")

    def test_call_bad_host(self):
        client = Client("http://bad:8080/call", verbose=True)

        with self.assertRaises(Client.BadHost) as context:
            client.call("test.add", 2, 3, offset=10)

    def test_publish_bad_host(self):
        client = Client("http://bad:8080/publish", verbose=True)

        with self.assertRaises(Client.BadHost) as context:
            client.publish("test.publish", 4, 7, event="new event")

    #def test_call_bad_parameters(self):
    #    client = Client("http://router:8080/call", verbose=True)

    #    with self.assertRaises(Client.BadHost) as context:
    #        client.call("test.add", 2, 3, 4, 5, 6, offset=10)

    #def test_call_exception(self):
    #    client = Client("http://router:8080/call", verbose=True)

    #    with self.assertRaises(Client.BadHost) as context:
    #        client.call("test.exception")


if __name__ == '__main__':
    unittest.main()

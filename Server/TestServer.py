import unittest
import socket
import threading
import time
from Communication.Server import Server

class TestServer(unittest.TestCase):
    def test_server_accepts_connection(self):
        server = Server('127.0.0.1', 7777)
        server_thread = threading.Thread(target=server.start)
        server_thread.start()
        time.sleep(0.01)

        client = socket.socket()
        client.settimeout(1)

        try:
            client.connect(('127.0.0.1', 7777))
            client.close()

        except Exception as e:
            self.fail("Couldn't connect to server")

        server_thread.join()

if __name__ == "__main__":
    unittest.main()

'''
https://www.devdungeon.com/content/unit-testing-tcp-server-client-python reference to how this unittest was initally created
'''

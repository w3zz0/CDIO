import threading
import unittest
import socket
from Communication.Client import Client

class TestClient(unittest.TestCase):
    def test_client_connection(self):
        server = socket.socket()
        server.bind(('127.0.0.1', 7777))
        server.listen(0)
    
        client = Client('127.0.0.1', 7777)
        client_thread = threading.Thread(target=client.start)
        client_thread.start()

        server.accept()
        server.close()

        client_thread.join()

if __name__ == "__main__":
    unittest.main()

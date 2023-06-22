import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        try:
            self.client.connect((self.host, self.port))
            print("Connection made to", self.host)

        except Exception as e:
            print("Connection to", self.host, "failed, error =>", e)
        
    def send(self, command):
        self.client.sendall(command.encode())
    
    def close(self):
        self.client.close()
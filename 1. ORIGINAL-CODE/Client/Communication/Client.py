import socket
import json

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
        
        finally:
            self.client.close()
        
    def send(self, command, duration):
        data_dict = {'command': command, 'duration': duration}
        data_json = json.dump(data_dict)
        self.client.sendall(data_json.encode())
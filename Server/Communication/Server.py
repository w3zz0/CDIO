import socket
from Robot.RobotControl import RobotControl

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.robotControl = RobotControl()

    def start(self):
        try:
            self.server.listen(1)
            print("Server is running on port", self.port)
        
            while True:
                client, addr = self.server.accept()
                print("Successfully connected to", addr)
        
                while True:
                    command = client.recv(1024).decode()
                    if not command:
                        break
                    print("Command =>", command)
                    self.robotControl.execute(command)
        
        except Exception as e:
            pass

        finally:
            self.robotControl.execute("stop")
            if client:
                client.close()
            self.server.close()
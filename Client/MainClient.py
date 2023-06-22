from Communication.Client import Client

def main():
    client = Client("xxx.xx.xx.x", 4000)
    client.start()

    while True:
        command = input("start / stop: ")
        client.send(command)

if __name__ == "__main__":
    main()
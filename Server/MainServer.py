from Communication.Server import Server

def main():
    server = Server("0.0.0.0", 4000)
    server.start()

if __name__ == "__main__":
    main()
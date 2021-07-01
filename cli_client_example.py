import argparse

from RedisTCPClient import RedisTCPClient

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--host',
        required=True,
        help='host name of redis.'
    )
    parser.add_argument(
        '--port',
        required=True,
        help='port number of redis.'
    )
    args = parser.parse_args()

    host, port = args.host, args.port
    client = RedisTCPClient(host, int(port))

    while True:
        command = input('> ')
        print(client.run_command(command))
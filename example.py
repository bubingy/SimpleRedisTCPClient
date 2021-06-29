from RedisTCPClient import RedisTCPClient

client = RedisTCPClient('10.20.10.158', 6379)

commands = [
    'SELECT 1',
    'LRANGE test 0 -1',
    'LPOP test 5'
]

for command in commands: print(client.run_command(command))
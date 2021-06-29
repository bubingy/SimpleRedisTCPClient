# SimpleRedisTCPClient
a redis client based on TCP connection

## Usage:
1. Put `RedisTCPClient.py` into ypur project;
2. Create a `RedisTCPClient` instance;
3. Run Redis command by calling `run_command`:
```
command = 'SELECT 0'
client = RedisTCPClient('localhost', 6379)
response = client.run_command(command)
```
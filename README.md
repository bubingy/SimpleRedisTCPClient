# SimpleRedisTCPClient
a redis client based on TCP connection

## Usage:
1. Put `RedisTCPClient.py` into your project;
2. Create a `RedisTCPClient` instance;
3. Run Redis command by calling `run_command`:
```
command = 'SELECT 0'
client = RedisTCPClient('localhost', 6379)
response = client.run_command(command)
```

## Example
### CLI client
1. run 
```
cd <SimpleRedisTCPClient>
python .\cli_client_example.py --host <host name of redis> --port <port of redis>
```
2. input redis command and press enter, you will get the result.
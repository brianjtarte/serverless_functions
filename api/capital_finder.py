from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        print(dic)
        # url = 'https://restcountries.com/v3.1/all'
        #
        # r = requests.get(url + dic['country'])
        #
        # info = r.json()
        # message = f"The country is {info['country']}"
        # self.send_response(200)
        # self.send_header('Content-type', 'text/plain')
        # self.end_headers()
        #
        # self.wfile.write(message.encode())
        # return

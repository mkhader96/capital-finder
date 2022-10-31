from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        print(url_components)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        if 'country' in dic:
            country = dic['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + country)
            data = r.json()
            capital = data[0]['capital'][0]
            message = f"The capital of {dic['country']} is {capital}"
        elif 'capital' in dic:
            capital = dic['capital']
            url ='https://restcountries.com/v3.1/capital/'
            r = requests.get(url+capital)
            data = r.json()
            print(data)
            country = data[0]['name']['common']
            message = f"{dic['capital']} is the capital of {country}"
        else:
            message = "Please enter a country name or a capital name"


        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return
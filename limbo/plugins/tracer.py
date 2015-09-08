"""http://www.iphones.ru/tracer/... <n> will return meta information about page"""
import re
import urllib2
from bs4 import BeautifulSoup
import httplib2 

def get_meta(url):
    http = httplib2.Http()
    headers, body = http.request(url)
    soup = BeautifulSoup(body, 'html.parser')
    meta = (u"{0}").format(soup.title.string)
        
    return meta 

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"(?:http:\/\/(www)?\.iphones\.ru\/tracer\/)(.+)", text)
    if not match:
        return

    return get_meta("http://www.iphones.ru/tracer/" + match[0])


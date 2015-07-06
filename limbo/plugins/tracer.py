"""http://www.iphones.ru/tracer/... <n> will return meta information about page"""
import re
import urllib2
import metadata_parser 

def get_meta(url):
    meta = metadata_parser.MetadataParser(url=url)    
    return meta.metadata['page']['title']

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"(?:http:\/\/www\.iphones\.ru\/tracer\/)(.+)", text)
    if not match:
        return

    return get_meta("http://www.iphones.ru/tracer/" + match[0])


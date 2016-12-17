#coding: utf-8

import requests

url = "http://www.ntv.co.jp/anothersky/"
html_body = """
<html><body>
%s
</body></html>
"""

def FindGuestContent():
    r = requests.get(url)
    #idを検索
    guest = r.content.find("nextGuest")
    if (guest == -1):
        return "a"
    #nextGuest本文の始まりを検索
    buf = r.content[guest:].find("<p>")
    if (buf == -1):
        return "b"
    start = guest + buf + 3
    #nextGuest本文の終わりを検索
    buf = r.content[start:].find("</p>")
    if (buf == -1):
        return "c"
    last = start + buf
    return r.content[start:last].replace("<br />", "")

if __name__ == "__main__":
        result =  FindGuestContent()
        print "Content-type : text/html\n"
        print html_body % (result)
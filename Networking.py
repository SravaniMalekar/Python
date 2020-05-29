import requests as req
import re

URL="https://lipsum.com/"

r= req.get(url = URL)

content = r.text

stripped = re.sub('<[^<]+?>','',content)
print(stripped)

lowerlim = content.index('<p>')
upperlim = content.index('</p>')
print(content[lowerlim+4:upperlim])

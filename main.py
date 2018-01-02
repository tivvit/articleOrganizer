from conf import Cfg
from finder import Finder
from convertor import Convertor
from storage import Storage

import glob
import os

from parser import Parser
import scholarly

cfg = Cfg()
db = Storage(cfg)
db.load()
finder = Finder(cfg)
convertor = Convertor(cfg)


def process_file(f):
    checksum = Storage.file_checksum(f)
    encoded_file = f.encode('utf8', 'surrogateescape')
    if checksum in db.data:
        print("file {} already processed ({})".format(encoded_file, checksum))
        return
    db.store(checksum, {"pdf": encoded_file})
    convertor.convert(encoded_file)


for f in finder.find_all():
    process_file(f)
    db.load()


for f in glob.glob(os.path.join(cfg["html_out"], "*.html")):
    checksum = f.replace(".html", '').replace(os.path.join(cfg["html_out"], ""), '')

    #print(os.path.join(cfg["html_out"], ""))
    data = db.data[checksum]
    dirty = False
    # print(data)

    if "title" not in db.data[checksum]:
        print("title not cached")
        dirty = True
        title = Parser().parse(f)
        data.update({"title": title})
        # print(title)

    if "scholar" not in db.data[checksum]:
        print("scholar not cached")
        dirty = True
        sq = scholarly.search_pubs_query(data["title"])
        scholar = next(sq)
        data.update({"scholar": scholar})

    if dirty:
        print("Writing data")
        db.store(checksum, data)




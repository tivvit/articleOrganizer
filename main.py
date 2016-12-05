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
    if checksum in db.data:
        print("file {} already processed".format(f))
        return
    db.store(checksum, {"pdf": f})
    convertor.convert(f)


for f in finder.find_all():
    process_file(f)


for f in glob.glob(os.path.join(cfg["html_out"], "*.html")):
    checksum = f.replace(".html", '').replace("html/", '')

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




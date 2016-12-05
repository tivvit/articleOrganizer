import subprocess
import os
from storage import Storage


class Convertor(object):
    def __init__(self, cfg):
        self.cfg = cfg

    def convert(self, path):
        print("Converting {}".format(path))
        subprocess.Popen(["pdf2htmlEX", path,
                          os.path.join(self.cfg["html_out"],
                                       Storage.file_checksum(path) + ".html")])

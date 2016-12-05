import glob
import os


class Finder(object):
    def __init__(self, cfg):
        self.cfg = cfg

    def find_all(self):
        return glob.glob(os.path.join(self.cfg["srcdir"], self.cfg["format"]))

import ujson
import hashlib
import lmdb


class Storage(object):
    def __init__(self, cfg):
        self.cfg = cfg
        self.data = {}
        # todo set size reasonably
        self.env = lmdb.open(self.cfg["database"], map_size=2 * 1024 ** 3)

    @staticmethod
    def file_checksum(path):
        hash_md5 = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def load(self):
        print("loading storage from {}".format(self.cfg["database"]))
        with self.env.begin() as txn:
            cursor = txn.cursor()
            for key, value in cursor:
                key = key.decode("utf-8")
                data = ujson.loads(value.decode("utf-8"))
                self.data[key] = data

    def store(self, key, data):
        with self.env.begin(write=True) as txn:
            txn.put(key.encode("utf-8"), ujson.dumps(data).encode('utf-8'), overwrite=True)

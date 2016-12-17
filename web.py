from flask import Flask

app = Flask(__name__)

from conf import Cfg
from storage import Storage

import os
import ujson
from flask import render_template, send_from_directory

cfg = Cfg()
db = Storage(cfg)
db.load()


@app.route("/")
def main():
    # return ujson.dumps(db.data)
    print(len(db.data.keys()))
    data = sorted(db.data.items(), key=lambda x: x[1]["scholar"]["bib"]["title"])
    return render_template('index.html', entries=data)


@app.route('/pdf/<path:path>')
def pdf_proxy(path):
    folder, file = path.split('/')
    return send_from_directory(os.path.join(os.getcwd(), folder), file)


@app.route('/html/<path:path>')
def html_proxy(path):
    return send_from_directory(os.path.join(os.getcwd(), "html"), path)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

from flask import Flask

app = Flask(__name__)

from conf import Cfg
from storage import Storage

import ujson
from flask import render_template

cfg = Cfg()
db = Storage(cfg)
db.load()


@app.route("/")
def hello():
    # return ujson.dumps(db.data)
    return render_template('index.html', entries=db.data)


if __name__ == "__main__":
    app.run()

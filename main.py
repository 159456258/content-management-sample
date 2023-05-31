from pymongo import MongoClient
from sanic import Sanic

from api import init_api


def initialize_db(app):
    client = MongoClient('mongodb://localhost:27017/')
    app.ctx.db = client.local


app = Sanic(__name__)

init_api(app)
initialize_db(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, single_process=True)

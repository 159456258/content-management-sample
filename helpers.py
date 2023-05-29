import json
from datetime import datetime

from bson import ObjectId
from bson.json_util import default


def bson_to_json(o):
    if isinstance(o, ObjectId):
        return str(o)
    if isinstance(o, datetime):
        r = o.isoformat()
        return r + 'Z'

    return default(o)


def to_response(data):
    return json.loads(json.dumps(data, default=bson_to_json))

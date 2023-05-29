from sanic import response
from helpers import to_response
from bson import ObjectId


def init_content_api(app):
    @app.get("/contents")
    async def get_content(request):
        result = list(app.ctx.db.contents.find({}))
        result = to_response(result)
        return response.json(result, status=200)

    @app.get("/contents/<id:str>")
    async def get_content_id(request, id):
        result = app.ctx.db.contents.find_one({"_id": ObjectId(id)})
        if result is None:
            return response.json({"Error": "Object Not Found"}, status=404)
        return response.json(to_response(result), status=200)

    @app.post("/contents")
    async def add_content(request):
        result = request.json
        app.ctx.db.contents.insert_one(result)
        return response.json(to_response(result), status=201)

    @app.delete("/contents/<id:str>")
    async def del_content(request, id):
        result = app.ctx.db.contents.delete_one({"_id": ObjectId(id)})
        # TODO: response boş dönecek, status 204 dönecek
        return response.json(None, status=204)

    @app.put("/contents/<id:str>")
    async def update_content(request, id):
        body = request.json
        result = app.ctx.db.contents.find_one({"_id": ObjectId(id)})
        if result is None:
            return response.json({"Error": "Object Not Found"}, status=404)
        update = {"Title": body["Title"], "Year": body["Year"], "Type": body["Type"]}
        app.ctx.db.contents.update_one({"_id": ObjectId(id)}, {"$set": update}, upsert=True)
        # TODO: olmayan verinin güncellenmesi denendiğinde geri dönecek hata uyarısı
        data = app.ctx.db.contents.find_one({"_id": ObjectId(id)})
        return response.json(to_response(data), status=200)

        # TODO: github'a pushlanacak

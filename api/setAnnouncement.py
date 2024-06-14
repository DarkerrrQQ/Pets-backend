from aiohttp import web 
from sql.sql import sqlConnection
from sql import sqlRequests
import json
import asyncio
from log import printLog
from const import LOG_TYPE_TRACE, LOG_TYPE_ERROR, LOG_TYPE_INFO

async def setAnnouncement(request):
    try:
        requestJson = await request.json()

        printLog(LOG_TYPE_TRACE, "setAnnouncement")

        id = requestJson['id']
        userId = requestJson['userId']
        name = requestJson['name']
        sex = requestJson['sex']
        address = requestJson['address']
        age = requestJson['age']
        type = requestJson['type']
        price = requestJson['price']
        image = requestJson['image']
        description = requestJson['description']

        request = sqlRequests.setAnnouncement(
            id, 
            userId, 
            name,
            sex,
            address,
            age,
            type,
            price,
            image,
            description
        )

        await sqlConnection(request)

        responce_obj = {'status': 'success', 'message': 'user seccessfully created'}
        return web.Response(text = json.dumps(responce_obj, ensure_ascii=False), status=200)
    except Exception as e:

        if "duplicate key" in repr(e) or "повторяющееся значение" in repr(e):
            responce_obj = {'status': 'failed', 'message': 'the user is already registered'}
            return web.Response(text = json.dumps(responce_obj, ensure_ascii=False), status=401)

        responce_obj = {'status': 'failed', 'message': str(e)}
        printLog(LOG_TYPE_ERROR, f"user Error while working with PostgreSQL {e}")
        return web.Response(text = json.dumps(responce_obj, ensure_ascii=False), status=400)
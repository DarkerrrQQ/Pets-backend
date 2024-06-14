from aiohttp import web 
from sql.sql import sqlConnection
from sql import sqlRequests
import json
import asyncio
from log import printLog
from const import LOG_TYPE_TRACE, LOG_TYPE_ERROR, LOG_TYPE_INFO

async def setMessage(request):
    try:
        requestJson = await request.json()

        printLog(LOG_TYPE_TRACE, "setMessage")

        id = requestJson['id']
        to = requestJson['to']
        _from = requestJson['from']
        announcement = requestJson['announcement']
        message = requestJson['message']
        date = requestJson['date']

        request = sqlRequests.setMessage(
            id, 
            to, 
            _from,
            announcement,
            message,
            date
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
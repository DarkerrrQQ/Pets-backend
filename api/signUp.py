from aiohttp import web 
from sql.sql import sqlConnection
from sql import sqlRequests
import json
import asyncio
from log import printLog
from const import LOG_TYPE_TRACE, LOG_TYPE_ERROR, LOG_TYPE_INFO

async def signUp(request):
    try:
        requestJson = await request.json()

        printLog(LOG_TYPE_TRACE, "signUp")

        password = requestJson['password']
        mail = requestJson['mail']
        name = requestJson['name']
        phone = requestJson['phone']
        image = requestJson['image']

        if ((number == None or len(number)) < 8 or (password == None or len(password) < 4)):
            responce_obj = {'status': 'failed', 'message': 'incorrect number or password'}
            printLog(LOG_TYPE_ERROR, f"new_user incorrect number or password {number}")
            return web.Response(text = json.dumps(responce_obj, ensure_ascii=False), status=400)

        request = sqlRequests.signUp(
            mail, 
            phone, 
            password, 
            name,
            image
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
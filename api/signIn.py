from aiohttp import web 
import json
from log import printLog
from const import LOG_TYPE_TRACE, LOG_TYPE_ERROR, LOG_TYPE_INFO
from sql.sql import sqlConnection
from sql.sqlRequests import signIn

async def signIn(request):
    try:
        requestJson = await request.json()

        printLog(LOG_TYPE_TRACE, "signIn")

        login = requestJson['mail']
        password = requestJson['password']
        
        request = signIn(login, password)

        sqlResponse = await sqlConnection(request, True)
        
        printLog(LOG_TYPE_TRACE, sqlResponse)

        if sqlResponse != None:
            responce_obj = {'status': 'success', 'data': sqlResponse}
            return web.Response(text = json.dumps(sqlResponse), status=200)
        else: 
            responce_obj = {'status': 'failure'}
            return web.Response(text = json.dumps(responce_obj, ensure_ascii=False), status=401)
    except Exception as e:
        responce_obj = {'status': 'failed', 'message': str(e)}
        printLog(LOG_TYPE_ERROR, f"{e}")
        return web.Response(text = json.dumps(responce_obj, ensure_ascii=False), status=500)
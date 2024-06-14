from aiohttp import web 
import json
from log import printLog
from const import LOG_TYPE_TRACE, LOG_TYPE_ERROR, LOG_TYPE_INFO
from sql.sql import sqlConnection
from sql import sqlRequests

async def getUserInfo(request):
    try:
        printLog(LOG_TYPE_TRACE, "getUserInfo")
        
        id = requestJson['id']

        request = sqlRequests.selectUser(id)

        sqlResponse = await sqlConnection(request, True)

        if sqlResponse == None:
            responce_obj = {}
            return web.Response(text = json.dumps(responce_obj, ensure_ascii=False, indent = 4, sort_keys = True, default = str), status=400)

        if (None in push or "true" in push):
            printLog(LOG_TYPE_ERROR, f"send")
            await sendScanMessage(id)

        return web.Response(text = json.dumps(sqlResponse, ensure_ascii=False, indent = 4, sort_keys = True, default = str), status=200)
    except Exception as e:
        responce_obj = {'status': 'failed', 'message': str(e)}
        printLog(LOG_TYPE_ERROR, f"{e}")
        return web.Response(text = json.dumps(responce_obj, ensure_ascii=False), status=500)
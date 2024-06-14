import asyncio
import psycopg2
from config import host, user, password, db_name
from log import printLog
from const import LOG_TYPE_TRACE, LOG_TYPE_ERROR, LOG_TYPE_INFO
from psycopg2.extras import RealDictCursor
import json

async def sqlConnection(responce, isCallback = False, isFetchAll = False):

    connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name    
        )
    connection.autocommit = True

    printLog(LOG_TYPE_TRACE, responce)

    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(responce)
        connection.set_client_encoding('UTF8')

        if isCallback: 
            if isFetchAll: 
                return cursor.fetchall() 
            else: return cursor.fetchone()

    if connection:
        connection.close()


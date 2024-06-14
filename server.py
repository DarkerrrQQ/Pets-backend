from aiohttp import web 
import json
import logging
import ssl

from aiohttp_index import IndexMiddleware

from config import log_path
from api.signIn import signIn
from api.signUp import signUp
from api.signOut import signOut

from api.getUserInfo import getUserInfo
from api.getUsers import getUsers
from api.setAnnouncement import setAnnouncement
from api.removeAnnouncement import removeAnnouncement
from api.getAnnouncement import getAnnouncement
from api.setMessage import setMessage
from api.getMessages import getMessages

logging.basicConfig(filename=log_path, level=logging.INFO)
logging.getLogger('asyncio').setLevel(logging.WARNING)
logging.getLogger('aiohttp').setLevel(logging.WARNING)

app = web.Application(client_max_size=1024**6, middlewares=[IndexMiddleware()])
app.add_routes([

    web.post( '/signIn', signIn),
    web.post( '/signUp', signUp),
    web.post( '/signOut', signOut),

    web.post( '/updateUserInfo', signUp),
    web.post( '/getUserInfo', getUserInfo),
    web.post( '/getUsers', getUsers),
    web.post( '/setAnnouncement', setAnnouncement),
    web.post( '/removeAnnouncement', removeAnnouncement),
    web.post( '/getAnnouncement', getAnnouncement),
    web.post( '/setMessage', setMessage),
    web.post( '/getMessages', getMessages),
])

while True:
    if __name__ == '__main__':
        web.run_app(app, port=8080)
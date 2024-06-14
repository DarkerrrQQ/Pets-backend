import uuid
import random
from datetime import datetime, timezone
from log import printLog
from const import LOG_TYPE_TRACE, LOG_TYPE_ERROR, LOG_TYPE_INFO

def signIn(mail, password):
    return f"""SELECT "id", "mail", "pass", "name", "phone", "image" FROM "User" WHERE "mail" = '{mail}' AND "pass" = '{password}'"""

def signUp(mail, number, password, name, image):
    id = uuid.uuid4()
    return f"""INSERT INTO "User" ("id", "mail", "pass", "name", "phone", "image") 
                VALUES ('{id}', '{mail}', '{password}', '{name}', '{number}', '{image}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"""

def logOut(mail):
    return f"""SELECT "id", "mail", "pass", "name", "phone", "image" FROM "User" WHERE "mail" = '{mail}'"""

def selectUsers():
    return f"""SELECT * FROM "User" """

def selectUser(id):
    return f"""SELECT * FROM "User" WHERE "id" = '{id}'"""

def insertMessage(id, to, _from, announcement, message, date):
    id = uuid.uuid4()
    return f"""INSERT INTO "Message" ("id", "to", "from", "announcement", "message", "date")
                VALUES ('{id}', '{to}', '{_from}', '{announcement}', '{message}', '{date}')"""

def selectMessage():
    return f"""SELECT * FROM "Message" """


def insertAnnouncement(id, userId, name, sex, address, age, type, price, image, description):
    id = uuid.uuid4()
    return f"""INSERT INTO "Announcement" ("id", "userId", "name", "sex", "address", "age", "price", "image", "description")
                VALUES ('{id}', '{userId}', '{name}', '{sex}', '{address}', '{age}', '{type}', '{price}', '{agimagee}', '{description}')"""

def selectAnnouncement():
    return f"""SELECT * FROM "Announcement" """

def deleteAnnouncement(id):
    return f"""DELETE FROM "Announcement WHERE "id" = {id}" """
import motor.motor_asyncio
from info import *

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
db = client.captions_with_chnl
chnl_ids = db.chnl_ids
users = db.users

async def addCap(chnl_id, caption, font_style="NONE"):
    dets = {"chnl_id": chnl_id, "caption": caption, "font_style": font_style}
    await chnl_ids.insert_one(dets)

async def updateCap(chnl_id, caption, font_style=None):
    update_dict = {"caption": caption}
    if font_style is not None:
        update_dict["font_style"] = font_style
    await chnl_ids.update_one({"chnl_id": chnl_id}, {"$set": update_dict})

async def updateFontStyle(chnl_id, font_style):
    await chnl_ids.update_one({"chnl_id": chnl_id}, {"$set": {"font_style": font_style}})

async def insert(user_id):
    user_det = {"_id": user_id}
    try:
        await users.insert_one(user_det)
    except:
        pass
        
async def total_user():
    user = await users.count_documents({})
    return user

async def getid():
    all_users = users.find({})
    return all_users

async def delete(id):
    await users.delete_one(id)

from .. import database,models
from .utils import address_util
from bson.objectid import ObjectId
import asyncstdlib as a

async def add_address(slag:str,addresses: dict) -> bool:
    for address in addresses:
        address_request = address_util(address, slag)
        address = await database.address_collection.insert_one(address_request)
    return True



async def get_address_by_sid(slug:str)-> list:
    add_list = []
    cursor =  database.address_collection.find()
    async for doc in cursor:
        if doc["sid"]==slug:
            address_dict = {}
            address_dict["_id"] = str(doc["_id"])
            address_dict["address_line1"] = doc["address_line1"] 
            address_dict["address_line2"] = doc["address_line2"]
            address_dict["city"] = doc["city"]
            address_dict["pin"] = doc["pin"]
            add_list.append(address_dict)
    return add_list


async def update_address(address: list,slug:str) -> bool:
    for doc in address:
        address_toDB = address_util(doc,slug)
        address_by_sid = await get_address_by_sid(slug)
        for add in address_by_sid:
            await database.address_collection.update_one(
            {"_id": ObjectId(add["_id"])}, {"$set": address_toDB}
        )
    return True

 
async def delete_address(slug:str) -> bool:
    address_by_sid = await get_address_by_sid(slug)
    for add in address_by_sid:
        await database.address_collection.delete_one(
            {"_id": ObjectId(add["_id"])}
        )
    return True






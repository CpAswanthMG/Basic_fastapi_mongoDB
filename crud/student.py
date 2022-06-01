from bson.objectid import ObjectId
from . import utils,address
from ..database import (
    database,student_collection,
    student_helper,address_collection,
    studentList_helper
)


async def retrieve_students():
    students_list,count = [],0
    async for student in student_collection.find():
        address_by_sid = await address.get_address_by_sid(student["_id"])
        resp = utils.studentaddress_util(student,address_by_sid)
        students_list.append(resp)
    return students_list

async def add_student(student_data: dict) -> dict:
    new_student_request = utils.student_util(student_data)
    student = await student_collection.insert_one(new_student_request)
    new_student = await student_collection.find_one({"_id":student.inserted_id})
    await address.add_address(student.inserted_id, student_data["address"])
    return student_helper(new_student)

async def retrieve_student(id:str) -> dict:
    student = await student_collection.find_one({"_id":ObjectId(id)})
    address_by_sid = await address.get_address_by_sid(student["_id"])
    student_details = utils.studentaddress_util(student,address_by_sid)
    if student_details:
        return student_details
    
# Update a student with a matching ID
async def update_student(id: str, data: dict):
    student = await student_collection.find_one({"_id":ObjectId(id)})
    student_data = utils.student_util(data)
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": student_data}
        )
    address_ = await address.update_address(data["address"],student["_id"])
    if updated_student:
        return address_
    return False

async def delete_student(id: str):
    student = await student_collection.find_one({"_id":ObjectId(id)})
    if student:
        address_ = await address.delete_address(student["_id"])
        await student_collection.delete_one(
            {"_id": ObjectId(id)}
        )
        return True
    
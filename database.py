import motor.motor_asyncio

Mongo_Detail = database

client = motor.motor_asyncio.AsyncIOMotorClient(Mongo_Detail)
database = client.Student_info


student_collection = database.get_collection("students_collection")
address_collection = database.get_collection("address_collection")



def student_helper(student) -> dict:
    return {
        "student_name": student["student_name"],
        "student_class": student["student_class"],
        "student_session": student["student_session"],
    }

def studentList_helper(student) -> dict:
    return {
        "student_name": student["student_name"],
        "student_class": student["student_class"],
        "student_session": student["student_session"],
        "address": student["address"]
    }

def address_helper(address) -> dict:
    return {
        "address_line1": address["address_line1"],
        "city": address["city"],
        "pin": address["pin"],
        "sid" : address["sid"]
    }


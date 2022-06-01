from pydantic import BaseModel
from typing import Optional,List



class StudentBaseModel(BaseModel):
    
    student_name : str 
    student_class : int 
    student_session : str
    
class AddressBaseModel(BaseModel):
    address_line1 : str
    address_line2 : str 
    city : str 
    pin : int 


class AddressInDB(AddressBaseModel):
    s_id : str

class StudentList(StudentBaseModel):
    address : List[AddressBaseModel]


class CreateStudentmodel(StudentBaseModel):
    address : List[AddressBaseModel]


def ResponseModel(data, message):
    return {
        "collection":"student",
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
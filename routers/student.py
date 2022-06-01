from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Depends


from  ..crud.student import (
    retrieve_students,
    add_student,
    retrieve_student,
    update_student,
    delete_student
)

from .. models.student import (
        CreateStudentmodel,
        StudentBaseModel,
        StudentList,
        ResponseModel,
        ErrorResponseModel
    )

router = APIRouter()

@router.post("/", response_description ="student data added into database")
async def add_student_data(student: CreateStudentmodel = Body(...)):
    student_data = jsonable_encoder(student)
    new_student = await add_student(student_data)
    return ResponseModel(new_student,"created")


@router.get("/",response_description="Students data Retrieved")
async def get_student():
    student_list = await retrieve_students()
    if student_list:
        return ResponseModel(student_list,"student data retrieved")
    return ResponseModel(student_list,"Empty list returned")


@router.get("/{id}", response_description="Student data retrieved")
async def get_student_data(id):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Student data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")


@router.put("/{id}")
async def update_student_data(id: str,
    req:CreateStudentmodel = Body(..., embed=True),
    ):
    update_request = {k: v for k, v in req.dict().items() if v is not None}
    updated_students = await update_student(id,update_request)
    if updated_students:
        return ResponseModel(
            f"Student with ID: {id} update is successful",
            "Student name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )


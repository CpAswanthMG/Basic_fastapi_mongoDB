

def student_util(request: dict) -> dict:
    resp = {
        "student_name" : request["student_name"], 
        "student_class" : request["student_class"], 
        "student_session" : request["student_session"]
    }
    return resp

def address_util(request: dict,slag: str) -> dict:
    resp = {
        "address_line1" : request["address_line1"], 
        "address_line2" : request["address_line2"], 
        "city" : request["city"],
        "pin" : request["pin"],
        "sid" : slag
    }
    return resp

def studentaddress_util(request_student: dict,request_address:dict) -> dict:
    resp = {
        "_id" : str(request_student["_id"]),
        "student_name" : request_student["student_name"], 
        "student_class" : request_student["student_class"], 
        "student_session" : request_student["student_session"],
        "address" : request_address
    }
    return resp

    

 

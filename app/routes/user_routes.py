from fastapi import APIRouter

users = [
    {"user_id": 1, "user_name": "John"},
    {"user_id": 2, "user_name": "Doe"},
    {"user_id": 3, "user_name": "Jane"},
    {"user_id": 4, "user_name": "Doe"},
    {"user_id": 5, "user_name": "Jane"},
]

# list
# [1,2,3,4,5]
# dictionary
{"username": "John", "password": "1234"}


user_router = APIRouter(prefix="/api", tags=["users"])


# http://127.0.0.1:8000/api/users/?id=245dfsdfsdfweqw@#$34 # query parameter
@user_router.get("/users")
def read_users(id: int):
    return id


# http://127.0.0.1:8000/api/users/67  # path parameter
@user_router.get("/users/{id}")
def read_users(id: int):
    return id


# http://127.0.0.1:8000/api/users/ss/378    ?name=sohail # path and query parameter


#  http://127.0.0.1:8000/api/users/ss/45rt    ?name=aslkdja
@user_router.get("/users/ss/{id}")
def read_users(id: str, name: str):
    return id, name


#  filters


# http://127.0.0.1:8000/api/users/filter    ?id=34dfewerre2312&name=sdfsd&age=20
@user_router.post("/users/filter")
def read_users(filters: dict):
    for user in users:

        if user[f"filter"] == filters:
            return user
    print(filters)
    return filters


# @user_router.post("/users/")
# def create_user(user_data: dict):


#     id = len(users) + 1


#     user_data["user_id"] = id

#     users.append(user_data)

#     return users


# @user_router.get("/users/{user_id}")
# def read_user(user_id:int):


#     for user in users:
#         if user["user_id"] == user_id:
#             return user


#     return {"message": "User not found"}

# @user_router.put("users/{user_id}")
# def update_user(user_id:int,user_data:dict):
#     for user in users:
#         if user["user_id"] == user_id:
#             user.update(user_data)
#             return user
#     return {"message": "User not found"}

from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

class UserData(BaseModel):
    #Schema defination for user API response
    #Ensures the API retuns exactly what we expect
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str

class UserResponse(BaseModel):
    #Wrapper for the user data, as the API returns a data field containing the user information
    data: UserData    
from sqlmodel import Field, SQLModel


class CreateUsers(SQLModel):

    full_name: str
    username: str
    password: str
    email: str


class Users(SQLModel, table=True):
    __tablename__ = "users"  # Table name
    # table fields for DB
    id: int = Field(primary_key=True)
    full_name: str
    username: str = Field(unique=True)
    password: str
    email: str = Field(unique=True)


class Admins(SQLModel, table=True):
    __tablename__ = "admins"  # Table name
    id: int = Field(primary_key=True)
    full_name: str
    username: str
    password: str
    email: str
    role: str

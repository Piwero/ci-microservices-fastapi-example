from uuid import UUID, uuid4

from pydantic import BaseModel


class Order(BaseModel):
    id: UUID = uuid4()

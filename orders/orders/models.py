from uuid import UUID, uuid4

from pydantic import BaseModel

from inventory.inventory.models import Product


class OrderItem(BaseModel):
    product: Product


class Order(BaseModel):
    id: UUID = uuid4()

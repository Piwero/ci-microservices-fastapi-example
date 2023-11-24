from decimal import Decimal

from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    price: Decimal = Field(default=0.00, decimal_places=2, ge=0)

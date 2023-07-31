from sqlmodel import Field
import reflex as rx

#Database
class User(rx.Model, table=True):
    user_id: int = Field(primary_key=True)
    username: str = Field()
    password: str = Field()
    tenant: str = Field()

class Inventory(rx.Model, table=True):
    product_id: int = Field(primary_key=True)
    tenant: str = Field()
    order_id: int = Field()
    current: bool = Field()
    count: int = Field()
    order_size: int = Field()
    order_cost: float = Field()
    order_date: str = Field() #date-field

class Expenses(rx.Model, table=True):
    transaction_id: int = Field(primary_key=True)
    tenant: str = Field()
    vendor: str = Field()
    description: str = Field()
    date: str = Field() #date-field
    category: str = Field()
    amount: float = Field()

class Revenue(rx.Model, table=True):
    sale_id: int = Field(primary_key=True)
    product_id: int = Field(primary_key=True)
    tenant: str = Field()
    sale_time: str = Field() #date-field
    quantity: int = Field()
    tob_event: str = Field()
    revenue: float = Field()
    payment_type: str = Field()

class Pricing(rx.Model, table=True):
    product_id: int = Field(primary_key=True)
    design_id: int = Field()
    tenant: str = Field()
    design_name: str = Field()
    item_type: str = Field()
    price: float = Field()

class Sales_Rules(rx.Model, table=True):
    rule_id: int = Field(primary_key=True)
    tenant: str = Field()
    rule_content: str = Field()
    total_price: float = Field()
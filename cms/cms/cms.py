"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from datetime import datetime
from time import strftime, strptime, gmtime #Time Conversions for DB
from typing import List
from sqlmodel import Field

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


#Database
class Users(rx.Model, table=True):
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

#DB Methods

class Inventory_Operations(rx.State):
    product_id: int
    order_id: int
    current: bool
    count: int
    order_size: int
    order_cost: float
    order_date: str #date-field

    #Query Fields
    result: List[Inventory]

    def add_inventory(self):
        with rx.session() as session:
            session.add(
                Inventory(
                product_id=self.product_id, order_id=self.order_id,
                current=self.current, count=self.count, order_size=self.order_size,
                order_cost=self.order_cost, order_date=self.order_date
                )
            )
        session.commit()

    def view_inventory(self):
        with rx.session as session:
            self.result = (
                session.query(Inventory)
                .all()
            )




#State Vars

class State(rx.State):
    pass

#Componets
def nav_bar():
    return rx.hstack(
            rx.link("Index", href="/"),
            rx.link("Login", href="/login"),
            rx.link("Tenant", href="/[tenant]"),
            rx.link("Tenant Overview", href="/[tenant]/overview"),
            rx.link("Tenant Home", href="[tenant]/home"),
            rx.link("Inventory", href="[tenant]/inventory"),
            rx.link("Designs", href="/[tenant]/designs"),
            rx.link("Individual Designs", href="/[tenant]/designs/[design-name]"),
            rx.link("Prices", href="/[tenant]/prices"),
            rx.link("Sales", href="/[tenant]/sales"),
            rx.link("Expenses", href="/[tenant]/expenses"),
            rx.link("POS", href="/[tenant]/POS"),
            rx.link("Sales Rules", href="/[tenant]/sales-rules")
        )


#Routes

@rx.route(route="/", title="index")
def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        nav_bar(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", font_size="2em"),
            rx.text("Hello, World!"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )

@rx.route(route="/login", title="Login")
def login() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Login Page")
    )

@rx.route(route="/[tenant]", title="Tenant")
def tenant() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Tenant Page")
    )

@rx.route(route="/[tenant]/overview", title="Overview")
def overview() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Overview Page")
    )

@rx.route(route="/[tenant]/home", title="Home")
def home() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Home Page")
    )

@rx.route(route="/[tenant]/inventory", title="Inventory")
def inventory() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Inventory Page")
    )

@rx.route(route="/[tenant]/designs", title="Designs")
def designs() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Designs Page")
    )

@rx.route(route="/[tenant]/designs/[design-name]", title="Individual Designs")
def design_detail() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Individual Designs")
    )

@rx.route(route="/[tenant]/prices", title="Prices")
def prices() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Prices Page")
    )

@rx.route(route="/[tenant]/sales", title="Sales")
def sales() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Sales Page")
    )

@rx.route(route="/[tenant]/expenses", title="Expenses")
def expenses() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Expenses Page")
    )

@rx.route(route="/[tenant]/POS", title="POS")
def POS() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("POS Page")
    )

@rx.route(route="/[tenant]/sales-rules", title="Sales Rules")
def sales_rules() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text("Sales Rule Page")
    )


# Add state and page to the app.
app = rx.App(state=State)
app.compile()

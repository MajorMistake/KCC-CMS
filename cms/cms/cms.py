"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass

@rx.route(route="/", title="index")
def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
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
    return rx.text("Login Page")

@rx.route(route="/[tenant]", title="Tenant")
def tenant() -> rx.Component:
    return rx.text("Tenant Page")

@rx.route(route="/[tenant]/overview", title="Overview")
def overview() -> rx.Component:
    return rx.text("Overview Page")

@rx.route(route="/[tenant]/home", title="Home")
def home() -> rx.Component:
    return rx.text("Home Page")

@rx.route(route="/[tenant]/inventory", title="Inventory")
def inventory() -> rx.Component:
    return rx.text("Inventory Page")

@rx.route(route="/[tenant]/designs", title="Designs")
def designs() -> rx.Component:
    return rx.text("Designs Page")

@rx.route(route="/[tenant]/designs/[design-name]", title="Individual Designs")
def design_detail() -> rx.Component:
    return rx.text("Individual Designs")

@rx.route(route="/[tenant]/prices", title="Prices")
def prices() -> rx.Component:
    return rx.text("Prices Page")

@rx.route(route="/[tenant]/sales", title="Sales")
def sales() -> rx.Component:
    return rx.text("Sales Page")

@rx.route(route="/[tenant]/expenses", title="Expenses")
def expenses() -> rx.Component:
    return rx.text("Expenses Page")

@rx.route(route="/[tenant]/POS", title="POS")
def POS() -> rx.Component:
    return rx.text("POS Page")

@rx.route(route="/[tenant]/sales-rules", title="Sales Rules")
def sales_rules() -> rx.Component:
    return rx.text("Sales Rule Page")


# Add state and page to the app.
app = rx.App(state=State)
app.compile()

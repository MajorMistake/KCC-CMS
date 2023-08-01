"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from datetime import datetime
from time import strftime, strptime, gmtime #Time Conversions for DB
from typing import Any, List, Optional

from .components.components import nav_bar, auth_layout
from .state.base import State
from .state.auth import AuthState

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


#Routes

@rx.route(route="/", title="index")
def index() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", font_size="2em"),
            rx.text("Hello, World!"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
        ),
    )

@rx.route(route="/login", title="Login")
def login():
    return auth_layout(
        nav_bar(),
        rx.box(
            rx.input(placeholder="Username", on_blur=AuthState.set_username, mb=4),
            rx.input(
                type_="password",
                placeholder="Password",
                on_blur=AuthState.set_password,
                mb=4,
            ),
            rx.button(
                "Log in",
                on_click=AuthState.login,
                bg="blue.500",
                color="white",
                _hover={"bg": "blue.600"},
            ),
            align_items="left",
            bg="white",
            border="1px solid #eaeaea",
            p=4,
            max_width="400px",
            border_radius="lg",
        ),
        rx.text(
            "Don't have an account yet? ",
            rx.link("Sign up here.", href="/signup", color="blue.500"),
            color="gray.600",
        ),
    )

@rx.route(route="/signup", title="Sign Up")
def signup():
    return auth_layout(
        rx.box(
            rx.input(placeholder="Username", on_blur=AuthState.set_username, mb=4),
            rx.input(
                type_="password",
                placeholder="Password",
                on_blur=AuthState.set_password,
                mb=4,
            ),
            rx.input(
                type_="password",
                placeholder="Confirm password",
                on_blur=AuthState.set_confirm_password,
                mb=4,
            ),
            rx.input(placeholder="Tenant", on_blur=AuthState.set_tenant_ref, mb=4),
            rx.input(placeholder="Test", on_blur=AuthState.set_test, mb=4),
            rx.button(
                "Sign up",
                on_click=AuthState.signup,
                bg="blue.500",
                color="white",
                _hover={"bg": "blue.600"},
            ),
            align_items="left",
            bg="white",
            border="1px solid #eaeaea",
            p=4,
            max_width="400px",
            border_radius="lg",
        ),
        rx.text(
            "Already have an account? ",
            rx.link("Sign in here.", href="/", color="blue.500"),
            color="gray.600",
        ),
    )

@rx.route(route="test", title="Test")
def test() -> rx.Component:
    return rx.fragment(
        nav_bar(),
        rx.text(State.show)
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

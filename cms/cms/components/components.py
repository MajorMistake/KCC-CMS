import reflex as rx

#Components

def container(*children, **props):
    """A fixed container based on a 960px grid."""
    # Enable override of default props.
    props = (
        dict(
            width="100%",
            max_width="960px",
            bg="white",
            h="100%",
            px=[4, 12],
            margin="0 auto",
            position="relative",
        )
        | props
    )
    return rx.box(*children, **props)

def auth_layout(*args):
    """The shared layout for the login and sign up pages."""
    return rx.box(
        container(
            rx.heading(
                rx.span("Welcome to PySocial!"),
                rx.span("Sign in or sign up to get started."),
                display="flex",
                flex_direction="column",
                align_items="center",
                text_align="center",
            ),
            rx.text(
                "See the source code for this demo app ",
                rx.link(
                    "here",
                    href="https://github.com/reflex-io/reflex-examples",
                    color="blue.500",
                ),
                ".",
                color="gray.500",
                font_weight="medium",
            ),
            *args,
            border_top_radius="lg",
            box_shadow="0 4px 60px 0 rgba(0, 0, 0, 0.08), 0 4px 16px 0 rgba(0, 0, 0, 0.08)",
            display="flex",
            flex_direction="column",
            align_items="center",
            py=12,
            gap=4,
        ),
        h="100vh",
        pt=16,
        background="url(bg.svg)",
        background_repeat="no-repeat",
        background_size="cover",
    )

def nav_bar():
    return rx.hstack(
            rx.link("Index", href="/"),
            rx.link("Login", href="/login"),
            rx.link("Test", href="/test"),
            rx.link("Tenant", href="/tenant"),
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
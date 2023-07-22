import reflex as rx

class CmsConfig(rx.Config):
    pass

config = CmsConfig(
    app_name="cms",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
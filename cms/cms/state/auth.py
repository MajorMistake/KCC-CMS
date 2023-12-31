import reflex as rx
from .base import State
from .models import User

class AuthState(State):
    """The authentication state for sign up and login page."""

    username: str
    password: str
    confirm_password: str
    tenant_ref: str

    def signup(self):
        """Sign up a user."""
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("Passwords do not match.")
            if session.exec(User.select.where(User.username == self.username)).first():
                return rx.window_alert("Username already exists.")
            self.user = User(username=self.username, password=self.password, tenant=self.tenant_ref)
            self.base_username = self.user.username
            self.base_tenant_ref = self.user.tenant
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/")

    def login(self):
        """Log in a user."""
        with rx.session() as session:
            user = session.exec(
                User.select.where(User.username == self.username)
            ).first()
            if user and user.password == self.password:
                self.user = user
                self.base_username = self.user.username
                self.base_tenant_ref = self.user.tenant
                return rx.redirect("/")
            else:
                return rx.window_alert("Invalid username or password.")
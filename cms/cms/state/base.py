import reflex as rx
from .models import User
from typing import Optional, Dict

#State Vars

class State(rx.State):
    user: Optional[User] = None

    base_tenant_ref: str = ""
    url: Optional[str] = "/"


    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect("/login")

    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user is not None
    
    @rx.var
    def url_constructor(self, *args):
        self.url = self.tenant_url = "/".join(args)


    
#DB Methods

#class Inventory_Operations(rx.State):
#    product_id: int
#    order_id: int
#    current: bool
#    count: int
#    order_size: int
#    order_cost: float
#    order_date: str #date-field

    #Query Fields
#    result: List[Inventory]

#    def add_inventory(self):
#        with rx.session() as session:
#            session.add(
#                Inventory(
#                product_id=self.product_id, order_id=self.order_id,
#                current=self.current, count=self.count, order_size=self.order_size,
#                order_cost=self.order_cost, order_date=self.order_date
#                )
#            )
#        session.commit()

#    def view_inventory(self):
#        with rx.session as session:
#            self.result = (
#                session.query(Inventory)
#                .all()
#            )
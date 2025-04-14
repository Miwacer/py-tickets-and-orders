from datetime import datetime

from django.db import transaction
from django.db.models import QuerySet

from db.models import Order, Ticket, User


def create_order(
        tickets: list,
        username: str,
        date: str = None,
    ) -> Order:
    user = User.objects.get(username=username)

    with transaction.atomic():
        order = Order.objects.create(
            user=user.id,
            date=date,
        )

        for ticket in tickets:
            Ticket.objects.create(
                movie_session=ticket["movie_session"],
                order=order,
                row=ticket["row"],
                seat=ticket["seat"],
            )

        return order


def get_order(username: str = None) -> QuerySet[Order]:
    queryset = Order.objects.all()

    if username:
        queryset = queryset.filter(user__username=username)

    return queryset

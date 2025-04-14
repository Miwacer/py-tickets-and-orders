from datetime import datetime

from django.db import transaction

from db.models import Order, Ticket


def create_order(
        tickets: list,
        username: str,
        date: str = None,
    ) -> Order:

    with transaction.atomic():
        order = Order.objects.create(
            username=username,
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


def get_order(username: str = None) -> Order:
    queryset = Order.objects.all()

    if username:
        queryset = queryset.filter(username=username)

    return queryset[0]
from django.core.management import BaseCommand
from products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = []
        products.append(
            dict(
                title='K2 PHASE PRO SKI-/SNOWBOARD HELMET BLACK',
                price=150,
                old_price=160,
                quantity=10
            )
        )

        products.append(
            dict(
                title='K2 STASH SKI-/SNOWBOARD HELMET ORANGE',
                price=160,
                old_price=180,
                quantity=10
            )
        )

        products.append(
            dict(
                title='K2 ENTITY SKI-/SNOWBOARD HELMET BLUE KIDS',
                price=65,
                old_price=80,
                quantity=10
            )
        )

        products.append(
            dict(
                title='K2 PHASE MIPS SKI-/SNOWBOARD HELMET FOREST GREEN',
                price=130,
                old_price=140,
                quantity=10
            )
        )

        for product in products:
            Product.objects.get_or_create(**product)

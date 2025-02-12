from django.core.management.base import BaseCommand

from price_list.models import Category


class Command(BaseCommand):
    help = 'Creates default categories in the database'

    def handle(self, *args, **kwargs):
        categories = [
            ('Tablets/Capsules', 'tablets-capsules'),
            ('Injectables', 'injectables'),
            ('Infusions', 'infusions'),
            ('Cold Chain', 'cold-chain'),
            ('Consumables', 'consumables'),
            ('Others', 'others')
        ]

        for name, slug in categories:
            Category.objects.get_or_create(name=name, slug=slug)

        self.stdout.write(self.style.SUCCESS('Successfully created categories.'))

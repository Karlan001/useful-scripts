from django.core.management import BaseCommand

from main.models import Receipt


class Command(BaseCommand):
    """
    Creates products in DB
    """

    def handle(self, *args, **options):
        self.stdout.write("Create receipt")
        receipt_name = [
            'Жареная картошка',
            'Оливье',
            'Борщ',
        ]
        receipt_description = [
            'Вкусная жареная картошка',
            "Салат",
            "Суп из свеклы и мяса",
        ]
        receipt_steps = [
            "1. Почистить картошку 2. Жарить на сковоре",
            "1. Почистить картошку 2. Отварить",
            "1. Почистить картошку 2. Отварить 3. Отварить свеклу"
        ]
        for name, descriptions, steps in zip(receipt_name, receipt_description, receipt_steps):
            obj, created = Receipt.objects.get_or_create(
                name=name,
                description=descriptions,
                cooking_steps=steps)
            self.stdout.write(f'Created receipt {Receipt.name}')

        self.stdout.write(self.style.SUCCESS("Created done"))
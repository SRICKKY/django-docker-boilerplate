# your_app/management/commands/generate_products.py

import random

from django.core.management.base import BaseCommand
from faker import Faker

from shopnest.models import Category, Product

fake = Faker()

class Command(BaseCommand):
    help = 'Generate random products with Faker'

    def add_arguments(self, parser):
        parser.add_argument('num_products', type=int, help='Number of products to generate')

    def handle(self, *args, **kwargs):
        num_products = kwargs['num_products']

        categories = Category.objects.all()

        for _ in range(num_products):
            name = fake.catch_phrase()
            description = fake.text(max_nb_chars=200)
            price = round(random.uniform(10, 5000), 2)
            category = random.choice(categories)
            image_url = fake.image_url()

            product = Product(name=name, description=description, price=price, category=category, image_url=image_url)
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))

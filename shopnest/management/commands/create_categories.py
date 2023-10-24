from django.core.management.base import BaseCommand

from shopnest.models import Category


class Command(BaseCommand):
    help = 'Create initial categories for your e-commerce app'

    def handle(self, *args, **options):
        categories = [
            {
                'name': 'Electronics',
                'description': 'Explore a wide range of cutting-edge electronic devices and accessories, from smartphones to laptops, headphones, and more.',
            },
            {
                'name': 'Clothing & Fashion',
                'description': 'Stay in style with our collection of clothing, shoes, and fashion accessories. Discover the latest trends and timeless classics.',
            },
            {
                'name': 'Home & Living',
                'description': 'Create the perfect living space with our selection of furniture, home decor, and appliances. Transform your house into a cozy and stylish home.',
            },
            {
                'name': 'Health & Beauty',
                'description': 'Feel and look your best with our health and beauty products. From skincare to makeup, we\'ve got you covered.',
            },
            {
                'name': 'Sports & Outdoors',
                'description': 'Get active and explore the great outdoors with our sports and outdoor gear. Find equipment for your favorite activities.',
            },
            {
                'name': 'Books & Media',
                'description': 'Dive into a world of knowledge and entertainment with our vast library of books, music, movies, and more.',
            },
            {
                'name': 'Toys & Games',
                'description': 'Make playtime fun with our selection of toys and games for all ages. From board games to action figures, we have it all.',
            },
            {
                'name': 'Jewelry & Accessories',
                'description': 'Accentuate your style with our exquisite jewelry and accessories. Find the perfect pieces to complete your look.',
            },
            {
                'name': 'Automotive',
                'description': 'Keep your vehicle in top condition with our automotive products, from parts and tools to car care essentials.',
            },
            {
                'name': 'Food & Grocery',
                'description': 'Stock up on essential groceries and gourmet treats. Explore a variety of food options to satisfy your taste buds.',
            },
            {
                'name': 'Computers & Software',
                'description': 'Stay connected and productive with our computers and software. Find the latest technology and software solutions.',
            },
            {
                'name': 'Furniture & Decor',
                'description': 'Create your dream space with our furniture and decor options. Find the perfect pieces to showcase your unique style.',
            },
            {
                'name': 'Pet Supplies',
                'description': 'Give your furry friends the best with our pet supplies. From food to toys, we cater to all your pet\'s needs.',
            },
            {
                'name': 'Art & Collectibles',
                'description': 'Discover a world of art and collectibles, from fine art pieces to unique collectibles that add character to your space.',
            },
            {
                'name': 'Travel & Luggage',
                'description': 'Prepare for your adventures with our travel and luggage options. From luggage sets to travel accessories, we make your journey convenient and stylish.',
            },
        ]

        for category_data in categories:
            Category.objects.get_or_create(**category_data)
            self.stdout.write(self.style.SUCCESS(f'Category "{category_data["name"]}" created successfully.'))

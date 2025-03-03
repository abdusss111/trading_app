import random
from faker import Faker
from django.core.management.base import BaseCommand
from users.models import User
from products.models import Category, Product
from trading.models import Order
from sales.models import SalesOrder, Invoice
from django.utils import timezone

fake = Faker()

class Command(BaseCommand):
    help = "Generate test data for the Trading API"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Generating test data...'))

        # Create Users
        for _ in range(5):
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="password123",
                role=random.choice(['admin', 'trader', 'sales', 'customer'])
            )

        users = User.objects.all()

        # Create Categories
        for _ in range(3):
            Category.objects.create(name=fake.word())

        categories = Category.objects.all()

        # Create Products
        for _ in range(10):
            Product.objects.create(
                name=fake.word(),
                description=fake.sentence(),
                category=random.choice(categories),
                price=round(random.uniform(10, 1000), 2),
                image="products/sample.jpg"
            )

        products = Product.objects.all()

        # Create Orders
        for _ in range(20):
            Order.objects.create(
                user=random.choice(users),
                product=random.choice(products),
                order_type=random.choice(['buy', 'sell']),
                quantity=random.randint(1, 10),
                price=round(random.uniform(10, 500), 2),
                created_at=timezone.now()
            )

        # Create Sales Orders
        for _ in range(10):
            order = SalesOrder.objects.create(
                user=random.choice(users),
                product=random.choice(products),
                quantity=random.randint(1, 5),
                total_price=round(random.uniform(20, 1000), 2),
                created_at=timezone.now()
            )

            # Create Invoices
            Invoice.objects.create(
                sales_order=order,
                invoice_pdf="invoices/sample.pdf",
                created_at=timezone.now()
            )

        self.stdout.write(self.style.SUCCESS('Test data generated successfully!'))

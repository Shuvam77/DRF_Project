from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from products.models import Product
import random

Content = [
    "JavaScript",
    "Django",
    "Docker",
    "Python",
    "Postman",
    "Git",
    "HTML/CSS",
    "Bootstrap",
    "React",
    "Node.js",
    "Java",
    "Ajax",
    "JQuery"
]

Title = [
    "Soap",
    "Mobile",
    "Car",
    "Bike",
    "Motor",
    "Chocolate",
    "Biscuits",
    "Cake",
    "Bottle",
    "Spoon",
    "Banana",
    "Handy",
    "Book",
    "Notebook",
    "Chair",
    "Towel",
    "Door",
    "bag",
    "Suitcase"
]

class Provider(faker.providers.BaseProvider):
    def product_content(self):
        return self.random_element(Content)
    def product_title(self):
        return self.random_element(Title)
    def price(self):
        price = random.uniform(10,100)
        return price

class Command(BaseCommand):
    help = "command Information"

    def handle(self, *args, **kwargs):
        fake = Faker()
        # fake = Faker("nl_NL") #Specify Language

        # print(faker.name())
        fake.add_provider(Provider)
        # print(fake.fake_content())

        for _ in range(15):
            # d = fake.unique.fake_content()
            title = fake.product_title()
            content = fake.product_content()
            price = fake.price()
            Product.objects.create(title = title, content = content, price = price)
        self.stdout.write(self.style.SUCCESS(f" Number of product: { Product.objects.all().count() }"))

        
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'sale_price', 'id']

    def get_something(self, obj):
        id = (obj.id)
        print(id)
        return id
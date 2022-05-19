from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

def validate_title(value):
    qs = Product.objects.filter(title__iexact = value )
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product" )
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all())

# something that can be used with email validation
def validate_title_no_suchvalue(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"Hello is not allowed")
    return value
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    # model = Product
    # should_index = 'is_public'
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public'
    ]
    
    setings = {
        'searchableAttributes': ['title', 'content'],
        'attributesForFaceting': ['user', 'public'],
    }


    # tags = something here
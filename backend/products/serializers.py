from requests import request
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title, validate_title_no_suchvalue, unique_product_title
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source ='user', read_only=True)
    my_user_data = serializers.SerializerMethodField(read_only = True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    url_edit = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field = "pk")
    title = serializers.CharField(validators=[validate_title_no_suchvalue, unique_product_title])
    # email = serializers.EmailField(source='user.email', read_only=True)
    # email = serializers.EmailField(write_only = True)
    class Meta:
        model = Product
        fields = ['owner', 'pk', 'url', 'url_edit', 'title', 'content', 'price', 'sale_price', 'my_discount', 'my_user_data']

    # validationFunction
    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact = value )
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product" )
    #     return value

    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('pop')
    #     return super().update(instance, validated_data)

    def get_my_discount(self, obj):
        # print(obj.id)
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    def get_url_edit(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)

    def get_my_user_data(self, obj):
        return obj.user.username
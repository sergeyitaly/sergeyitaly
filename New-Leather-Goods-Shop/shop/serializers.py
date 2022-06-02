from ast import Delete
from rest_framework import serializers
from .models import Product, Category


#serializer for JSON of Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug','photo')
        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}

#serializer for JSON of product
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Product
        fields = ('id','name', 'slug','category','photo','photo2','brandimage', 'color','price', 'stock', 'available')

#used for creation product be means of API
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','category', 'photo', 'photo2','brandimage', 'color','price', 'stock')
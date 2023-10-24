from rest_framework import serializers

from .models import Order, Product


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source='category', read_only=True)
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('id', 'name', 'description', 'price', 'image_url', 'category_id', 'category_name')


    def get_category_name(self, obj):
        return obj.category.name


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
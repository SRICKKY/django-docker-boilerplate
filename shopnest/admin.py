from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import (
    Cart,
    CartItem,
    Category,
    Order,
    PaymentMethod,
    Product,
    ReviewAndRating,
    ShippingAddress,
    Wishlist,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'image_url_link')
    list_filter = ('category',)
    search_fields = ('name', 'description') 
    

    def image_url_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.image_url, obj.image_url)

    image_url_link.short_description = 'Image URL'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'total_price', 'order_date', 'order_status')
    readonly_fields = ('total_price',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)
admin.site.register(Wishlist)
admin.site.register(PaymentMethod)
admin.site.register(ReviewAndRating)
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Cart, CartItem, Category, Order, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'image_url_link')
    list_filter = ('category',)

    def image_url_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.image_url, obj.image_url)

    image_url_link.short_description = 'Image URL'

admin.site.register(Product, ProductAdmin)


admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)

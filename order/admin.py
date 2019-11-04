from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0

class OrderAdmin(admin.ModelAdmin):

    inlines = [OrderItemInLine]

admin.site.register(Order, OrderAdmin)
#
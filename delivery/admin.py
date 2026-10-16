
from django.contrib import admin
from .models import Restaurant, MenuItem, Order


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "is_open", "created_at")
    search_fields = ("name", "address", "phone")
    list_filter = ("is_open",)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "restaurant",
        "price",
        "is_available",
    )
    search_fields = ("name", "restaurant__name")
    list_filter = ("restaurant", "is_available")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_name",
        "restaurant",
        "total_amount",
        "status",
        "created_at",
    )
    search_fields = ("customer_name", "customer_phone")
    list_filter = ("status", "restaurant", "created_at")

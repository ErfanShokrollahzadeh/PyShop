from django.contrib import admin
from .models import Product, Offer, image, Signup, Login, Comment, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')

class HomeAdmin(admin.ModelAdmin):
    list_display = ('img_url',)

class imageAdmin(admin.ModelAdmin):
    list_display = ('img_url',)

class signupAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

class loginAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

class commentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

class orderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(image, imageAdmin)
admin.site.register(Signup, signupAdmin)
admin.site.register(Login, loginAdmin)
admin.site.register(Comment, commentAdmin)
admin.site.register(Order, orderAdmin)
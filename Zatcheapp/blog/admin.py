from django.contrib import admin
from .models import Blog, Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("name","is_active","is_home","slug")
    list_editable = ("is_active","is_home")
    search_fields = ("name","description")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    search_fields = ("name",)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)



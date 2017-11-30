from django.contrib import admin

# Register your models here.
from .models import Abstract, Author


class AuthorInline(admin.StackedInline):
    model = Author
    extra = 1


class AbstractAdmin(admin.ModelAdmin):
    inlines = [AuthorInline]

admin.site.register(Abstract, AbstractAdmin)
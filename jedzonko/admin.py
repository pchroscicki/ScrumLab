from django.contrib import admin
from jedzonko.models import Recipe


# Register your models here.
admin.site.register(Recipe)
# Register your models here.




# from jedzonko.models import Page
#
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description',)
#     prepopulated_fields = {'slug': ('title',)}
#
# admin.site.register(Page, PageAdmin)
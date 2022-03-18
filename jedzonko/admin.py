from django.contrib import admin
from jedzonko.models import Recipe, Schedule, RecipePlan

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Schedule)
admin.site.register(RecipePlan)
# Register your models here.




# from jedzonko.models import Page
#
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description',)
#     prepopulated_fields = {'slug': ('title',)}
#
# admin.site.register(Page, PageAdmin)
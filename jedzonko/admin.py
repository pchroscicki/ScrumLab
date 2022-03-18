from django.contrib import admin

from jedzonko.models import Recipe, Schedule, DayName, RecipePlan, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Recipe)
admin.site.register(Schedule)
admin.site.register(DayName)
admin.site.register(RecipePlan)
admin.site.register(Page, PageAdmin)
# Register your models here.






from django.contrib import admin
from game.models import Words as Word,WordsSet
class WordAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('title','features','classify','level')
            }),
        )
    list_display = ('title','features','classify','level')

admin.site.register(Word,WordAdmin)


from django.contrib import admin

# Register your models here.
from .models import Paragraph ,Paper,Translated_Paragraph

class PaperAdmin(admin.ModelAdmin):
    class Meta:
        model= Paper

admin.site.register(Paper,PaperAdmin)


class ParagraphAdmin(admin.ModelAdmin):
    class Meta:
        model= Paragraph

admin.site.register(Paragraph,ParagraphAdmin)



class TranslatedAdmin(admin.ModelAdmin):
    class Meta:
        model= Translated_Paragraph

admin.site.register(Translated_Paragraph,TranslatedAdmin)
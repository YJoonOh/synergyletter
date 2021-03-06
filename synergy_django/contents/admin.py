from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Content, Book, Category

# Apply summernote to all TextField in model.
class ContentAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Content, ContentAdmin)
admin.site.register(Book)
admin.site.register(Category)

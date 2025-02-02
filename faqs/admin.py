from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    
    fieldsets = (
        ('FAQ Content', {
            'fields': ('question', 'answer'),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Translations', {
            'fields': (
                ('question_hi', 'answer_hi'),
                ('question_bn', 'answer_bn'),
            ),
            'classes': ('collapse',),
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        })
    )

    class Media:
        css = {
            'all': ('css/custom_admin.css',)
        }

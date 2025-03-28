from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as BaseFlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _

# Определяем нового админа FlatPageAdmin
class FlatPageAdmin(BaseFlatPageAdmin):
    # Определяем структуру полей для админки
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        # Расширенные настройки
        (_('Advanced options'), {
            'classes': ('collapse', ), # сворачиваемый блок
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )

# Перерегистрация FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
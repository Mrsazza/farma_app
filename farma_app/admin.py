from django.contrib import admin
from .models import ItemTable,Unit
from django.db.models import F
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(ItemTable)
class ItemTableAdmin(ImportExportModelAdmin):

    list_display = ('id', 'refno', 'slno', 'stock', 'days_to_exp', 'date')  # table view in admin view

    # shows stock in admin list view

    def get_queryset(self, request):
        qs = super(ItemTableAdmin, self).get_queryset(request)
        qs = qs.annotate(
            stock=(F('amount') - F('consumption'))
        )
        return qs

    def stock(self, obj):
        return obj.stock

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'units')
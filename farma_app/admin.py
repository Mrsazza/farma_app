from django.contrib import admin
from .models import ItemTable
from django.db.models import F


# Register your models here.
@admin.register(ItemTable)
class ItemTableAdmin(admin.ModelAdmin):

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

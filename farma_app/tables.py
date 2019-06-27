import django_tables2 as tables
from .models import ItemTable

class items(tables.Table):
    # makes days_to_exp order able in table
    to_exp = tables.Column(accessor='days_to_exp', verbose_name='Days to expire')

    class Meta:

        model = ItemTable
        fields = ('id', 'refno', 'slno', 'date', 'mata_name', 'manu_name', 'batch_no', 'product', 'agent', 'mfgdate', 'expdate', 'amount', 'consumption', 'stock', 'coa', 'msds', 'moa', 'to_exp', 'edit', 'delete',)
        attrs = {
            'class': 'table  table-bordered table-hover table-striped ',
            'thead': {
                'class': 'thead-light mytable '
            }

        }



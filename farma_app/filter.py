from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .models import ItemTable
from .tables import items

class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = items
    model = ItemTable
    template_name = 'index.html'

    filterset_class = ItemFilter
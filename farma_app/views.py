from django.shortcuts import render, redirect
from .tables import items
from django_tables2 import RequestConfig
from .models import ItemTable
from django.core.paginator import InvalidPage
from django.db.models import F


# Create your views here.
def index(request):
    '''table = items(ItemTable.objects.all())
    RequestConfig(request, paginate={'per_page': 5}).configure(table)
    return render(request, "index.html", {'table': table})'''

    # use a list so django_tables2 sorts in memory
    my_models = list(ItemTable.objects.all().annotate(stock=(F('amount') - F('consumption'))))

    my_models_table = items(my_models)
    RequestConfig(request).configure(my_models_table)

    try:
        page_number = int(request.GET.get('page'))
    except (ValueError, TypeError):
        page_number = 1

    try:
        my_models_table.paginate(page=page_number, per_page=10)
    except InvalidPage:
        my_models_table.paginate(page=1, per_page=10)

    template_vars = {'table': my_models_table}
    return render(request, "index.html", template_vars)

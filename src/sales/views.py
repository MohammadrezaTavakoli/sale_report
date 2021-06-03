from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Sale
from .forms import SalesSearchForm
from .utils import get_customer_name, get_saleman_name, get_chart

from reports.forms import ReportForm

import pandas as pd


@login_required
def home_view(request):
    sales_data_frame = None
    positions_data_frame = None
    merged_data_frame = None
    main_data_frame = None
    chart = None
    no_data = None

    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm()
    
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_by = request.POST.get('results_by')
        
        query_set = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)

        if query_set:
            sales_data_frame = pd.DataFrame(query_set.values())
            sales_data_frame['customer_id'] = sales_data_frame['customer_id'].apply(get_customer_name) 
            sales_data_frame['saleman_id'] = sales_data_frame['saleman_id'].apply(get_saleman_name)
            sales_data_frame['created'] = sales_data_frame['created'].apply(lambda x: x.strftime('%Y-%m-%d'))
            sales_data_frame.rename({'id':'sale_id', 'customer_id': 'customer', 'saleman_id': 'saleman'}, axis=1, inplace=True)

            positions_data = []
            for query in query_set:
                for pos in query.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price,
                        'sale_id': query.id,    
                    }
                    positions_data.append(obj)
            
            positions_data_frame = pd.DataFrame(positions_data)
            merged_data_frame = pd.merge(sales_data_frame, positions_data_frame, on='sale_id')
            main_data_frame = merged_data_frame.groupby('transaction_id', as_index=False)['price'].agg('sum')
            chart = get_chart(chart_type, sales_data_frame, results_by)
            
            sales_data_frame = sales_data_frame.to_html()
            positions_data_frame = positions_data_frame.to_html()
            merged_data_frame = merged_data_frame.to_html()
            main_data_frame = main_data_frame.to_html()
        else:
            no_data = 'No Data Available.'

    context = {
        'search_form': search_form,
        'report_form': report_form,
        'sales_data_frame': sales_data_frame,
        'positions_data_frame': positions_data_frame,
        'merged_data_frame': merged_data_frame,
        'main_data_frame': main_data_frame,
        'chart': chart,
        'no_data': no_data,
    }

    return render(request, 'sales/home.html', context)


class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'sales/main.html'


class SaleDetailView(LoginRequiredMixin, DetailView):
    model = Sale
    template_name = 'sales/detail.html'
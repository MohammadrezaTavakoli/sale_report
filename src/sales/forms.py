from django import forms


chart_choices = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)
result_choices = (
    ('#1', 'transaction'),
    ('#2', 'sales date'),
)

class SalesSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices=chart_choices)
    results_by = forms.ChoiceField(choices=result_choices)
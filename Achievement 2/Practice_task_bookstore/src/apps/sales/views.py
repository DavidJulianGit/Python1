from django.shortcuts import render

# Create your views here.
def sales_view(request):
    return render(request, 'sales/sales_view.html')
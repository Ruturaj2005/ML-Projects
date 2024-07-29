from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")
def Accounts(request):
    return render(request,"accounts.html")
def Mutual_funds(request):
    return render(request,"mutual_funds.html")
def real_estate(request):
    return render(request,"real_estate.html")
def stock_market(request):
    return render(request,"stock_market.html")
def gold_investment(request):
    return render(request,"gold_investment.html")

# Create your views here.

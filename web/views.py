from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User ,income ,Expense , Token
from datetime import datetime
# Create your views here.
@csrf_exempt
def submit_income(request):
    """user submit an income"""
    this_token = request.POST['token']
    print (this_token)
    this_user = Token.objects.get(token = this_token).user
    print(this_user)
    if 'date' not in request.POST:
        date = datetime.now()
    income.objects.create(user=this_user, amount=request.POST['Amount'],
        text = request.POST['Text'],date = date)
        
    return JsonResponse({
        'status' : 'ok', 
    }, encoder= JSONEncoder)
   

@csrf_exempt
def submit_expense(request):
    """user submit an expense"""
    this_token = request.POST['token']
    print(this_token)
    this_user =Token.objects.get(token = this_token).user
    print(this_user)
    
    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user=this_user, amount=request.POST['Amount'],
        text = request.POST['Text'],date = date)
        
    return JsonResponse({
        'status' : 'ok', 
    }, encoder= JSONEncoder)

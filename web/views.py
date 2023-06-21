from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User , Token , income ,Expense
from datetime import datetime
# Create your views here.
@csrf_exempt
def submit_expense(request):
    """user submit an expense"""
    if request.method == 'POST':
         this_Token = request.POST['token']
    this_user = User.objects.filter(Token__Token = this_Token).get()
    now = datetime.now()
    Expense.objects.create(User=this_user, amount=request.post['amount'],
            text = request.post['text'],date =now)
    print ("I'm in submit expense")
    if request.method == 'POST':
           print(request.POST)
    return JsonResponse({
        'status' : 'ok', 
    }, encoder= JSONEncoder)


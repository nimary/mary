from django.contrib import admin
from .models import Expense, income ,Token
# Register your models here.
admin.site.register(Expense)
admin.site.register(income)
admin.site.register(Token)
from django.contrib import admin

from .models import Transaction

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['emp_name', 'emp_code', 'punch_time']

    class Meta:
        ordering = ('id',)
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.urls import reverse
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder

import datetime
import json
import time

from .models import Transaction
from .forms import TransactionForm

# Create your views here.
def home(request):
    return render(request, 'home.html', context={})


class TransactionView(View):
    form_class = TransactionForm
    initial = {}
    template_name = 'transactions.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        transactions = Transaction.objects.all().order_by('id')
        return render(request, self.template_name, {"form": form, "transactions": transactions})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('transactions'))



class TransactionStreamView(View):
    def transaction_stream(self):
        initial_data = ""

        while True:
            data = json.dumps(
                list(Transaction.objects.all().order_by('id').values('emp_name', 'emp_code', 'punch_time')),
                cls=DjangoJSONEncoder
                )
            if initial_data != data:
                yield f"\ndata: {data}\n\n"
                initial_data = data
            time.sleep(1)

    def get(self, request):
        response = StreamingHttpResponse(self.transaction_stream())
        response['Content-Type'] = 'text/event-stream'
        return response

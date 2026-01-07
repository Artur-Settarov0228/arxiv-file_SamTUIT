from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View

class Talabalar(View):
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request=HttpRequest, template_name="ftot/index.html")
    

class AddTalaba(View):
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request=request, template_name="ftot/talaba_qoshish.html")
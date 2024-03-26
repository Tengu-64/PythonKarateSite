from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .forms import show_form
from .models import *
# Create your views here.
def index(request):
   return render(request, 'karate/index.html')

def belt(request):
   blt = Belt.objects.order_by('pk')
   return  render(request, 'karate/belt.html', {'info': blt})

def exam(request):
   blt = Belt.objects.order_by('pk')
   ab_ex = Info.objects.filter()
   return render(request, 'karate/exam.html', {'href': blt, 'info': ab_ex})

def power(request): #
   nf = Info.objects.all()
   return render(request, 'karate/power.html', {'ofp': nf})



def dictionary(request):
   words = Dictionary.objects.all()
   #pw = Info.odject.all()
   return render(request, 'karate/dictionary.html', {'words': words,}) #'pw': pw})

def concrete_exam(request, exam_id):
   blt = Belt.objects.filter(id=exam_id)
   i = Info.objects.filter(info_id=exam_id)

   context = {
      'blt': blt,
      'info': i,
      'ex_id': exam_id
   }
   return render(request, 'karate/exam_id.html', context=context)

def PageNotFound(request, exception):
   return render(request, 'karate/404.html', status=404)

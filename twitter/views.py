from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import userinput
from . apicall import getdata
from chartjs.views.lines import BaseLineChartView


# Create your views here.


def home(request):
    # hall = 'trump'
    # random = getdata(hall)
    # print(random)
    word = "word of the home"
    return render(request, 'home.html', {"word": word})

def analyse(request):
    user_input = userinput(request.GET or None)
    if request.GET and user_input.is_valid():
        input_hastag = user_input.cleaned_data['q']
        # print(input_hastag)
        data = getdata(input_hastag)
        positive = data['Positive']
        neutral = data['Neutral']
        negative = data['Negative']
        print(data['Positive'])
        print(data)
        return render(request, "results.html", {'data': data, 'positive': positive, 'neutral': neutral, 'negative': negative})
    return render(request, "home.html", {'input_hastag': user_input})

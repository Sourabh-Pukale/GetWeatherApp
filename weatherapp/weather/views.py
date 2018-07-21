import requests
from django.shortcuts import render
from .models import city
from .forms import CityForm
def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=741a7add12e09858f1ac23d0abbd6277'

    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()
    form=CityForm()

    data=[]

    cities= city.objects.all()
    for dp in cities:
        r = requests.get(url.format(dp.name)).json()

        info = {
            'city':dp.name,
            'temp':r['main']['temp'],
            'desp':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']

        }
        data.append(info)

    context={'data':data, 'form':form}
    return render(request,'weather.html',context)
from django.shortcuts import render
import requests
from datetime import date
# Create your views here.
def index(request):
    if request.method == 'POST':
        location = request.POST['location']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=4d85c767ba8677e79356365ac4617881'.format(location)
        response = requests.get(url)
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        data = response.json()
        final_data = {
            "country_code": str(data['sys']['country']),
            "coordinate":str(data['coord']['lon'])+' '+str(data['coord']['lat']),
            "weather": str(data['weather'][0]['main']),
            "temperature":str(round(data['main']['temp']-273.15,2))+ ' C',
            "humidity":str(data['main']['humidity'])+ ' %',
            "wind_speed":str(data['wind']['speed'])+ ' km/h',
            "pressure":str(data['main']['pressure'])+' hPa'
        }
    else:
        location = ''
        final_data = ''
    return render(request,'index.html',{'data':final_data,'location':location,'time':d2})
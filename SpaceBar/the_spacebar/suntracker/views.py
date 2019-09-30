from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from datetime import datetime
import time

def suntracker(request):
        #using the ip-api to get latitude and longitude
    info = requests.get("http://ip-api.com/json/?fields=lat,lon")
    print(info.status_code)
    latLon = BeautifulSoup(info.content, 'html.parser')
    location = str(latLon)

    #modify the latLon string to be something we can pass the sunrise-sunset api
    location = location.strip('{')
    location = location.strip('}')
    location = location.replace('"', "")
    location = location.replace(':', "=")
    location = location.replace(",", "&")
    location = location[:13] + 'ng' + location[15:]

    #now that latitude and longitude are in the correct form we pass them to the api
    suncalc = requests.get("https://api.sunrise-sunset.org/json?" + location + "&formatted=0")

    #printing out the sunrise and sunset at the ip addresses location
    soup = BeautifulSoup(suncalc.content, 'html.parser')
    soupStr = str(soup)
    sunStart = soupStr.find('sunrise') + 10
    sunEnd = sunStart + 19
    sunrise = soupStr[sunStart:sunEnd]
    datetimeObject1 = datetime.strptime(sunrise, '%Y-%m-%dT%H:%M:%S')
    localSunrise = datetime_from_utc_to_local(datetimeObject1).strftime("%I:%M %p")
    #The sunset could be at 9:00 or 10:00 which gives the string an extra character, this will be a comma which will get removed by this line
    sunrise = sunrise.replace(",", "")
    setStart = soupStr.find('sunset') + 9
    setEnd = setStart + 19
    sunset = soupStr[setStart:setEnd]
    #convert the string to a datetime object so we can convert for the correct timezone then back to a string
    datetimeObject2 = datetime.strptime(sunset, '%Y-%m-%dT%H:%M:%S')
    localSunset = datetime_from_utc_to_local(datetimeObject2).strftime("%I:%M %p")
    #The sunset could be at 9:00 or 10:00 which gives the string an extra character, this will be a comma which will get removed by this line
    localSunset = localSunset.replace(",", "")
    context = {'sunrise': localSunrise, 'sunset': localSunset,}
    return render(request, "suntracker/sunriseSunset.html", context)

#code that converts the times from UTC to the local timezone
def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

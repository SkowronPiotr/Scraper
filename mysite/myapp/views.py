from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.


def scrape(request):
    page = requests.get('http://www.facebook.com')
    soup = BeautifulSoup(page.text, 'html.parser')

    link_address = []

    for link in soup.find_all('a'):
        link_address.append(link.get('href'))

    return render(request, 'myapp/result.html', {'link_address': link_address})

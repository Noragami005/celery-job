from celery import shared_task
from bs4 import BeautifulSoup
import requests
from .models import ReverseProxy


@shared_task
def scrape_proxies():
    url = 'https://geonode.com/free-proxy-list'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    proxy_table = soup.find('table', class_='proxy__t')
    proxies = proxy_table.find_all('tr')[1:]

    for proxy_row in proxies:
        proxy_data = proxy_row.find_all('td')
        ip = proxy_data[0].text
        port = proxy_data[1].text
        protocol = proxy_data[3].text
        country = proxy_data[4].text
        uptime = proxy_data[7].text

        ReverseProxy.objects.create(ip=ip, port=port, protocol=protocol, country=country, uptime=uptime)


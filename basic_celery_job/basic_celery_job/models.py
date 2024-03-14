from django.db import models


class ReverseProxy(models.Model):
    proxy_ip = models.CharField(max_length=100)
    port = models.IntegerField()
    protocol = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    uptime = models.CharField(max_length=100)

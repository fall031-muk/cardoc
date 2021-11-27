import urllib.request
import json
import django
import os

from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from tires.models import Tire

@transaction.atomic
def DataUploader():
    
    trimid = ["5000", "9000", "11000", "15000"]
    
    for i in trimid:
        if not Tire.objects.filter(trimid=int(i)).exists():
            
            url = "https://dev.mycar.cardoc.co.kr/v1/trim/" + i

            response    = urllib.request.urlopen(url)
            json_str    = response.read().decode("utf-8")
            json_object = json.loads(json_str)
            data        = json_object
            frontTire   = data['spec']['driving']['frontTire']['value']
            rearTire    = data['spec']['driving']['rearTire']['value']


            Tire.objects.create(
                trimid             = int(i),
                front_width        = int(frontTire.split('/')[0]),
                front_aspect_ratio = int(frontTire.split('/')[1].split('R')[0]),
                front_wheel_size   = int(frontTire.split('/')[1].split('R')[1]),
                rear_width         = int(rearTire.split('/')[0]),
                rear_aspect_ratio  = int(rearTire.split('/')[1].split('R')[0]),
                rear_wheel_size    = int(rearTire.split('/')[1].split('R')[1]),
            )

DataUploader()
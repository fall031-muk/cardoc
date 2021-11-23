from django.db import models

class Tire(models.Model):

    trimid             = models.IntegerField()
    front_width        = models.IntegerField()
    front_aspect_ratio = models.IntegerField()
    front_wheel_size   = models.IntegerField()
    rear_width         = models.IntegerField()
    rear_aspect_ratio  = models.IntegerField()
    rear_wheel_size    = models.IntegerField()

    class Meta:
        db_table = 'tires'
    
class User_Tire(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    tire = models.ForeignKey('Tire', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_tires'
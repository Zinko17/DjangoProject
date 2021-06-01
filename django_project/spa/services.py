from user_profile.models import Profile
import datetime


def profileCreate(profile_data,instance):
    name = profile_data.get('name')
    age = profile_data.get('age')
    email = profile_data.get('email')
    Profile.objects.create(name=name,age=age,email=email,user=instance)


def checkExpired(certificates):
    for certificate in certificates:
        date_expired = certificate.date_expired
        today = datetime.date.today()
        if today > date_expired:
            certificate.status = 'dead'
            certificate.save()
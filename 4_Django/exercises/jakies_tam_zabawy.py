import sys
from django.core.wsgi import get_wsgi_application
import os
current_dir = os.getcwd()
sys.path.append(current_dir )
settings = "coderslab.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
application = get_wsgi_application()


from exercises.models import Band, Album

b1 = Band.objects.get(pk=1)
b2 = Band.objects.get(pk=2)
b3 = Band.objects.get(pk=3)
#
# a1 = Album.objects.create(name='aaabbbb', year=-1, rating=1, band=b1)
# a2 = Album.objects.create(name='bbbbcccc', year=-1, rating=1,band=b1)
# a3 = Album.objects.create(name='aaabccccdddbbb', year=-1, rating=1, band=b2)
# a4 = Album.objects.create(name='Abrakadabra', year=-1, rating=1,band=b3)

for album in b1.album_set.all():
    print(album.name)



from django.core.management.base import BaseCommand
from vp.models import Location
from viceprice import settings
import unicodecsv as csv

class Command(BaseCommand):

    # Write Facebook data from file
    def update_facebook(self):
        with open('facebook_data.csv', 'rb') as datafile:
            reader = csv.reader(datafile)
            for row in reader:
                location_id = int(row[0])
                location = Location.objects.get(id = location_id)
                location.facebookId = row[3]
                location.save()


    def handle(self, *args, **options):
        self.update_facebook()
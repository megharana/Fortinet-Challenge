from django.core.management.base import BaseCommand, CommandError
from bhojanalayas.models import Address, Details
import csv

# from float import float


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('../../../../restaurantsa9126b3.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            count_own = 0
            for row in csv_reader:
                if count_own > 0:

                    entry = Details(
                        resturant_id=row[0],
                        rest_name=row[1],
                        cuisines=row[2],
                        avg_cost_ofTwo=int(row[3]),
                        currency=row[4],
                        has_table_booking=row[5],
                        has_online_delivery=row[6],
                        aggregate_rating=float(row[7]),
                        rating_color=row[8],
                        rating_text=row[9],
                        votes=int(row[10]))
                    entry.save()
                count_own += 1
                print(count_own)
            print(count_own)
        with open('../../../../restaurant_addc9a1430.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            count_own = 0
            for row in csv_reader:
                if count_own > 0:

                    entry = Address(
                        country_code=row[1],
                        city=row[2],
                        address=row[3],
                        locality=row[4],
                        locality_verbose=row[5],
                        longitude=float(row[6]),
                        latitude=float(row[7]),
                        rest_id_id=row[0])
                    entry.save()
                count_own += 1
                print(count_own)
            print(count_own)

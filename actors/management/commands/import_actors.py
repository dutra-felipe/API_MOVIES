from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo csv',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row.get('name')
                birthday_str = row.get('birthday')
                nationality = row.get('nationality', 'Unknown') 

                if not name or not birthday_str:
                    self.stdout.write(self.style.WARNING(f'Skipping row with missing name or birthday: {row}'))
                    continue

                try:
                    birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
                except ValueError:
                    self.stdout.write(self.style.WARNING(f'Invalid date format for {name}: {birthday_str}'))
                    continue

                self.stdout.write(self.style.NOTICE(f'Importing {name}'))

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )
        
        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO!'))

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

from vestgo_api.models import School, CustomUser


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        school = School.objects.create(
            name='Escola Exemplo',
            address='Rua das Flores, 123',
            city='São Paulo',
            state='SP',
            country='Brasil',
        )
        self.stdout.write(self.style.SUCCESS(f'Created school: {school.__str__()}'))

        user = CustomUser.objects.create_superuser(
            email='admin@example.com',
            password='senha123',
            name='Admin User',
            school=school,
        )
        self.stdout.write(self.style.SUCCESS(f'Created user: {user.__str__()}'))

        # adding the other models here

        self.stdout.write(self.style.SUCCESS('Seeding completed successfully!'))

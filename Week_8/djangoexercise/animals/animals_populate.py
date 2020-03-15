import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animals.settings')

import django
django.setup()
from info.models import Family

animals = ['Mammal', 'Reptile', 'Insect', 'Arachnid', 'Amphibian', 'Marsupial']


print('Populating animal table')
for animal in animals:
    a = Family(name=animal)
    a.save()
print('done')









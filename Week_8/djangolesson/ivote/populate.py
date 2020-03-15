import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ivote.settings')

import django
django.setup()
from app.models import Party

parties = ['Likud', 'Blue&White', 'Emet', 'Shas', 'JointList', 'Yemina', 'YB', 'Otzma']


print('Populating Party table')
for party in parties:
    p = Party(name=party)
    p.save()
print('done')
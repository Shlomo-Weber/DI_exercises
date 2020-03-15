import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ivote.settings')

import django
django.setup()
from app.models import Party, Affiliation

affiliations = {'Likud': 'Right', 'Blue&White': 'Center', 'Emet': 'Left', 'Shas':'Right', 'JointList': 'Left', 'Yemina': 'Right', 'YB':'Right', 'Otzma': 'Right'}

heads = {'Likud': 'Bibi Netanyahu', 'Blue&White': 'Benny Gantz', 'Emet': 'Amir Peretz', 'Shas':'Aryeh Dery', 'JointList': 'Aimann Oudeh', 'Yemina': 'Naftali Bennet', 'YB':'Avigdor Lieberman', 'Otzma': 'Itamar Ben-Gvir'}


for party, head in heads.items():
    p = Party.objects.get(name=party)
    # aff, created = Affiliation.objects.get_or_create(name=affiliation)
    # aff.save()
    p.head = head
    p.save()

print('Done')
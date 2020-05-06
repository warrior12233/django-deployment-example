import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from appTwo.models import AccessRecord,Webpage,Topic,User
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News']

def add_topics():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        top = add_topics()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webp = Webpage.objects.get_or_create(topic = top,url = fake_url,name = fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name = webp,date = fake_date)[0]

def populate_users(N=5):
    for entry in range(N):
        temp_user = User.objects.get_or_create(first_name = fakegen.name().split()[0],last_name = fakegen.name().split()[1],email = fakegen.email())[0]

if __name__ == '__main__':
    print('Populating scripts')
    populate_users(20)
    print("Populating complete")
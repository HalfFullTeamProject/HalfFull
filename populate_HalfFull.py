import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Half_Full_Project.settings')

import django
django.setup()
from HalfFull.models import Pub

def populate():
	pubs_dict = [{'name': 'City Merchant', 'picture': 'static/images/city_merchant.jpg', 'drinks': 4, 'atmosphere': 4, 'service':5},
				 {'name': 'The Horse Shoe', 'picture': 'static/images/horse_shoe.jpg', 'drinks': 4, 'atmosphere': 4, 'service': 4},
				 {'name': 'James Tassie', 'picture': 'static/images/james_tassie.jpg', 'drinks': 4, 'atmosphere': 3, 'service': 4},
				 {'name': 'The Ben Nevis', 'picture': 'static/images/ben_nevis.jpg', 'drinks': 4, 'atmosphere': 4, 'service': 5}]
			
	for pub in pubs_dict:
		p = add_pub(pub['name'], pub['picture'], pub['drinks'], pub['atmosphere'], pub['service'])
		
	for p in Pub.objects.all():
		print(f'- {p}')
	
def add_pub(name, picture, drinks=0, atmosphere=0, service=0):
	p = Pub.objects.get_or_create(name=name, drinks=drinks, atmosphere=atmosphere, service=service, picture=picture)[0]
	p.drinks = drinks
	p.atmosphere = atmosphere
	p.service = service
	p.picture = picture
	p.save()
	return p
	
	
if __name__ == '__main__':
	print('Starting HalfFull population script...')
	populate()
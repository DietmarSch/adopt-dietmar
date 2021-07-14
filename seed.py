"""Seed file to make sample data for users db."""

from models import Pet, db
from app import app


db.drop_all()
db.create_all()

Pet.query.delete()


p1=Pet(name='Bubi', species='purcubine', age = 2, photo_url= 'https://www.zoomontana.org/images/img_7oG4iZhLWRyAxceYYZHoMe/north-american-porcupine.jpg?fit=outside&w=1600&dpr=1', notes = 'always hungry')
p2=Pet(name='John', species='dog', age = 3, photo_url = 'https://media.istockphoto.com/photos/puppy-running-at-the-park-picture-id1184654849?b=1&k=6&m=1184654849&s=170667a&w=0&h=WIPur4xVwMeiPYxiWegtulUWu6AQrva5QtFQUk_2otQ=', notes = 'always crazy')
p3=Pet(name='Caesar', species='dog', age = 2, photo_url='https://cdn.pixabay.com/photo/2015/06/08/15/02/pug-801826__340.jpg', notes = 'always crazy')
p4=Pet(name='Anthea', species='cat', age = 1, photo_url='https://www.thesprucepets.com/thmb/NIAWlO8KAWhnLq5V8E-35tAwanc=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/portrait-of-tortoiseshell-cat-sitting-by-door-at-home-654708285-57dac1e53df78c9cceaf7c8f.jpg', notes = 'always crazy')

db.session.add_all([p1,p2,p3,p4])
db.session.commit()


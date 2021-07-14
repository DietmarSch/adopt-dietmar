
from flask import Flask, render_template,request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
#from models import db, connect_db, User, Post, Tag, PostTag
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'Dietmar123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_pet_list():
    pets = Pet.query.all()
    return render_template('pet_list.html', pets = pets)

@app.route('/available')
def show_available_pets():
    pets = Pet.query.filter(Pet.available==True)
    return render_template('pet_list.html', pets = pets)

@app.route('/not_available')
def show_not_available_pets():
    pets = Pet.query.filter(Pet.available==False)
    return render_template('pet_list.html', pets = pets)

@app.route('/add', methods = ['GET', 'POST'])
def add_new_pet():
    form=AddPetForm()
    
    if form.validate_on_submit():
        pet=Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data, age = form.age.data, notes = form.notes.data)
        db.session.add(pet)
        db.session.commit()
        flash (f"{form.name.data} added.")
        return redirect('/')
    else:
        return render_template('add.html', form=form)

@app.route('/pets/<int:pet_id>')
def show_pet(pet_id):
    pet=Pet.query.get_or_404(pet_id)
    return render_template('details.html', pet=pet)



@app.route('/pets/<int:pet_id>/edit', methods = ['GET', 'POST'])
def edit_pet(pet_id):
    pet=Pet.query.get_or_404(pet_id)
    form=EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url=form.photo_url.data
        pet.notes=form.notes.data
        pet.available=form.available.data
        db.session.commit()
        flash(f'{pet.name} edited.')
        return redirect('/')
    else:
        return render_template("edit.html", form=form, pet=pet)
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(80) , unique = True , nullable = False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name}  - {self.description}"

@app.route('/')
def index():
    return "Hellow!"

@app.route('/drink')
def drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name , 'description':drink.description}
        output.append(drink_data)
    return {"drinks":output}   

@app.route('/drink/<id>')
def drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name":drink.name , "description":drink.description}

@app.route('/drink' ,  methods = ['POST'])
def add_drink():
    drink = Drink(name = request.json['name'] , description = request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}

@app.route('/drink/<id>' , methods = ['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"Error":"not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"meassage":"Delte Successfully"}


if __name__ == "__main__":
    app.run(debug=True)
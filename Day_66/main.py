from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy(app)


## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random/")
def random_cafe():
    
    cafes = db.session.query(Cafe).all()
    print(cafes)
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())
    

## HTTP GET - Read Record
@app.route("/all")
def all_cafes():
    cafes_list = []
    cafes = db.session.query(Cafe).all()
    for cafe in cafes:
        cafes_list.append(cafe.to_dict())
    return jsonify(cafes=cafes_list)

@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("loc"),
        has_sockets = bool(request.form.get("has_socket")),
        has_toilet = bool(request.form.get("has_toilet")),
        has_wifi = bool(request.form.get("has_wifi")),
        can_take_calls = bool(request.form.get("can_take_calls")),
        seats = request.form.get("seats"),
        coffee_price = request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    new_price = request.args.get("new_price")
    print(new_price)
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully update price of the cafe"}), 200
    else:
        return jsonify(error={"not found": "sorry a cafe with that id is not found in your database"}), 404

@app.route("/delete-cafe/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    user_api_key = request.args.get("user_api_key")
    api_key = "TopSecretAPIKey"
    if user_api_key == api_key:
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from our database"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in our database"}), 404
    else: 
        return jsonify(error={"Forbidden": "Sorry, that's not allowed, make sure you have the correct api_key"}), 403

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

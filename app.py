from hmac import compare_digest
from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

jwt = JWTManager(app)
db = SQLAlchemy(app)
ma = Marshmallow()
ma.init_app(db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    full_name = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, default='password')

    # NOTE: In a real application make sure to properly hash and salt passwords
    def check_password(self, password):
        return compare_digest(password, self.password)


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "username", "full_name")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

# Register a callback that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

# @app.post("api/v1/create")
# def create():
#     name = request.json["name"]
#     email = request.json["email"]
#     password = request.json["password"]

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/api/v1/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(username=username).one_or_none()
    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401

    # Notice that we are passing in the actual sqlalchemy user object here
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)


@app.route("/api/v2/login", methods=["POST"])
def loginV2():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).one_or_none()
    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401

    # Notice that we are passing in the actual sqlalchemy user object here
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/api/v1/who_am_i", methods=["GET"])
@jwt_required()
def who_am_i():
    # Access the identity of the current user with get_jwt_identity
    current_user = User.query.get(get_jwt_identity())
    return jsonify(
        id=current_user.id,
        full_name=current_user.full_name,
        username=current_user.username,
    ), 200


@app.route("/public/api/v1/users", methods=["GET"])
def user_list():
    users = User.query.all()
    all_users = users_schema.dump(users) 
    return jsonify(all_users)



if __name__ == "__main__":
    db.create_all()
    db.session.add(User(full_name="Bruce Wayne", username="batman"))
    db.session.add(User(full_name="Ann Takamaki", username="panther"))
    db.session.add(User(full_name="Jester Lavore", username="little_sapphire"))
    db.session.commit()
    print("Create db")

    app.run()
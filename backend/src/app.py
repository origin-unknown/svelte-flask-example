from flask import (
	Flask, 
	jsonify
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import ( 
	DeclarativeBase, 
	Mapped 
)
from flask_marshmallow import Marshmallow


class Base(DeclarativeBase):
	pass

app = Flask(__name__, 
	static_url_path=''
)
app.config.from_mapping(
	SQLALCHEMY_DATABASE_URI='sqlite:///example.db'
)
db = SQLAlchemy(app, model_class=Base)
ma = Marshmallow(app)

class User(db.Model):
	id:Mapped[int] = db.mapped_column(db.Integer, primary_key=True)
	name:Mapped[str] = db.mapped_column(db.String, nullable=False, unique=True)
	desc:Mapped[str] = db.mapped_column(db.String, nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = User

with app.app_context():
	db.drop_all()
	db.create_all()
	users = [
		User(
			name=f'user-{i}', 
			desc=f'Description of the user {i}.'
		) for i in range(1, 11)
	]
	db.session.add_all(users)
	db.session.commit()


@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/data')
def data():
	users = db.session.execute(db.select(User)).scalars()
	users_schema = UserSchema(many=True)
	return users_schema.jsonify(users)

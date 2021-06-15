# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
#
# # SQLAlchemy is used as ORM for the data storage of registrants:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports_registry.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# # Pycharm does not detect .Column etc.
# class Registrant(db.Model):
#     email = db.Column(db.String(150), primary_key=True)
#     first_name = db.Column(db.String(100), unique=False, nullable=False)
#     last_name = db.Column(db.String(100), unique=False, nullable=False)
#     sports = db.Column(db.String(500), unique=False, nullable=False)
#
#     def __repr__(self):
#         return f'*{self.email}, {self.first_name} {self.last_name}, {self.sports}*'
#

# ---------
# how to query for 1 element?

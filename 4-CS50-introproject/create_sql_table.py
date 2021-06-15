# create a db/table suiting the web applications needs:
# pip install Flask-SQLAlchemy

from application import db

# creating a new Table:
db.create_all()

# delete old Table:
# db.drop_all()

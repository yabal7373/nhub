from project import db

from project.models import Intern

db.drop_all()

db.create_all()

db.session.commit()
from app import db

class Profile(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80), unique=True)
  last_name = db.Column(db.String(80), unique=True)
  gender = db.Column(db.String(10), unique=True)
  image = db.Column(db.String(2), unique=True)
  
  
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def __repr__(self):
    return '<Profile %r %r>' % (self.first_name, self.last_name)
  
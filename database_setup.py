from app import db
db.create_all()

admin = User('admin', 'admin@example.com')
guest = User('guest', 'guest@example.com')
# add and commit the new users to the database
db.session.add(admin)
db.session.add(guest)
db.session.commit()
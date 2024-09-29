from config import db

class Contact(db.Model):
    # Key we are going to use to index this and it must be unique for every single entery inside the databaase
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    # Takes all of the different fields we have on our object and converts it into a python dictionary 
    def to_json(self):
        return{
            "id": self.id, 
            "firstName": self.first_name,
            "lastName": self.last_name, 
            "email": self.email
        }
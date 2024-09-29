from flask import request, jsonify
from config import app, db
from models import Contact

# Gets the necessary information to make a contact and converts them to json  
@app.route("/contacts", methods=["GET"])
def get_contacts(): 
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

# Adds a contact for the first time 
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email: 
        return (
            jsonify({"message": "You must include a first name, last name, and email"}), 
            400, 
        )

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e: 
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201

# Updates information of exisitng contacts 
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found :( )"}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated successfully!!"}), 200


# Deletes a user 
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found :( )"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!!"}), 200


if __name__ == "__main__":
    # When we are about to start the application this will get the context of the application 
    with app.app_context(): 
        # Will create all of the different models we have defined in our database 
        db.create_all()
    
    app.run(debug = True)
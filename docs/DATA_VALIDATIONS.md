# Data Validations

Lets say a request is coming from the client and we need to make sure it contains the right information.

We have to use conditionals to make the validations, if we want to validate the request body we have to retrive it first and then add the condition, like this:
```py
body = request.get_json()
if 'username' not in body:
    raise APIException('You need to specify the username', status_code=400)
```

- Its a good practice to raise exeptions because it will stop the code execution.
- Its a good practice to return 400 because that way the client knows it was his mistake and not ours.

### Here is a full example of a POST request to add a new person into a database:

```py
@app.route('/person', methods=['POST'])
def handle_person():

    # First we get the payload json
    body = request.get_json()

    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'username' not in body:
        raise APIException('You need to specify the username', status_code=400)
    if 'email' not in body:
        raise APIException('You need to specify the email', status_code=400)

    # at this point, all data has been validated, we can proceed to inster into the bd
    user1 = Person(username=body['username'], email=body['email'])
    db.session.add(user1)
    db.session.commit()
    return "ok", 200
```


#  AirBnB clone - The console

##  Contents:

- Project Description

- Command Interpreter Description

	* How to start it
	* Commands and their usage
	* How to use it
	* examples

- Unittests


##  Project Description

Airbnb Clone is the main project of the second trimester at Holberton School.Main aim is development of an entire web application that simulates the behavior of the Airbnb platform. Starting from the console or command interpreter, to manipulate data without a visual interface, like in a Shell (perfect for development and debugging), followed by the construction of a website (the front-end) that shows the final product to everybody: static and dynamic, once it's finished what follows is the connection with the database or files that store data (data = objects). And last but not least, the creation of an API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).


##  Command Interpreter Description

* How to start it

	Follow the instructions to get a copy of the program and run in your local machine:
	- Clone the following repository.
		> (https://github.com/Zineb49/AirBnB_clone.git)
	- Run the program
		> `./console.py`

* Commands and their usage

| Command | Usage | Example | Description
|--|--|--|--|
| create | `create <class  name>` | create BaseModel | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. |
| show | `show <class  name>  <id>` | show BaseModel 1234-1234-1234 | Prints the string representation of an instance based on the class name and id. |
| destroy | `destroy <class  name>  <id>`| destroy BaseModel 1234-1234-1234 | Deletes an instance based on the class name and id (save the change into the JSON file). |
| all | `all <class  name> or all` | all BaseModel | Prints all string representation of all instances based or not on the class name. |
| update | `update <class  name>  <id>  <attribute  name> "<attribute  value>"` | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). |
| all() | `<class  name>.all()` | User.all() | Retrieve all instances of a class |
| count() | `<class  name>.count()` | User.count() | Retrieve the number of instances of a class |
| show() | `<class  name>.show(<id>)` | User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68") | retrieve an instance based on its ID |
| destroy() | `<class  name>.destroy(<id>)` | User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")| Destroy an instance based on his ID |
| update() | `<class  name>.update(<id>, <attribute  name>, <attribute  value>)` | User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89) | Update an instance based on his ID |
| update() with dictionary | `<class  name>.update(<id>, <dictionary  representation>)` | User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89}) | Update an instance based on his ID with a dictionary |


##  Built with...

- Visual Studio Code - Coding and structuring.
- python 3.4.3

###  [BaseModel](./models/base_model.py)

* Write a class BaseModel that defines all common attributes/methods for other classes

###  [File storage](./models/engine/file_storage.py)

* Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances

###  [Console](./console.py)

* Write a program called console.py that contains the entry point of the command interpreter:

	- create
	- show
	- destroy
	- all
	- update

###  [First User](./models/user.py)

* Write a class User that inherits from BaseModel

###  More classes

* Classes that inherit from BaseModel:

	- [State](./models/state.py)

	- [City](./models/city.py)

	- [Amenity](./models/amenity.py)

	- [Place](./models/place.py)

	- [Review](./models/review.py)

## Unittests

All the tests should be executed at the root of the project by using the following command:

`python3 -m unittest discover tests`
thank you.

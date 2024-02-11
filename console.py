#!/usr/bin/python3
<<<<<<< HEAD
"""
BaseModel class which defines all common attributes/methods for other classes
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from re import search


class HBNBCommand(cmd.Cmd):
    """
        Summary: class that defines the interpreter command:
    """
    prompt = "(hbnb) "
    list_classes = ["BaseModel", "User", "Place", "State", "City",
                    "Amenity", "Review"]

    doc_header = "Documented commands (type help <topic>):"
    ruler = '='

    def do_EOF(self, line):
        "Exit the program with Ctrl+D"
        return True

    def do_quit(slef, line):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything
            If the line is empty, emptyline() is called,
            the method was modified because the default
            implementation runs the previous command again
            and we want it to pass not executing anything.
        """
        pass

    def do_create(self, arg):
        """ func to create a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        args_list = arg.split(" ")
        if not args_list[0]:
            print("** class name missing **")
        elif args_list[0] in HBNBCommand.list_classes:
            new_instance = globals()[args_list[0]]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ func to print the string representation of an instance
            based on the class name and id
        """
        args_list = arg.split(" ")
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to
            create id_object with the form Classname.id that is the key that
            we will ask if is in Storge and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """print the string representation based on the
                   class name and the ID
                """
                print(storage.all()[id_object])

    def do_destroy(self, arg):
        """ fucn to delete an instance based on the class name and id
            (save the change into the JSON file).
        """
        args_list = arg.split(" ")
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to
            create id_object with the form Classname.id that is the key that
            we will ask if is in Storge and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """deletes an instance for the dictionary
                """
                storage.all().pop(id_object)
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not
            on the class name
        """
        element_list = []
        args_list = arg.split()
        if len(args_list) == 0:
            for key, value in storage.all().items():
                element_list.append(str(value))
            print(element_list)
        elif args_list[0] in HBNBCommand.list_classes:
            for key, value in storage.all().items():
                if value.__class__.__name__ == args_list[0]:
                    element_list.append(str(value))
            print(element_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
           updating attribute  (save the change into the JSON file).
        """
        args_list = shlex.split(arg[:])
        arg = arg.split(" ")
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) < 3:
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            "if the instance of the class name doesn’t exist for the id"
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                dog = r"\d+\.\d+"
                id_object = "{}.{}".format(args_list[0], args_list[1])
                name_attr = args_list[2]
                value = args_list[3]
                """ Only “simple” arguments can be updated: string,
                    integer and float. """
                if '"' in arg[3]:
                    pass
                elif search(dog, arg[3]):
                    value = float(value)
                elif arg[3].isdigit():
                    value = int(value)
                setattr(storage.all()[id_object], name_attr, value)
                storage.all()[id_object].save()

    def do_count(self, arg):
        """Count the number of instances of a class"""
        count = 0
        for key, value in storage.all().items():
            if key.split(".")[0] == arg:
                count += 1
        print(count)

    def default(self, arg):
        """Method called on an input line when the command prefix is
        not recognized. If this method is not overridden, it prints an
        error message and returns. """
        # BaseModel show("440f0fd5-502f-4f46-bc09-6b2c1b156fa7")
        args_list = arg.split(".", 1)
        if args_list[0] in HBNBCommand.list_classes:  # BaseModel
            method = args_list[1].split("(")  # show
            # retrieve all instances of a class by using: <class name>.all()
            if method[0] == "all":
                return self.do_all(args_list[0])
            # retrieve the number of instances of a class: <class name>.count()
            elif method[0] == "count":
                return self.do_count(args_list[0])
            elif method[0] == "show":
                id_show = args_list[1].split('"')
                args_show = "{} {}".format(args_list[0], id_show[1])
                return self.do_show(args_show)
            elif method[0] == "destroy":
                id_destroy = args_list[1].split('"')
                args_destroy = "{} {}".format(args_list[0], id_destroy[1])
                return self.do_destroy(args_destroy)
            elif method[0] == "update":
                part1 = method[1].replace(")", "")
                check_dict = part1[:].split(", ")
                if check_dict[1][0] is "{":
                    class_id = check_dict[0].replace('"', "")
                    dog = r"\d+\.\d+"
                    for i in range(1, len(check_dict)):
                        dict_parse = check_dict[i].replace("{", "", 1)
                        dict_parse = dict_parse.replace("}", "")
                        dict_parse = dict_parse.replace("'", "")
                        dict_parse = dict_parse.split(": ")
                        if '"' in dict_parse[1]:
                            pass
                        elif search(dog, dict_parse[1]):
                            dict_parse[1] = float(dict_parse[1])
                        elif dict_parse[1].isdigit():
                            dict_parse[1] = int(dict_parse[1])
                        args_update = "{} {} {} {}".format(args_list[0],
                                                           class_id,
                                                           dict_parse[0],
                                                           dict_parse[1])
                        self.do_update(args_update)
                else:
                    part2 = part1.replace('"', "", 4)
                    part3 = part2.split(", ")
                    args_update = "{} {} {} {}".format(args_list[0], part3[0],
                                                       part3[1], part3[2])
                    return self.do_update(args_update)
=======
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()
>>>>>>> My first commit


if __name__ == "__main__":
    HBNBCommand().cmdloop()

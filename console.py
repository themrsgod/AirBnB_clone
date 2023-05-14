#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import sys
import inspect
from shlex import split


class HBNBCommand(cmd.Cmd):
    """
    Represents the command-line interface of the program

    This class defines a command-line interface for a program that manages objects of different classes.
    """

    # Define the prompt string for the command-line interface
    prompt = "(hbnb) "

    def default(self, some_args):
        """
        This method is called when a command is not recognized.

        This method lists all available classes in the program, allowing the user to choose one to operate on.
        """
        self.our_classes = []
        self.classes()

    def do_create(self, some_arg):
        """
        Creates a new instance of BaseModel and saves it (to the JSON file) with a new id.
        Ex: create BaseModel
        """
        argument = process_argument(some_arg)
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in self.our_classes:
            print("** class doesn't exist **")
        else:
            storage.save()
            # eval extracts the object type from string then creates the object and gets the id.
            the_id = eval(argument[0])().id
            print(the_id)

    def do_show(self, some_arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Ex: show BaseModel 1234-1234-1234
        """
        argument = process_argument(some_arg)
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in self.our_classes:
            print("** class doesn't exist **")
        elif len(argument) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(argument[0], argument[1]) not in storage.all():
            print("** no instance found **")
        else:
            stored_items = storage.all()
            index = "{}.{}".format(argument[0], argument[1])
            item_at_id = stored_items[index]
            print(item_at_id)

    def do_destroy(self, some_arg):
        """
        Deletes an instance based on the class name and id (saves the change into the JSON file).
        Ex: destroy BaseModel 1234-1234-1234
        """
        argument = process_argument(some_arg)
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in self.our_classes:
            print("** class doesn't exist **")
        elif len(argument) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(argument[0], argument[1]) not in storage.all():
            print("** no instance found **")
        else:
            stored_items = storage.all()
            index = "{}.{}".format(argument[0], argument[1])
            item_at_id = stored_items[index]
            del (item_at_id)
            storage.save()

    def do_all(self, some_arg):
        """
        Prints all string representations of all instances based or not on the class name.
        Ex: all BaseModel or all
        """
        argument = process_argument(some_arg)
        if len(argument) == 0:
            print("** class name missing **")
        else:
            list_of_instances = []
            for item in storage.all().values():
                list_of_instances.append(item.__str__())
            print(list_of_instances)

    def do_update(self, some_arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Ex: update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        argument = process_argument(some_arg)
        object_dictionary = storage.all()

        if len(argument) == 0:
            print("** class name missing **")
            return False
        if argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argument) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argument[0], argument[1]) not in object_dictionary.keys():
            print("** no instance found **")
            return False
        if len(argument) == 2:
            print("** attribute name missing **")
            return False
        if len(argument) == 3:
            try:
                type(eval(argument[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        elif type(eval(argument[2])) == dict:
            obj = object_dictionary["{}.{}".format(argument[0], argument[1])]
            for k, v in eval(argument[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_quit(self, some_arg):
        """
        Exits the program
        """
        return True

    def do_EOF(self, some_arg):
        """
        Exits the program
        """
        self.do_quit()

    def emptyline(self):
        """
        Do nothing when the user inputs an empty line
        """
        pass

    def classes(self):
        """
        This method lists all available classes in the program.
        """
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj):
                self.our_classes.append(obj.__name__)
                print(obj.__name__)


def process_argument(some_arg):
    """
    Parses the user input and returns the arguments as a list
    """
    curly_braces = re.search(r"\{(.*?)\}", some_arg)
    brackets = re.search(r"\[(.*?)\]", some_arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(some_arg)]
        else:
            lexer = split(some_arg[:brackets.span()[0]])
            result = [i.strip(",") for i in lexer]
            result.append(brackets.group())
            return result
    else:
        lexer = split(some_arg[:curly_braces.span()[0]])
        result = [i.strip(",") for i in lexer]
        result.append(curly_braces.group())
        return result


if __name__ == '__main__':
    HBNBCommand().cmdloop()

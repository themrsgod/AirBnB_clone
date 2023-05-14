#!/usr/bin/python3

import cmd
import sys
import inspect
from shlex import split


class HBNBCommand(cmd.Cmd):
    """
    contains the entry point of the command interpreter
    """

    prompt = "(hbnb) "

    def classes(self):
        self.our_classes.clear()
        # get all modules in current package
        current_module = sys.modules[__name__]
        # loop over the modules
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj):  # check if its a class
                self.our_classes.append(str(obj))
                # save to out classes list

    def default(self, some_args):
        self.our_classes = []
        self.classes()

    def do_create(self, some_arg):
        """
        create: Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
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
        show: Prints the string representation of an instance 
        based on the class name and id
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
        destroy: Deletes an instance based on the class name and id 
        (save the change into the JSON file)
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
        all: Prints all string representation of all instances 
        based or not on the class name.
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
        'Quit command to exit the program'
        return True

    def do_EOF(self, some_arg):
        'EOF command to quit the program'
        self.do_quit()

    def emptyline(self):
        # use pass to not repeat anything
        pass


def process_argument(some_arg):
    args = split(some_arg)
    return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()

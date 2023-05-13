#!/usr/bin/python3

import cmd, sys, inspect
from shlex import split

def process_argument(some_arg):
    args = split(some_arg)
    return args

class HBNBCommand(cmd.Cmd):
    """
    contains the entry point of the command interpreter
    """

    prompt = "(hbnb) "

    def classes(self):
        self.our_classes.clear()
        current_module = sys.modules[__name__] # get all modules in current package
        for name, obj in inspect.getmembers(sys.modules[__name__]): # loop over the modules
            if inspect.isclass(obj): # check if its a class
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
            the_id = eval(argument[0])().id # eval extracts the object type from string then creates the object and gets the id.
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
        elif "{}.{}".format(argument[0],argument[1]) not in storage.all():
            print("** no instance found **")
        else:
            stored_items = storage.all()
            index =  "{}.{}".format(argument[0],argument[1])
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
        elif "{}.{}".format(argument[0],argument[1]) not in storage.all():
            print("** no instance found **")
        else:
            stored_items = storage.all()
            index =  "{}.{}".format(argument[0],argument[1])
            item_at_id = stored_items[index]
            del(item_at_id)
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

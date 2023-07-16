#!/usr/bin/python3
""" Console Module """

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel}

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id
        """
        if len(arg) == 0:
            print('** class name missing **')
            return
        l = arg.split()
        if len(l) == 1:
            if arg in self.classes.keys():
                print(self.classes[arg]().id)
                self.classes[arg]().save()
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
        if len(arg) == 0:
            print('** class name missing **')
            return
        l = arg.split()
        if len(l) == 1:
            print('** instance id missing **')
        elif l[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(l) > 1:
            if "{}.{}".format(l[0], l[1]) not in storage.all():
                print('** no instance found **')
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name
            and id (save the change into the JSON file)
        """
        if len(l) == 0:
            print("** class name missing **")
        l = parse(arg)
        if l[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(l[0], l[1]) not in storage.all().keys():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(l[0], l[1])]
            storage.save()

    def do_all(self, arg):
        """
            Prints all string representation of all instances based
            or not on the class name
        """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        """
            Updates an instance based on the class name
            and id by adding or updating attribute
            (save the change into the JSON file)
        """
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

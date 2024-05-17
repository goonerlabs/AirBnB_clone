#!/usr/bin/python3

"""" Entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand """
    prompt = '(hbnb) '
    __classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.__classes[arg]()
        print(new_instance.id)
        new_instance.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        k = "{}.{}".format(args[0], args[1])
        if k not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[k])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        k = "{}.{}".format(args[0], args[1])
        if k not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[k]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(v) for v in storage.all().values()])
            return
        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        print([
            str(v) for v in storage.all().values()
            if type(v) is HBNBCommand.__classes[arg]
            ])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        k = "{}.{}".format(args[0], args[1])
        if k not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        _, _, a, v = args
        if "\"" in v:
            v = v.replace("\"", "")
        try:
            if "." in v:
                v = float(v)
            else:
                v = int(v)
        except ValueError:
            pass
        setattr(storage.all()[k], a, v)
        storage.all()[k].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

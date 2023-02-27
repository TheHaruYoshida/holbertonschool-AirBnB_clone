#!/usr/bin/python3
"""Console"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "
    commands = {'User': "User", 'BaseModel': "BaseModel"}

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command"""
        print()
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args= line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.commands.keys():
            print("** class doesn't exist **")
        else:
            new = eval(HBNBCommand.commands[args[0]])()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints the str representation of an instance
        based on the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.commands.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.commands.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = line.split()
        if not line:
            for key, value in models.storage.all().items():
                print(value)
        elif args[0] not in HBNBCommand.commands.keys():
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if args[0] in key:
                    print(value)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.commands.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.all()[key].save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

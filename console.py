#!/usr/bin/python3
"""Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def quit(self, arg):
        """Exit the program"""
        return True

    def EOF(self, arg):
        """EOF command"""
        print()
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
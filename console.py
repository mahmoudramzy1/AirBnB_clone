#!/usr/bin/python3
"""console module"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """console class"""
    prompt = '(hbnb)'
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]    
    def do_EOF(self, arg):
        """exit console"""
        return True
    
    def do_quit(self, arg):
        """exit the console"""
        return True
    
    def emptyline(self):
        pass

    def do_create(self, arg):
        """create new object"""
        if len(arg) == 0:
             print("** class name missing **")
        if (arg):
            args = arg.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                new = eval(args[0])()
                new.save()
                print(new.id)

    def do_show(self, arg):
        """show the object with id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """prints all instances"""
        if len(arg) == 0:
            lo = []
            for o in storage.all().values():
                lo.append(str(o))
            print(lo)
        else:
            args = arg.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                print([str(o) for key, o in storage.all().items() if key.split(".")[0] == args[0]])
    
    def do_update(self, arg):
        """update an instance"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) <= 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return
        if len(args) <= 2:
            print("** attribute name missing **")
            return
        if len(args) <= 3:
            print("** value missing **")
            return
        content = storage.all()['{}.{}'.format(args[0], args[1])]
        setattr(content, args[2], eval(args[3]))

        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

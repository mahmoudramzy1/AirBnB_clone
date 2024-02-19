#!/usr/bin/python3
"""console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """console class"""
    prompt = '(hbnb)'
    
    def do_EOF(self, arg):
        """exit console"""
        return True
    
    def do_quit(self, arg):
        """exit the console"""
        return True
    
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

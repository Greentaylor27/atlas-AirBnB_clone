#!/usr/bin/python3
"""
Console for Airbnb clone
"""
import cmd
from models.base_model import BaseModel
import json
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Attributes and methods for Airbnb console
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Called when empty line is passed
        Useed to override command to keep from repeating previous command
        """
        pass

    def default(self, line: str):
        self.line = line.strip()

    def input_checker(self, buffer):
        """
        Checks to see if input is empty or valid

        Args:
            buffer (str): User input if there is any

        Returns:
            _type_: _description_
        """
        if self.line:
            return self.line
        else:
            pass

    # Exit command
    def do_EOF(self, arg):
        """
        Command that exits console interface

        Returns:
            True
        """
        print("Have a pleasant day")
        return True

    # Quit command
    def do_quit(self, arg):
        """
        Command that quits console interface

        Returns:
            True
        """
        print("Have a pleasant day")
        return True

    # Create command
    def do_create(self, arg):
        """
        Command that creates a new instance of the class

        Returns:
            A new instance of the class and saves it to a JSON
        """
        buffer = arg.split()
        if not buffer:
            print("** class name missing **")
            return
        buffer = buffer[0]
        if buffer == "BaseModel": 
            """
            need a "class doesn't exist" case -- (meaning that we 
            have to have some way of iterating through all
            existing classes -- I'm thinking something like 
            my classes function in FileStorage and how that allows
            me to do reload properly)
            """
            instance = BaseModel()
            storage.new(instance)  #saves instance to filestorage dictionary
            storage.save() #converts that filestorage dictionary to json in 'file.json'
            print(f"{instance.id}")
        else:
            print("** class doesn't exist **")
        
    #prints string representation of an instance using class name and id
    def do_show(self, arg):
        """
        #prints string representation of an instance using 
        class name and id
        """
        buffer = arg.split()
        if not buffer:
            print("** class name missing **")
            return
        if buffer[0] == "BaseModel":
            storage.save()
            storage.reload()
            objects = storage.all()
            class_and_id = f"{buffer[0]}.{buffer[1]}"
            if class_and_id in objects.keys():
                print(objects[class_and_id])
            else:
                print("** instance id missing")
        else:
            print("** class doesn't exist **")

    #Deletes an instance using class and id
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name 
        and id (save the change into the JSON file)
        """
        buffer = arg.split()
        if not buffer:
            print("** class name missing **")
            return
        if buffer[0] == "BaseModel":
            storage.save()
            storage.reload()
            objects = storage.all()
            class_and_id = f"{buffer[0]}.{buffer[1]}"
            if class_and_id in objects.keys():
                del objects[class_and_id]
                storage.save() 
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

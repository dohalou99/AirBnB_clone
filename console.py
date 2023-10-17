import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb) "
    clList = ['BaseModel', 'User', 'Amenity',
              'Place', 'City', 'State', 'Review']

    lsClss = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            agm = cnd[1].split(')')
            hbLsCls = HBNBCommand.clList
            hbLc = HBNBCommand.lsClss
            if cls[0] in hbLsCls and cnd[0] in hbLc:
                arg = cnd[0] + ' ' + cls[0] + ' ' + agm[0]
        return arg

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_count(self, nmClass):
        """counts number of instances of a class"""
        cnt = 0
        for k, v in storage.all().items():
            clss = k.split('.')
            if clss[0] == nmClass:
                cnt = cnt + 1
        print(cnt)

    def do_create(self, mdtyoe):
        """ Creates an instance according to a given class """

        if not mdtyoe:
            print("** class name missing **")
        elif mdtyoe not in HBNBCommand.clList:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[mdtyoe]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ Shows string representation of an instance passed """

        if not arg:
            print("** class name missing **")
            return

        agm = arg.split(' ')

        if agm[0] not in HBNBCommand.clList:
            print("** class doesn't exist **")
        elif len(agm) == 1:
            print("** instance id missing **")
        else:
            allOb = storage.all()
            for k, v in allOb.items():
                nmObj = v.__class__.__name__
                idObj = v.id
                if nmObj == agm[0] and idObj == agm[1].strip('"'):
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance passed """

        if not arg:
            print("** class name missing **")
            return

        agm = arg.split(' ')

        if agm[0] not in HBNBCommand.clList:
            print("** class doesn't exist **")
        elif len(agm) == 1:
            print("** instance id missing **")
        else:
            allOb = storage.all()
            for k, v in allOb.items():
                nmObj = v.__class__.__name__
                idObj = v.id
                if nmObj == agm[0] and idObj == agm[1].strip('"'):
                    del v
                    del storage._FileStorage__objects[k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints string represention of all instances of a given class """

        if not arg:
            print("** class name missing **")
            return

        agm = arg.split(' ')

        if agm[0] not in HBNBCommand.clList:
            print("** class doesn't exist **")
        else:
            allOb = storage.all()
            instLs = []
            for k, v in allOb.items():
                nmObj = v.__class__.__name__
                if nmObj == agm[0]:
                    instLs += [v.__str__()]
            print(instLs)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        agm = shlex.split(a)

        if agm[0] not in HBNBCommand.clList:
            print("** class doesn't exist **")
        elif len(agm) == 1:
            print("** instance id missing **")
        else:
            allOb = storage.all()
            for k, objc in allOb.items():
                nmObj = objc.__class__.__name__
                idObj = objc.id
                if nmObj == agm[0] and idObj == agm[1].strip('"'):
                    if len(agm) == 2:
                        print("** attribute name missing **")
                    elif len(agm) == 3:
                        print("** v missing **")
                    else:
                        setattr(objc, agm[2], agm[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

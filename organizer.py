import os
from formats import *
from zipfile import ZipFile
from os.path import expanduser
from operations_logger import OperationsLogger
import tempfile
import datetime
import shutil

home = expanduser("~")
logger = OperationsLogger()
e = Extensions()

class Organizer(object):

    def __init__(self):
        
        # Parent directory where dirs and files are going to be organized in.
        self.parent_organizer_dir = f"{home}/Downloads"
        
        # From current starting path_name, set deepness as 0. Increments when getting deeper through directories.
        self.deepness = 0
        self.path_name = ""
        return

    def organize(self, path_name):
        """Organizes every dir and file from path_name to a parent_organizer_dir (directory).

        Args:
            path_name (str): directory were to perform the decluttering.

        """
        self.path_name = path_name
        parent = path_name
        os.chdir(path_name) # move os to indicated path_name
        for f in os.listdir(path_name):
            # If f is a file
            if os.path.isfile("{}/{}".format(os.getcwd(), f)) and f != "organizer.py":

                print("file", f)
                # organizer directory path
                directory = e.dir_for(f)
                print("directory '", directory, "'")

                # if directory don't exist
                if not self.dir_exists(directory):
                    print("El directorio no existe.")
                    self.create_dir(directory)  # create it

                # move file to organizer directory path
                self.move_to(path_name, directory, f)

            # If it is a path
            else:
                try:
                    # if f is a "organizer directory path" and the deepnes is not zero.
                    if f not in e.types or self.deepness > 0:
                        self.deepness += 1          # increase deepnesresult_msg              self.organize(parent+"/"+f) # uses recursion to organize sub-directory
                        os.chdir(path_name)         # move os to original path_name
                        os.rmdir(parent+"/"+f)      # removes sub-directory
                        self.deepness -= 1          # decreases deepness again
                except OSError:
                    pass
        return

    def dir_exists(self, directory):
        """Verifies directory existence.

        Args:
            directory (str): directory to verify existence.

        Returns:
            bool: wether directory exists.
        """
        try:
            l = os.listdir("{}/{}".format(self.parent_organizer_dir,directory))
            return len(l) > 0
        except:
            return False

    def create_dir(self, path):
        """Creates directory.

        Args:
            path (str): to create directory.
        """
        try:
            new_dir_path = "{}/{}".format(self.parent_organizer_dir, path)  # Creates path's name string.
            os.makedirs(new_dir_path)                                       # Creates directory with path's name.
        except PermissionError:
            logger.log_operation_result(False, path, "", "PermissionError", "used by another process")  # Log error.
        return

    def delete_dir(self, path):
        """Deletes specified directory.

        Args:
            path (str): directory to delete.
        """
        try:
            os.rmdir(path)                                      # Deletes diretory.
            logger.log_operation_result(True, path, "Delete")   # Logs successful operation on path.
        except PermissionError:
            logger.log_operation_result(False, path, "", "PermissionError", "used by another process") # Logs error.
        except OSError:
            logger.log_operation_result(False, path, "", "OSError", "directory is not empty")          # Logs error.
        return
    
    def move_to(self, cur_directory_parent:str, path:str, f: str):
        """Moves a file or directory from one place to another.

        Args:
            cur_directory_parent (str): parent directory which contains organizers.
            path (str): organizer path name.
            f (str): file name.
        """
        old_path = "{}/{}".format(cur_directory_parent, f)
        new_path = "{}/{}/{}".format(self.parent_organizer_dir, path, f)
        try:
            os.rename(old_path, new_path)                                                           # Moves file.
            logger.log_operation_result(True, f"{old_path} to {new_path}", "Moved")                 # Logs successful operation on paths.
            return
        except FileExistsError:
            os.remove("{}/{}".format(cur_directory_parent, f))
            logger.log_operation_result(False, f"{old_path} to {new_path}", "", "FileExistsError", "File wasn't replaced.")
            return

    def __repr__(self):
        return f'Organizing {self.path_name}'

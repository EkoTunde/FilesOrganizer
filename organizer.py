import os
from formats import *
from zipfile import ZipFile

e = Extensions()

class Organizer(object):

    def __init__(self):
        
        # Parent directory where dirs and files are going to be organized in.
        self.parent_organizer_dir = "C:/Users/juan_/Downloads"
        
        # From current starting path_name, set deepness as 0. Increments when getting deeper through directories.
        self.deepness = 0
        return

    def organize(self, path_name):
        """Organizes every dir and file from path_name to a parent_organizer_dir (directory).

        Args:
            path_name (str): directory were
        """
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
                # if f is a "organizer directory path" and the deepnes is not zero.
                if f not in e.types or self.deepness > 0:
                    self.deepness += 1          # increase deepness
                    self.organize(parent+"/"+f) # uses recursion to organize sub-directory
                    os.chdir(path_name)         # move os to original path_name
                    os.rmdir(parent+"/"+f)      # removes sub-directory
                    self.deepness -= 1          # decreases deepness again
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
        new_dir_path = "{}/{}".format(self.parent_organizer_dir, path)
        os.makedirs(new_dir_path)
        return

    def delete_dir(self, path):
        """Deletes specified directory.

        Args:
            path (str): directory to delete.
        """
        os.rmdir(path)
        return
    
    def move_to(self, cur_directory_parent:str, path:str, f: str):
        """Moves a file or directory from one place to another.

        Args:
            cur_directory_parent (str): parent directory which contains organizers.
            path (str): organizer path name.
            f (str): file name.
        """
        try:
            old_path = "{}/{}".format(cur_directory_parent, f)
            new_path = "{}/{}/{}".format(self.parent_organizer_dir, path, f)
            os.rename(old_path, new_path)
            return
        except FileExistsError:
            os.remove("{}/{}".format(cur_directory_parent, f))
            return


organizer = Organizer()

desktop_path = "C:/Users/juan_/Desktop"

organizer.organize(desktop_path)

downloads_path= "C:/Users/juan_/Downloads"

organizer.organize(downloads_path)
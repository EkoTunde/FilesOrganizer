import os
from os.path import expanduser
import tempfile
import datetime
import shutil
from operations_logger import OperationsLogger

home = expanduser("~")
logger = OperationsLogger()

class Cleaner(object):

    def __init__(self):
        self.logs_dir_path = home+"/cleaner_error_logs.txt"
        return

    def clean(self):
        """Performs the cleaning operations
        """
        logger.log_title()              # Logs new session created in logs file
        temp = tempfile.gettempdir()    # Gets current's user temp directory.
        os.chdir(temp)                  # Move os to indicated temp_path_name
        for f in os.listdir(temp):
            path_to_f = temp + "\\" + f
            self.delete(path_to_f, f)   # Delete the file/directory.
        return

    def delete(self, path:any="", f:any=""):
        """Deletes files and directories in the current user's temp files directory.

        Args:
            path (str): Generally a str representing the path to a file or directory in temp files directory.
            f (str): File's name and extension.
        """
        try:
            os.remove(path) if os.path.isfile(f) else os.rmdir(path)                    # Depending on if it's a file or directory, is removed with the correct method.
            logger.log_operation_result(success=True, path=path, operation = "Deleted") # Logs operation's success
        except PermissionError:
            logger.log_operation_result(False, path, "", "PermissionError", "used by another process") # Logs error.
        except OSError:
            logger.log_operation_result(False, path, "", "OSError", "directory is not empty")   # Logs error.
            self.del_not_empty_dir(path)                                                        # Performs a tree directories removal.
        return

    def del_not_empty_dir(self, path:str):
        """Deletes a non empty directory which needs a "tree removal", deleting files and sub-directories recursively.

        Args:
            path (str): the parent directory path to delete.
        """
        try:
            shutil.rmtree(path)                                 # Perform removal.
            logger.log_operation_result(True, path, "Deleted")  # Logs operation's success
        except PermissionError:
            logger.log_operation_result(False, path, "", "PermissionError", "used by another process (dir)")    # Logs error.


    def __repr__(self):
        return f"Cleaner points to {self.logs_dir_path}"
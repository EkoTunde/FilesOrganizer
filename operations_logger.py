import datetime
from os.path import expanduser

class OperationsLogger(object):

    def __init__(self):
        home = expanduser("~")
        self.logs_dir_path = home+"/clean_and_declutter_logs.txt"
        return
    
    def log_title(self):
        """Appends a "new session" title-text line in the file used to register logging results.
        """
        with open(self.logs_dir_path,'a') as log_file:  # Opens (and creates if not exists) the logs file.
            title = "| NEW SESSION |".center(71,"-")    # Defines a title, "just ---| NEW SESSION |---" alike.
            title = f"\n\n{title}\n"                    # Adds to linebreaks at the beginning and one extra at the end.
            log_file.write(title)                       # Write the file with the new session title.
        return


    def log_operation_result(self, success:bool, path:str, operation:str="", error:str="", msg:str=""):
        """Performs the log's writing in the logs file.

        Args:
            success (bool): if the log corresponds to a successful or failed operation.
            path (str): of the file/directory which the deleting operation attempt was intended to.
            msg (str, optional): the operation performed. Defaults to "".
            error (str, optional): the exception's name. Defaults to "".
            msg (str, optional): the exception's message. Defaults to "".
        """
        with open(self.logs_dir_path,'a') as log_file:                                      # Opens the logs file.
            now = str(datetime.datetime.now())                                              # Declares new string containing currents date and time.
            result_state = "SUCCESS" if success else "FAILURE"                              # Declares new string indicating if result was successful or not.
            result_msg = f"{error}: {msg} for path" if len(error) != 0 else f"{operation}"   # Composes the error message dependening on "error" and "msg" parameters.
            final_msg = f"{now} - {result_state} > {result_msg} '{path}'.\n"                 # Composes the final message to be logged.
            log_file.write(final_msg)                                                       # Appends the text to the end of the file.
        return

    def __repr__(self):
        return f"Logger pointing to {self.logs_dir_path}"
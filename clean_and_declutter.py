from cleaner import Cleaner
from organizer import Organizer
from os.path import expanduser

home = expanduser("~")

cleaner = Cleaner()
cleaner.clean()

desktop_path = f"{home}/Desktop"
downloads_path= f"{home}/Downloads"

organizer = Organizer()
organizer.organize(desktop_path)
organizer.organize(downloads_path)
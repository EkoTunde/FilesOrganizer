# -*- coding: utf-8 -*-

"""
From: https://www.computerhope.com/issues/ch001789.htm
"""

class ExtensionNotFoundError(Exception):
    pass

class Extensions(object):

    types = ["media","other","programming","text"]

    extensions = {
        '.aif':	'media/audio',	 # AIF audio file
        '.cda':	'media/audio',	 # CD audio track file
        '.mid':	'media/audio',	 # MIDI audio file
        '.midi': 'media/audio',	 # MIDI audio file
        '.mp3':	'media/audio',	 # MP3 audio file
        '.mpa':	'media/audio',	 # MPEG-2 audio file
        '.ogg':	'media/audio',	 # Ogg Vorbis audio file
        '.wav':	'media/audio',	 # WAV file
        '.wma':	'media/audio',	 # WMA audio file
        '.wpl':	'media/audio',	 # Windows Media Player playlist

        '.7z':	'other/compressed',	 # 7-Zip compressed file
        '.arj':	'other/compressed',	 # ARJ compressed file
        '.deb':	'other/compressed',	 # Debian software package file
        '.pkg':	'other/compressed',	 # Package file
        '.rar':	'other/compressed',	 # RAR file
        '.rpm':	'other/compressed',	 # Red Hat Package Manager
        '.tar.gz': 'other/compressed',	 # Tarball compressed file
        '.z': 'other/compressed',	 # Z compressed file
        '.zip':	'other/compressed',	 # Zip compressed file

        '.bin':	'other/disc',	 # Binary disc image
        '.dmg':	'other/disc',	 # macOS X disk image
        '.iso':	'other/disc',	 # ISO disc image
        '.toast': 'other/disc',	 # Toast disc image
        '.vcd':	'other/disc',	 # Virtual CD

        '.csv':	'programming/database',	 # Comma separated value file
        '.dat':	'programming/database',	 # Data file
        '.db':	'programming/database',	 # Database file
        '.dbf':	'programming/database',	 # Database file
        '.log':	'programming/database',	 # Log file
        '.mdb':	'programming/database',	 # Microsoft Access database file
        '.sav':	'programming/database',	 # Save file (e'.g'., game save file)
        '.sql':	'programming/database',	 # SQL database file
        '.tar':	'programming/database',	 # Linux / Unix tarball file archive
        '.xml':	'programming/database',	 # XML file

        '.email': 'other/email',	 # Outlook Express e-mail message file'.
        '.eml':	'other/email', # E-mail message file from multiple e-mail clients, including Gmail'.
        '.emlx': 'other/email',	 # Apple Mail e-mail file'.
        '.msg':	'other/email',	 # Microsoft Outlook e-mail message file'.
        '.oft':	'other/email',	 # Microsoft Outlook e-mail template file'.
        '.ost':	'other/email', # Microsoft Outlook offline e-mail storage file'.
        '.pst':	'other/email',	 # Microsoft Outlook e-mail storage file'.
        '.vcf':	'other/email',	 # E-mail contact file'.

        '.fnt':    'other/fonts',  # Windows font file
        '.fon':    'other/fonts',  # Generic font file
        '.otf':    'other/fonts',  # Open type font file
        '.ttf':    'other/fonts',  # TrueType font file

        '.apk':	'other/executable',	 # Android package file
        '.bat':	'other/executable',	 # Batch file
        '.bin':	'other/executable',	 # Binary file
        '.com':	'other/executable',	 # MS-DOS command file
        '.exe':	'other/executable',	 # Executable file
        '.gadget': 'other/executable',	 # Windows gadget
        '.jar':	'other/executable',	 # Java Archive file
        '.msi':	'other/executable',	 # Windows installer package
        '.wsf':	'other/executable',	 # Windows Script File

        '.fnt':	'media/image',	 # Windows font file
        '.fon':	'media/image',	 # Generic font file
        '.otf':	'media/image',	 # Open type font file
        '.ttf':	'media/image',	 # TrueType font file
        '.ai':	'media/image',	 # Adobe Illustrator file
        '.bmp':	'media/image',	 # Bitmap image
        '.gif':	'media/image',	 # GIF image
        '.ico':	'media/image',	 # Icon file
        '.jpeg': 'media/image',	 # JPEG image
        '.jpg':	'media/image',	 # JPEG image
        '.png':	'media/image',	 # PNG image
        '.ps':	'media/image',	 # PostScript file
        '.psd':	'media/image',	 # PSD image
        '.svg':	'media/image',	 # Scalable Vector Graphics file
        '.tif':	'media/image',	 # TIFF image
        '.tiff': 'media/image',	 # TIFF image

        '.c': 'programming/c',        # C and C++ source code file
        '.cgi': 'programming/pearl',      # .pl - Perl script file.
        '.pl': 'programming/pearl',           # Perl script file.
        '.class': 'programming/java',    # Java class file
        '.cpp': 'programming/c',      # C++ source code file
        '.cs': 'programming/c',       # Visual C# source code file
        '.h': 'programming/c',        # C, C++, and Objective-C header file
        '.java': 'programming/java',     # Java Source code file
        '.kt': 'programming/kotlin',     # Java Source code file
        '.php': 'programming/php',      # PHP script file.
        '.py': 'programming/python',       # Python script file.
        '.sh': 'programming/bash_shell',       # Bash shell script
        '.swift': 'programming/swift',    # Swift source code file
        '.vb': 'programming/visual_basic',      # Visual Basic file

        '.asp':	'other/internet',	 # Active Server Page file
        '.aspx': 'other/internet',	 # Active Server Page file
        '.cer':	'other/internet',	 # Internet security certificate
        '.cfm':	'other/internet',	 # ColdFusion Markup file
        '.cgi':	'other/internet',	 # Perl script file
        '.pl':	'other/internet',	 # Perl script file
        '.css':	'other/internet',	 # Cascading Style Sheet file
        '.htm':	'other/internet',	 # HTML file
        '.html': 'other/internet',	 # HTML file
        '.js':	'other/internet',	 # JavaScript file
        '.jsp':	'other/internet',	 # Java Server Page file
        '.part': 'other/internet',	 # Partially downloaded file
        '.php':	'other/internet',	 # PHP file
        '.rss':	'other/internet',	 # RSS file
        '.xhtml': 'other/internet',	 # XHTML file

        '.key':	'text/office/presentation',	 # Keynote presentation
        '.odp':	'text/office/presentation',	 # OpenOffice Impress presentation file
        '.pps':	'text/office/presentation',	 # PowerPoint slide show
        '.ppt':	'text/office/presentation',	 # PowerPoint presentation
        '.pptx': 'text/office/presentation',	 # PowerPoint Open XML presentation

        '.ods': 'text/office/spreadsheet',	 # OpenOffice Calc spreadsheet file
        '.xls': 'text/office/spreadsheet',	 # Microsoft Excel file
        '.xlsm': 'text/office/spreadsheet',	 # Microsoft Excel file with macros
        '.xlsx': 'text/office/spreadsheet',	 # Microsoft Excel Open XML spreadsheet file

        '.bak': 'text/other/system', # Backup file
        '.cab': 'text/other/system', # Windows Cabinet file
        '.cfg': 'text/other/system', # Configuration file
        '.cpl': 'text/other/system', # Windows Control panel file
        '.cur': 'text/other/system', # Windows cursor file
        '.dll': 'text/other/system', # DLL file
        '.dmp': 'text/other/system', # Dump file
        '.drv': 'text/other/system', # Device driver file
        '.icns': 'text/other/system', # macOS X icon resource file
        '.ico': 'text/other/system', # Icon file
        '.ini': 'text/other/system', # Initialization file
        '.lnk': 'text/other/system', # Windows shortcut file
        '.msi': 'text/other/system', # Windows installer package
        '.sys': 'text/other/system', # Windows system file
        '.tmp': 'text/other/system', # Temporary file

        '.3g2':	'media/video',	 # 3GPP2 multimedia file
        '.3gp':	'media/video',	 # 3GPP multimedia file
        '.avi':	'media/video',	 # AVI file
        '.flv':	'media/video',	 # Adobe Flash file
        '.h264':	'media/video',	 # H'.264 video file
        '.m4v':	'media/video',	 # Apple MP4 video file
        '.mkv':	'media/video',	 # Matroska Multimedia Container
        '.mov':	'media/video',	 # Apple QuickTime movie file
        '.mp4':	'media/video',	 # MPEG4 video file
        '.mpg':	'media/video',	 # MPEG video file
        '.mpeg':	'media/video',	 # MPEG video file
        '.rm':	'media/video',	 # RealMedia file
        '.swf':	'media/video',	 # Shockwave flash file
        '.vob':	'media/video',	 # DVD Video Object
        '.wmv':	'media/video',	 # Windows Media Video file

        '.doc':	'text/office/word',	 # Microsoft Word file
        '.docx': 'text/office/word',	 # Microsoft Word file
        '.odt':	'text/office/word',	 # OpenOffice Writer document file
        '.pdf':	'text/pdf',	 # PDF file
        '.rtf':	'text/text_files',	 # Rich Text Format
        '.tex':	'text/text_files',	 # A LaTeX document file
        '.txt':	'text/text_files',	 # Plain text file
        '.wpd':	'text/text_files'	 # WordPerfect document
    }

    def dir_for(self, file: str):
        if file.endswith(".tar.gz"):
            return self.extensions[".tar.gz"]
        else:
            extension = file[file.rindex("."):]
            if extension in self.extensions.keys():
                return self.extensions[extension]
            else:
                return "other/not_listed"
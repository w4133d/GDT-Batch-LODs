# Utility functions

__VERSION__ = "v1.3"

import os, sys, ctypes

# Global vairables
UTILS_DIR = os.path.dirname( os.path.abspath( __file__ ) )
ROOT_DIR = UTILS_DIR.replace( "utils", "" )
CONFIG_PATH = os.path.join( ROOT_DIR, 'configuration.conf' )
ASSETS_PATH = os.path.join( ROOT_DIR, "assets" )
DEBUG_STR   = "[    DEBUG    ]          "
ERROR_STR   = "[    ERROR    ]          "
WARNING_STR = "[   WARNING   ]          "
CONSOLE_STR = "[   CONSOLE   ]          "

# Flag
flags = {}

# when you use "from engine import *", you have to define the things it imports with the __all__ variable:
__all__ = [ 'flags', 'UTILS_DIR', 'ROOT_DIR', 'CONFIG_PATH', 'ASSETS_PATH', 'DEBUG_STR', 'ERROR_STR', 'WARNING_STR', 'CONSOLE_STR' ]

# Init level
class GVar():
    def __init__( self ):
        self.__info = 'Advanced global variable utilisation. No more worrying about variable scopes'

level = GVar()

__all__.append( 'level' )

# Wait - like GSC
from time import sleep

def wait( n_time_to_wait ):
    sleep( n_time_to_wait ); 

__all__.append( 'wait' )

# Info Message Box
def MsgBox( title: str, text: str, style: int ):
    """
    Message Box Styles: 
    
    MB_ABORTRETRYIGNORE = 2
    MB_CANCELTRYCONTINUE = 6
    MB_HELP = 0x4000
    MB_OK = 0
    MB_OKCANCEL = 1
    MB_RETRYCANCEL = 5
    MB_YESNO = 4
    MB_YESNOCANCEL = 3

    MB_ICONEXCLAMATION = MB_ICONWARNING = 0x30
    MB_ICONINFORMATION = MB_ICONASTERISK = 0x40
    MB_ICONQUESTION = 0x20
    MB_ICONSTOP = MB_ICONERROR = MB_ICONHAND = 0x10

    MB_DEFBUTTON1 = 0
    MB_DEFBUTTON2 = 0x100
    MB_DEFBUTTON3 = 0x200
    MB_DEFBUTTON4 = 0x300

    MB_APPLMODAL = 0
    MB_SYSTEMMODAL = 0x1000
    MB_TASKMODAL = 0x2000

    MB_DEFAULT_DESKTOP_ONLY = 0x20000
    MB_RIGHT = 0x80000
    MB_RTLREADING = 0x100000

    MB_SETFOREGROUND = 0x10000
    MB_TOPMOST = 0x40000
    MB_SERVICE_NOTIFICATION = 0x200000

    IDABORT = 3
    IDCANCEL = 2
    IDCONTINUE = 11
    IDIGNORE = 5
    IDNO = 7
    IDOK = 1
    IDRETRY = 4
    IDTRYAGAIN = 10
    IDYES = 6
    """
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

__all__.append( 'MsgBox' )

# Pillow Installer
import subprocess
import sys

def InstallPillow():
    os.system("cls || clear");

    print( "This program requires pillow, which handles image processing." );
    wait( 1.25 );

    while( True ):
        print( "You do not have pillow" );
        wait( 1 );
        print( "Would you like to install now? \ny | n" );
        option = input( " --> " ).lower();
        if( option == "yes" or option == "y" ):
            break;
        else:
            print( "You must install pillow to use this application." );
            wait( 1.75 );
            
            print( "Quit? \ny | n" );
            quit_input = input( " --> " ).lower();
            quit = True if( quit_input != "no" or quit_input != "n" ) else False;
            
            if( quit is True ):
                sys.exit();
            continue;

    os.system("cls || clear")

    wait(1)
    print("Installing Pillow...")
    wait(1)

    print(f"\n{ '=' * 40 }\n")
    wait(0.5)

    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])

    print("\n\nPillow installed successfully.\n\n")
    wait(0.75)
    print("Exiting...")
    wait(0.5)


# Progress bar

# Print iterations progress
def printProgressBar( iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r" ):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: print()



# Write print lines to console.log
import logging

# Init log
logging.basicConfig( 
    level=logging.DEBUG, 
    filename="console.log", 
    filemode="a+", 
    format="%(asctime)-15s %(levelname)-8s %(message)s"
)

logging.info( '\n\n\n' )
logging.info( f'{ "=" * 100 }\n{ "=" * 100 }' )
logging.info( '\n\n\n' )    

def PrintLn( *print_args, sep: str = ' ', end: str ='\n' ):
    """
    Prints to console & writes print statements to console.log
    <console.log> can be found in cwd
    """

    print_str = ''
    
    for item in print_args:
        if( not type( item ) == str ):
            item = str( item )
        
        print_str += item + sep
    
    print_str +=  bcolors.ENDC
    logging.info( print_str )
    print( print_str, sep=sep, end=end )

def log( *args ):
    """
    Writes a statements to console.log
    <console.log> can be found in cwd
    """
    log_str = ''


    for item in args:
        if( not type( item ) == str ):
            item = str( item )
        
        log_str += item
    
    log_str +=  bcolors.ENDC
    logging.info( log_str )

# Colour text when printing
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def RaiseWarning( *args, sep = ' ', end = '\n' ):
    _print_str = bcolors.WARNING + WARNING_STR
    for a in args:
        _print_str += str( a ) + sep
    PrintLn( _print_str, sep = sep, end = end )

def RaiseError( *args, sep = ' ', end = '\n' ):
    _print_str = bcolors.FAIL + ERROR_STR
    for a in args:
        _print_str += str( a ) + sep
    PrintLn( _print_str, sep = sep, end = end )

def Bold( *_args, sep = ' ' ):
    """Returns a string with a bold format. 
    If you were to print this string, text would be bold in console"""
    _str = ''
    for arg in _args:
        _str += str( arg ) + sep
    return bcolors.BOLD + _str + bcolors.ENDC

def Underline( *_args, sep = ' ' ):
    """Returns a string with an underlined format. 
    If you were to print this string, text would be underlined in console"""
    _str = ''
    for arg in _args:
        _str += str( arg ) + sep
    return bcolors.UNDERLINE + _str + bcolors.ENDC



units_of_time = (
    ( 'weeks',          86400 * 7   ),
    ( 'days',           86400       ),
    ( 'hours',          3600        ),
    ( 'minutes',        60          ),
    ( 'seconds',        1           ),
    ( 'milliseconds',   0.001       )
)

def DisplayTime( seconds, granularity=2 ):
    result = []

    for name, count in units_of_time:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])


byte_intervals = (
    ( 'GB',     10**9   ),
    ( 'MB',     10**6   ),
    ( 'KB',     10**3   ),
    ( 'bytes',  1       ),
    ( 'bits',   0.125   )
)

def DisplaySize( seconds, granularity=2 ):
    result = []

    for name, count in byte_intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])


def GetFolderSize( _dir : str, granularity : int = 3 ):
    """Returns the folder size in MB"""
    n_size = 0
    for path, dirs, files in os.walk( _dir ):
        for f in files:
            full_path = os.path.join( path, f )
            n_size += os.path.getsize( full_path )
    n_size = DisplaySize( n_size, granularity )
    return n_size

def GetFileSize( _filedir, granularity : int = 3 ):
    """Returns the respective file size in MB"""
    n_size = 0
    n_size += os.path.getsize( _filedir )
    n_size = DisplaySize( n_size, granularity )
    return n_size

def GetFileArraySize( _filedirarray, granularity : int = 3 ):
    """Returns the total file size of all the file paths in an array in MB"""
    n_size = 0
    for _dir in _filedirarray:
        n_size += os.path.getsize( _dir )
    n_size = DisplaySize( n_size, granularity )
    return n_size

def DeleteFile( _path ):
    os.remove( _path )

def StripAll( _str : str, *strip_args ):
    """
    Basically does the work of str.strip() | 
    But instead you can pass multiple chars and it will strip all the chars from the string, 1 by 1 | 
    Param 1 - String to be stripped | 
    Param 2 onwards - chars to strip from string"""
    for chars in strip_args:
        chars = str( chars )
        _str = _str.replace( chars, '' )
    
    return _str


def IsDefined( __param ):
    try:
        return True if __param is not None else False
    except NameError:
        return False
    return True

def IS_TRUE( __param ):
    return True if( __param is True or __param == True ) else False

def IS_EVEN( __number ):
    return True if ( __number % 2 ) == 0 else False

def IS_ODD( __number ):
    return True if ( __number % 2 ) == 1 else False

def DEFAULT( __var, __default ):
    if not IsDefined( __var ):
        return __default
    return __var

def GetDirName( __file__ ):
    return GetFolderName( __file__ )

def GetFolderName( __file__ ):
    return os.path.dirname( __file__ )

def GetFileName( __file__, extention=False ):
    if extention:
        return os.path.splitext( os.path.basename( __file__ ) )[0]
    return os.path.basename( __file__ )

def GetFileType( __file__ ):
    return os.path.splitext( __file__ )[1]

def GetFileTypesInDir( dir, file_format: str or list or tuple ): 
    list = []
    
    if( type( file_format ) == str ):
        for f in os.scandir( dir ):
            if( f.name.endswith( file_format ) ):
                list[ len( list ) ] = f.name
        return list
    
    return True if( [ [ f.name for f in os.scandir( dir ) if f.name.endswith( type_ ) ] for type_ in file_format ] ) else False

def GetFilesInDir( dir, full_path=False, extention : str = None ):
    """
    "full_path" - True returns the full path to the file, false only the file
    "extention" - can specify a filetype return
    """
    files = []; 
    if not full_path:
        if not extention is None:
            for f in os.scandir( dir ):
                if f.name.endswith( extention ):
                    files.append(f.name); 
        else:
            for f in os.scandir( dir ):
                files.append(f.name); 
        
        return files
    
    # Code below runs if full_path = true
    if not extention is None:
            for f in os.scandir( dir ):
                if f.name.endswith( extention ):
                    files.append( os.path.join( dir, f.name ) ); 
    else:
        for f in os.scandir( dir ):
            files.append( os.path.join( dir, f.name ) ); 
    return files
    

def SearchFileForKeyword( file, kword, return_idx=False, all=True ):
    """
    Searches a file and returns a list of all lines in that file that have the keyword in
    If nothing is found it returns None
    @params:
    if all is False, it will return the first occurence
    If return_idx is True, then it will return the line numbers
    """

    with open( file, 'r' ) as f:
        lines = f.readlines(); 
        matches = []; 
        matches_idx = []; 
        for line in lines:
            idx = lines.index( line ); 
            if( line.find( kword ) != -1 ):
                matches.append( line ); 
                matches_idx.append( idx ); 

    if matches == []:
        return None

    if not return_idx:
        if not all:
            return matches[0] # Return 1st match
        return matches # Return all matches
    if not all:
        return matches_idx[0] # Return line number of 1st match
    return matches_idx # Return line number of all matches



def Concatenate( *__params, sep: str = '' ):
    """
    Concatenates all params, with an optional separator defined by doing sep=
    """
    #print( __params )
    concatenation = ''
    for string in __params:
        concatenation += str( string ) + sep
    return concatenation

def ClearConsole():
    os.system( "cls || clear" ); 



from time import perf_counter

def timer():
    return perf_counter(); 



def GetPyVersion():
    """
    Returns current python version. 
    E.g. I am on python 3.11
    """
    
    return Concatenate( sys.version_info[ 0 ], '.', sys.version_info[ 1 ] )



def init( _str : str = 'INIT' ):
    ClearConsole()
    print( f'{"="*40} { _str } {"="*40}' )

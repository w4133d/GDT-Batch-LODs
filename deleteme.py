import os

GDT_PATH = "M:\\Black Ops III\\steamapps\\common\\Call of Duty Black Ops III\\model_export\\pv\\_Shoddy\\Medieval Ruins\\geo\\geo.gdt"; 
MODEL_EXPORT_ROOT_PATH = 'M:\\Black Ops III\\steamapps\\common\\Call of Duty Black Ops III\\model_export'

from utils.engine import *

string = 'yomama'; 
string.upper(); 
print( string ); 

def CreateLevelVar():
    level.GDT_PATH = GDT_PATH

CreateLevelVar()

print( level.GDT_PATH )
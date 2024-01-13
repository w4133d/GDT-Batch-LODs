"""
REF MISC MODEL ENTITY:

// entity 1
{
guid "{E017B222-6080-11EE-B31A-2CF05D5F8163}"
"classname" "misc_model"
"angles" "0 340 -25.0002"
"model" "pv_arrow"
"modelscale" "3.5"
"origin" "0.109985 -0.330994 43.789"
"lightingstate1" "1"
"lightingstate2" "1"
"lightingstate3" "1"
"lightingstate4" "1"
"static" "1"
}
"""

import os; os.system( 'cls||clear' ); 
import uuid

from utils import engine;
from utils.engine import *;

engine.init(); 
StartTime = engine.timer(); 

GDT_PATH = "M:\\Black Ops III\\steamapps\\common\\Call of Duty Black Ops III\\model_export\\pv\\_Shoddy\\Medieval Ruins\\geo\\geo.gdt"; 
BO3_ROOT_PATH = 'M:\\Black Ops III\\steamapps\\common\\Call of Duty Black Ops III\\'; 
MAP_FILE_PATH = os.path.join( BO3_ROOT_PATH, 'map_source\\_prefabs\\_pv\\pv_medieval_ruins.map' ); 

######################
## Get xmodel names ##
##     from GDT     ##
######################

with open( GDT_PATH, 'r' ) as gdt:
    gdt_lines = gdt.readlines(); 

xmodels = []; 
for line in gdt_lines:
    
    if line.find( 'xmodel.gdf' ) == -1:
        continue; 

    xmodels.append( line.split( '"' )[1] ); 

#############################
## Place xmodels at origin ##
##     in the map file     ##
#############################

# Doing this as a function and not just a var cause it's cleaner & I can 
# pass a new guid, model name & ent_number as a param each iteration
def GenerateCoDMapXModel( entity_no, _guid, _model ):
    return engine.Concatenate( 
        f'// entity {entity_no}', 
        '{', 
        f'guid "{ "{" + str( _guid ).upper() + "}" }"', 
        '"classname" "misc_model"', 
        '"angles" "0 0 0"', 
        f'"model" "{_model}"', 
        '"modelscale" "1"', 
        '"origin" "0 0 0"', 
        '"lightingstate1" "1"', 
        '"lightingstate2" "1"', 
        '"lightingstate3" "1"', 
        '"lightingstate4" "1"', 
        '"static" "1"',
        '}', 
        sep='\n'
    ); 

print( 'Found', len( xmodels ), 'xmodels in', os.path.basename( GDT_PATH ) ); 
print( 'Placing all xmodels at origin...' ); 

# Clear map file so radiant doesn't shit itself
# (sanity error) when there are 2 worldspawns in a prefab
codmap = open( MAP_FILE_PATH, 'w' ); codmap.write( '' ); codmap.close(); 

with open( MAP_FILE_PATH, 'a+' ) as codmap:
    # Write worldspawn [entity 0] to .map prefab
    entity_0 = open( os.path.join( engine.ROOT_DIR, 'entity 0.txt' ), 'r' ); 
    map_data = entity_0.read(); 
    entity_0.close(); 
    
    for idx in range( len( xmodels ) ):
        engine.printProgressBar( idx, len( xmodels ) - 1, suffix='Complete' ); 
        map_data += GenerateCoDMapXModel( idx + 1, uuid.uuid1(), xmodels[idx] ); 
    
    #print( map_data ); # prints the whole map file
    
    # Just checked the .map file and was like dman it didnt write anything wtf
    # then i realised i fogot to write to the file (╯°□°）╯︵ ┻━┻ :kekw:
    # ¯\_(ツ)_/¯
    codmap.write( map_data ); 

print( 'Generated codmap at', MAP_FILE_PATH ); 
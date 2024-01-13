"""
Official Bulk Auto-LOD GDT Assigner for Call of Duty®: Black Ops III - Mod Tools
© 2023 Activision Publishing, Inc. ACTIVISION, CALL OF DUTY, CALL OF DUTY BLACK OPS III and CALL OF DUTY BLACK OPS III - MOD TOOLS are trademarks of Activision Publishing, Inc. 
All other trademarks and trade names are the property of their respective owners.

"lowestLod" "pv\\_Shoddy\\Medieval Ruins\\geo\\sm_bench_01_01_lod3.xmodel_bin"

"lowLod" "pv\\_Shoddy\\Medieval Ruins\\geo\\sm_bench_01_01_lod2.xmodel_bin"

"mediumLod" "pv\\_Shoddy\\Medieval Ruins\\geo\\sm_bench_01_01_lod1.xmodel_bin"

"""

"""
XBIN_LINES_IN_GDT = engine.SearchFileForKeyword( GDT_PATH, '.xmodel_bin' ); 
XBIN_LINE_IDX_IN_GDT = engine.SearchFileForKeyword( GDT_PATH, '.xmodel_bin', return_idx=True ); 
XFILES_IN_FOLDER = engine.GetFilesInDir( engine.GetDirName( GDT_PATH ), extention='xmodel_bin', full_path=True ); 

LOD_LEVELS = [ 'lowestLod', 'lowLod', 'mediumLod' ]

# FUNCTIONS #

# There's no reason i should search the whole folder of 20k xmodels (inc. LODs) to verify they have a lod for that model, i KNOW
# that the file exists, so why tf am i wasting time doing this? This is partly why i rewrote the script below
def get_lod_files_for_xmodel( xmodel: str, xfiles: list[ str ] ):
    ""
    Searches the folder of the GDT_PATH and returns file paths of all respective LODs
    ""
    _lod1 = xmodel.replace( 'lod0', 'lod1' ); 
    _lod2 = xmodel.replace( 'lod0', 'lod2' ); 
    _lod3 = xmodel.replace( 'lod0', 'lod3' ); 
    _lod_scale = [ _lod1, _lod2, _lod3 ]
    #print( '_lod_scale =', _lod_scale )
    _lod_files = []
    #print( "xmodel =", xmodel )
    for f in xfiles:
        for _lod in _lod_scale:
            file_name = engine.GetFileName(f, extention=True); 
            if file_name == _lod:
                _lod_files.append( f ); 
    return _lod_files

def extract_file_name( line ):
    file_path = line.split( '"' )[3]; 
    file_name = os.path.splitext( engine.GetFileName( file_path ) )[0]; 
    return file_name

print( "Processing data..." )
engine.printProgressBar
all_lod_lists = []
with open( GDT_PATH, 'r' ) as gdt:
    gdt_data = gdt.readlines(); 
    for i in range( len(XBIN_LINES_IN_GDT) ):
        engine.printProgressBar( i, len( XBIN_LINES_IN_GDT ) - 1 ); 
        xmodel = extract_file_name( XBIN_LINES_IN_GDT[i] ); # example datum: "sm_chapelcornice_01_02_lod0_17"
        LODs = get_lod_files_for_xmodel( xmodel, XFILES_IN_FOLDER ); # Get LODs 1, 2 & 3 file paths
        #print( "len( LODs ) =", len( LODs ) )
        for lod in LODs: 
            idx = LODs.index( lod ); 
            lod = lod.replace( MODEL_EXPORT_ROOT_PATH, '' ); 
            #print( 'adding lod', lod, 'to GDT' )
            #print( 'idx =', idx )
            #print( 'LODs =', LODs )
            #print( 'XBIN_LINES_IN_GDT[i] =', XBIN_LINES_IN_GDT[i] + ', line number', XBIN_LINE_IDX_IN_GDT[i] )
            #print( 'XBIN_LINE_IDX_IN_GDT[i] =', XBIN_LINE_IDX_IN_GDT[i] )
            #print( f'\nAnd gdt_data[ {XBIN_LINE_IDX_IN_GDT[i] + idx} ] is', gdt_data[ XBIN_LINE_IDX_IN_GDT[i] + idx ] )
            gdt_data.insert( ( XBIN_LINE_IDX_IN_GDT[i] + idx ), engine.Concatenate( ( '\n' if lod.find( 'lod0') == -1 else '' ), '\t\t"', LOD_LEVELS[idx], '" "', lod, '"', ( '\n' if lod.find( 'lod3' ) != -1 else '' ) ) ); 

gdt = open( GDT_PATH, 'w' ); 
gdt.writelines( gdt_data ); 
gdt.close(); 

TotalTime = engine.timer() - StartTime; 
print( 'Finished writing file', GDT_PATH, 'in', engine.DisplayTime( TotalTime ) ); 

"""
# ==========================================================================================

# ==========================================================================================

import os; os.system( 'cls||clear' )

from utils import engine
from utils.engine import *;

engine.init()
StartTime = engine.timer(); 

GDT_PATH = "M:\\Black Ops III\\steamapps\\common\\Call of Duty Black Ops III\\model_export\\pv\\_Shoddy\\Medieval Ruins\\geo\\geo.gdt"; 
MODEL_EXPORT_ROOT_PATH = 'M:\\Black Ops III\\steamapps\\common\\Call of Duty Black Ops III\\model_export'
GDT_READ = open( GDT_PATH, 'r' ); 
gdt_data = GDT_READ.readlines(); 
GDT_LINES = engine.SearchFileForKeyword( GDT_PATH, '"filename"' ); 
LOD_LEVELS = [ 'lowestLod', 'lowLod', 'mediumLod' ]; 

for i in range( len( GDT_LINES ) ):
    engine.printProgressBar( i, len( GDT_LINES ) - 1 ); 
    
    lod0_path = GDT_LINES[i].split( '"' )[3]; 
    lod1_path = lod0_path.replace( 'lod0', 'lod1' ); 
    lod2_path = lod0_path.replace( 'lod0', 'lod2' ); 
    lod3_path = lod0_path.replace( 'lod0', 'lod3' ); 
    
    lod1_line = f'\t\t"{ LOD_LEVELS[2] }" "{ lod1_path }"'; 
    lod2_line = f'\t\t"{ LOD_LEVELS[1] }" "{ lod2_path }"'; 
    lod3_line = f'\t\t"{ LOD_LEVELS[0] }" "{ lod3_path }"'; 
    
    #print( gdt_data.index( GDT_LINES[i] ) + 1, '|', lod1_line ); 
    #print( gdt_data.index( GDT_LINES[i] ) + 2, '|', lod2_line ); 
    #print( gdt_data.index( GDT_LINES[i] ) + 3, '|', lod3_line ); 
    #print(); 
    
    gdt_data.insert( gdt_data.index( GDT_LINES[i] ) + 1, lod1_line + '\n' ); 
    gdt_data.insert( gdt_data.index( GDT_LINES[i] ) + 2, lod2_line + '\n' ); 
    gdt_data.insert( gdt_data.index( GDT_LINES[i] ) + 3, lod3_line + '\n' ); 

GDT = open( GDT_PATH, 'w' ); 
GDT.writelines( gdt_data ); 
GDT.close();         

TotalTime = engine.timer() - StartTime; 
print( 'Finished writing LOD paths to', os.path.basename( GDT_PATH ), 'in', engine.DisplayTime( TotalTime ), '\n\nFile path:', GDT_PATH ); 
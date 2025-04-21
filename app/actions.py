from tools import console
from tools import database
import serializer

log = console.Logger("ACTION")

def unpack(inpath: str, outpath: str):
    try:
        manager = database.BaseManager(inpath)
    except:
        log.error("Failed to open database :0")

    if manager.count == 0:
        log.warning("Database is empty!")
    else:
        serializer.export_zodb(manager, outpath)
    

def pack(inpath: str, outpath: str):
    try:
        manager = database.BaseManager(outpath)
    except:
        log.error("Failed to open database :0")

    serializer.import_json(inpath, manager)
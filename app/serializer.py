import json
from tools import console

log = console.Logger("SERIALIZER")

def serialize_obj(obj):
    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj
    elif isinstance(obj, dict):
        return {k: serialize_obj(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [serialize_obj(v) for v in obj]
    elif isinstance(obj, tuple):
        return {
            "__type__": "tuple",
            "items": [serialize_obj(v) for v in obj]
        }
    else:
        return {
            "__type__": obj.__class__.__name__,
            "__module__": obj.__class__.__module__,
            "attributes": {
                k: serialize_obj(v)
                for k, v in obj.__dict__.items()
            }
        }

def deserialize_obj(data):
    pass

def export_zodb(manager, json_path):
    try:
        data = manager.get_root()
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({k: serialize_obj(v) for k, v in data.items()}, f, indent=4, ensure_ascii=False)
        log.success("Processed has been ended.")
    except Exception as ex:
        log.error(f"Failed to export database: {ex}")

def import_json(json_path, manager):
    log.warning("Sorry, this feature is not implemented yet ._.")
    return
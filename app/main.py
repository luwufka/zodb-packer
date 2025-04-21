import argparse
from tools import console
from actions import pack, unpack

log = console.Logger("MAIN")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a tool for the Zope Object Database")

    parser.add_argument("inpath", type=str, help="Input path")
    parser.add_argument("action", type=str, help="Action to perform: pack / unpack")
    parser.add_argument("outpath", type=str, help="Out path")

    args = parser.parse_args()

    match args.action:
        case "pack":
            pack(args.inpath, args.outpath)
        case "unpack":
            unpack(args.inpath, args.outpath)
        case _:
            log.warning("Invalid action ._.")
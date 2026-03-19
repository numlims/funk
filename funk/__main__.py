# automatically generated, DON'T EDIT. please edit main.ct from where this file stems.
import argparse
import funk
import os
import sys
def main():
    """
     main chunks a fhir bundle into a bunch of fhir bundles, each holding a
     primary sample and its children.
    """
    parser = argparse.ArgumentParser(description="fhir chunk")
    parser.add_argument("input", help="the input file or dir to chunk")
    parser.add_argument("outdir", help="the output directory")
    parser.add_argument("-e", help="input encoding")
    args = parser.parse_args()    
    out = []
    if os.path.isdir(args.input):
        files = os.listdir(args.input)
        for file in files:
            _, ext = os.path.splitext(file)
            if ext != ".json":
                continue
            path = os.path.join(args.input, file)
            written = funk.chunk(path, args.outdir, encoding=args.e)
            out.extend(written)
    else:
        out = funk.chunk(args.input, args.outdir, encoding=args.e)
    for o in out:
        print(o)
sys.exit(main())

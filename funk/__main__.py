# automatically generated, DON'T EDIT. please edit main.ct from where this file stems.
import argparse
import funk
import sys
def main():
    """
     main chunks a fhir bundle into a bunch of fhir bundles, each holding a
     primary sample and its children.
    """
    parser = argparse.ArgumentParser(description="fhir chunk")
    parser.add_argument("file", help="the file to chunk")
    parser.add_argument("outdir", help="the output directory")
    parser.add_argument("-e", help="encoding")
    args = parser.parse_args()    
    out = funk.chunk(args.file, args.outdir, encoding=args.e)
    for o in out:
        print(o)
sys.exit(main())

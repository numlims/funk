# automatically generated, DON'T EDIT. please edit init.ct from where this file stems.
import fhirbuild
from figs import specimen as figs
import json
import pathlib
def chunk(infile:str, outdir:str, encoding:str="utf-8") -> list:
    """
     chunk chunks a fhir resource into multiple files, each holding one
     primary sample and its children. it assumes that the children
     immediately follow their respective primary. it returns a list of files written.
    """
    f = open(infile, "r", encoding=encoding)
    jsonin = json.load(f)
    f.close()
    entries = jsonin["entry"]
    chunks = []
    currentchunk = []
    for entry in entries:
        resource = figs.resource(entry)
        if figs.category(resource) == "MASTER":
            if len(currentchunk) > 0:
                chunks.append(currentchunk)
            currentchunk = [entry]
        else:
            currentchunk.append(entry)
    stem = pathlib.Path(infile).stem
    return fhirbuild.writeout(chunks, outdir, outname=stem)

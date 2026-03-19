# automatically generated, DON'T EDIT. please edit init.ct from where this file stems.
import fhirbuild
from figs import specimen as figs
import json
import pathlib
def chunk(infile:str, outdir:str, encoding:str="utf-8") -> list:
    """
     chunk chunks a fhir resource into multiple files and returns a list of
     files written.
     
     specimen: each written file holds one primary sample and its
     children. it assumes that the children immediately follow their
     respective primary.
     
     observation: it puts max 5 together into one file.
    """
    with f = open(infile, "r", encoding=encoding):
        jsonin = json.load(f)
        entries = jsonin["entry"]
        chunks = []
        currentchunk = []
        obschunks = []
        currentobs = []
        for entry in entries:
            resource = figs.resource(entry)
            if figs.resource_type(resource) == "Observation":
                if len(currentobs) == 5:
                    obschunks.append(currentobs)
                    currentobs = []
                currentobs.append(entry)
            elif figs.resource_type(resource) == "Specimen":
                if figs.category(resource) == "MASTER":
                    if len(currentchunk) > 0:
                        chunks.append(currentchunk)
                    currentchunk = [entry]
                else:
                    currentchunk.append(entry)
        if len(currentchunk) > 0:
            chunks.append(currentchunk)
        if len(currentobs) > 0:
            obschunks.append(currentobs)
        stem = pathlib.Path(infile).stem
        #print(len(obschunks))
        return fhirbuild.writeout(chunks + obschunks, outdir, outname=stem)

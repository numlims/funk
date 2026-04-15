# funk - fhir chunk
 
chunk a fhir bundle into seperate files each containing a primary sample and its children.

```
funk <infile> <outdir>
```

api doc [here](https://numlims.github.io/funk/).

## install

download funk whl from
[here](https://github.com/numlims/funk/releases). install whl with
pip:

```
pip install funk-<version>.whl
```

## dev

edit [init.ct](funk/init.ct) and [main.ct](funk/main.ct).

generate the code from the ct files with [ct](https://github.com/tnustrings/ct).

build and install:

```
make install
```

generate api doc:

```
make doc
```

# LDPy

[LDP 1.0](https://www.w3.org/TR/ldp/) Client for Python. 

Very prototypical client, initially written for cross-testing [Apache Marmotta reference implementation](http://wiki.apache.org/marmotta/LDPImplementationReport).

## Setup

Releases available from PyPI: https://pypi.python.org/pypi/ldpy

    pip install ldpy

## Usage

    ldpy = ldpy.Client("http://localhost:8080/ldp")
    resource = ldpy.create("http://localhost:8080/ldp", open("file.ttl"), "text/turtle", "example")
    print ldpy.read(resource)

Available under [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).

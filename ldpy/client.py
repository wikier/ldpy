# -*- coding: utf8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rdflib.graph import Graph
import requests

_rdflibFormatsMappings = {
    "text/turtle"           : "turtle",
    "application/rdf+xml"   : "xml",
    "text/n3"               : "n3",
    "application/n-triples" : "nt",
    "application/trix"      : "trix"
}

class Client:

    def __init__(self, server):
        self.server = server
        try:
            requests.head(self.server)
        except requests.exceptions.ConnectionError, e:
            raise ValueError("server %s does not look to be alive: %s" % (server, e.message))

    def create(self, container, payload, format=None, tentativeName=None):
        if (not container.startswith(self.server)):
            raise ValueError("base container %s does not belong to this client instance", container)

        # TODO: do this in a more pythonic way
        g = None
        if (payload):
            if (type(payload) == str):
                if (not format in _rdflibFormatsMappings):
                    raise ValueError("unsupported format %s to send string payload", format)
                else:
                    g = Graph()
                    g.parse(data=payload, format=_rdflibFormatsMappings[format])
            elif (type(payload) == file):
                if (not format in _rdflibFormatsMappings):
                    raise ValueError("unsupported format %s to send string payload", format)
                else:
                    g = Graph()
                    g.parse(data=payload.read(), format=_rdflibFormatsMappings[format])
            elif (type(payload) == Graph):
                g = payload
            else:
                raise ValueError("unsupported type %s as payload", type(payload))

        headers = {"Content-Type" : "text/turtle" }
        if (len(tentativeName) > 0 ):
            headers["Slug"] = tentativeName
        request  = requests.post(container, data=g.serialize(format='turtle'), headers=headers)

        if (request.status_code == 201):
            return request.headers["Location"]
        else:
            raise RuntimeError("creation of resource in container %s failed, server returned %d status code", (container, request.status_code))
        
    def read(self, resource, format=None):
        if (not resource.startswith(self.server)):
            raise ValueError("requested resource %s does not belong to this client instance", resource)

        if (not format in _rdflibFormatsMappings):
            format = "text/turtle"

        request  = requests.get(resource, headers={"Accept" : format })

        if (request.status_code == 200):
            return request.text
        else:
            raise RuntimeError("reading resource %s failed, server returned %d status code", (resource, request.status_code))

        

if __name__ == "__main__":
    ldp = Client("http://localhost:8080/ldp")

    blog = ldp.create("http://localhost:8080/ldp", open("data/blog.ttl"), "text/turtle", "blog")
    print "LDP Blog created at <%s>: ", blog
    print
    print ldp.read(blog)
    print

    post = ldp.create(blog, open("data/post.ttl"), "text/turtle", "post")
    print "LDP Post created at %s: ", post
    print
    print ldp.read(post)
    print

    print ldp.read("http://localhost:8080/ldp/foo")




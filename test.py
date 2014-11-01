# -*- coding: utf8 -*-

import ldpy

if __name__ == "__main__":

    ldpy = ldpy.Client("http://localhost:8080/ldp")

    blog = ldpy.create("http://localhost:8080/ldp", open("data/blog.ttl"), "text/turtle", "blog")
    print "LDP Blog created at <%s>: ", blog
    print
    print ldpy.read(blog)
    print

    post = ldpy.create(blog, open("data/post.ttl"), "text/turtle", "post")
    print "LDP Post created at %s: ", post
    print
    print ldpy.read(post)
    print

    #print ldpy.read("http://localhost:8080/ldp/foo")

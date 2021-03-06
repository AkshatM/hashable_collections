# About

This library enables dictionaries and lists to be used as keys inside a dictionary. In other words, it makes them hashable. 

While mutable objects (lists, dictionaries) should not be made hashable in general, the programmer is trusted not to abuse this power (you *do* test your code before shipping into production, don't you?). An extension option to explicitly make the resulting hashable object immutable is provided below for convenience.

There are certain use cases - e.g. when trying to pass seemingly identical keys to [NetworkX](https://networkx.github.io) as different nodes, or when you want to query an object's properties in place while making a mapping instead of calling a complicated identification function - where these may be useful and reduce boilerplate code.  

# Usage

```
>>> from hashable_collections.hashable_collections import hashable_dict
>>> hashed_dict = hashable_dict({'name':'foo'})
>>> from hashable_collections.hashable_collections import hashable_list
>>> hashed_list = hashable_list(['bar',1])
>>> output = {hashed_dict:0,hashed_list:1}
>>> output
{{'name':'foo'}: 0, ['bar', 1]: 1}

```
These hashable objects still retain mutability - in other words, it is still possible to assign `hashed_dict['squiggle'] = 'squiggle'` and have it execute without an issue. The hash will change correspondingly, effectively making it a different object from before.

Alternatively, one can subclass the objects defined here and override the `__setitem__` method to make sure the resulting hashable dictionary/list is immutable:

```
class immutable_hashable_dict(hashable_dict):

    def __setitem__(self,key,value):
        raise ValueError('Immutable hashable dicts do not let you change values inside your dictionary.')

class immutable_hashable_list(hashable_list):

    def __setitem__(self,key,value):
        raise ValueError('Immutable hashable lists do not let you change valus inside your list.')

```
# Caveats

The following is a list of known issues that may crop up with this technology.

-    Creating a copy: If `s` is a `hashable_dict`, and one does `m = s` and then changes `m[0]`, the corresponding value of `s[0]` is changed as well. **Never** assign an existing hashable_dict or hashable_list to another object unless you are sure the second object is not going to change.

# Installation

`pip install hashable_collections`

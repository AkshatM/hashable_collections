'''
A collection of hashable implementations of ordinary Python objects e.g. dictionaries and lists.
'''

class hashable_dict(dict):

  '''

  Implements a hash method for dictionaries, allowing one to use them as keys
  in another dictionary. This implementation is sourced from Alex Martelli's
  answer at Stack Overflow:

  http://stackoverflow.com/questions/1151658/python-hashable-dicts

  It is recommended that all hashable_dicts be considered immutable to avoid
  unexpected hash collisions, although this property is not strictly enforced.

  To instantiate, simply pass a dictionary to hashable_dict as argument.
  '''

  def __key(self):
    
    '''

    Returns a tuple of tuples for hashing in __hash__; orders dictionaries first,
    so that identical dictionaries with randomised key order obtain the same hash
    value.

    '''

    return tuple((k,self[k]) for k in sorted(self))

  def __hash__(self):
    return hash(self.__key())

  def __eq__(self, other):
    return self.__key() == other.__key()

class hashable_list(list):

  '''

  Implements a hash method for dictionaries, allowing one to use them as keys
  in another dictionary. This implementation is modified from Alex Martelli's
  answer at Stack Overflow about hashable dictionaries:

  http://stackoverflow.com/questions/1151658/python-hashable-dicts

  It is recommended that all hashable_lists be considered immutable to avoid
  unexpected hash collisions, although this property is not strictly enforced.

  To instantiate, simply pass a list to hashable_list as argument.
  '''

  def __key(self):
    
    '''

    Returns a tuple of tuples for hashing in __hash__; does not order lists, so that
    arrays with identical elements, but non-identical order, are not considered equivalent.

    Hashable_lists are also not made immutable - however, as in hashable_dicts, this behaviour
    is strongly recommended to prevent hash collisions.
    
    '''

    return tuple((k) for k in self)

  def __hash__(self):
    return hash(self.__key())

  def __eq__(self, other):
    return self.__key() == other.__key()

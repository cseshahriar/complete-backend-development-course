""" exception """
"""
built in errors: 
    IndexError 
    KeyError 
    NameError
    AttributeError
    NotImplementedError
    RuntimeError
    SyntaxError
    IndentationError
    TabError
    TypeError
    ValueError
    ImportError
    DeprecationError
"""

# index error
friends = ['Nazmul', 'Piyash']

try:
    print(friends[2])
except IndexError as e:
    print(e)

try:
    print(x)
except Exception as e:
    print(e)

try:
    print(x)
except NameError as e:
    print(e)
except Exception as e:
    print(e)


try:
  print(x)
except:
  print("Something went wrong")
finally:
    raise Exception("The 'try except' is finished")
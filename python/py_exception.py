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

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#     raise Exception("The 'try except' is finished")


# key error
def show_movie(movie):
    try:
        # print(f"name : {movie[0]}")
        print(f"name : {movie[1]}")
    except KeyError as e:
        pass


show_movie(['shahriar', 3])


# attr errors
friends3 = {'name': 'Shhariar'}

try:
    print(friends3.get('age'))
except AttributeError as e:
    pass
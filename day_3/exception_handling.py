#!/usr/bin/python3

def foo():
   num = float(input("Enter a floating number: "))
   return num

while True:
    try:
        print(foo())
        print(shiva) # in case there is no ValueError raised by input then to raise NameError
    except ValueError:
        print("You entered wrongly")
    except NameError:
        print("NameError occurred!")
    except:
        print("\nUnknown exception occur")
    finally:
        print("This is the final statement useful to close files")
        break 

try:
    raise TypeError("a type error occured")
except TypeError:
    print("\nthis is intentional")

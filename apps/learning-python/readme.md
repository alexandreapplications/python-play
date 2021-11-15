# Remember

## Variables can be set togeter
a, b = 2, 3

## Python can multiply strings
```python
    a = 10
    print ("Alexandre" * a)
```

## String formating
Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

```python
    # This prints out "John is 23 years old."
    name = "John"
    age = 23
    print("%s is %d years old." % (name, age))
```

## Some formaters
* %s - String (or any object with a string representation, like numbers)
* %d - Integers
* %f - Floating point numbers
* %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
* %x/%X - Integers in hex representation (lowercase/uppercase)

## Slice strings

[start:stop:step].

## IFs

* if name == "John" and age == 23:
* if name == "John" or name == "Rick":
* if name in ["John", "Rick"]:
* if full
```python
    if statement is True:
        # do something
        pass
    elif another_statement is True: # else if
        # do something else
        pass
    else:
        # do another thing
     pass
```

## FOR
* primes = [2, 3, 5, 7]
  for prime in primes:
* for x in range(begin, end, step):
* We can use else for loops to be run after the look unless break is called

## Module
We can use if to select which module

```python
    # game.py
    # import the draw module
    if visual_mode:
        # in visual mode, we draw using graphics
        import draw_visual as draw
    else:
        # in textual mode, we print out text
        import draw_textual as draw

    def main():
        result = play_game()
        # this can either be visual or textual depending on visual_mode
        draw.draw_game(result)
```
Import from another folder
```python
import sys
sys.path.append("/foo")
```

There are some libraries. We can find the list here:
https://docs.python.org/3/library/


#!/usr/bin/env python3
# define function
def color_translator(color):
 if color=="red":
  return print("color code #FF0000")
 elif color=="green":
  return print("color code #00FF00")

 elif color=="blue":
  return print("color code #0000FF")
 else:
    return print("unknown color")
color_translator("red")
color_translator("blue")
color_translator("pink")
color_translator("green")

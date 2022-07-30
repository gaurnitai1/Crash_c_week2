#!/usr/bin/env python3
def format_name(last,first):
    if first!="":
        formatted=("Name:"+(first+" "+last))
        return formatted
    elif first=="" and last!="":
        formatted=("Name:"+last)
        return formatted
    else:
        formatted=" "
        return formatted
print(format_name("Ernest", "Hemingway"))
print(format_name("", "Madonna"))
print(format_name("Voltaire", ""))
print(format_name("", ""))

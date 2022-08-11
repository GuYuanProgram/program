import os
import time
import tkinter as tk
from tkinter import messagebox
import datetime
import generate


class terminal_info:
    info = "easy for Box"
    start = os.getcwd()+" $ "
    @classmethod
    def error(cls,errorsentences):
        return f"error! the '{errorsentences}' is not can run's language!"

class sen:
    public = {"ls":os.getcwd(),"info":terminal_info.info,"time":datetime.datetime.today(),"date":datetime.date.today()}
    def __init__(self,s):
        pass
    @classmethod
    def syntax(cls,s):
        if s == "calc":
            generate.calc()
        elif s.split(" ",maxsplit=1)[0] == "echo":
            try:
                generate.echo(s.split(" ", maxsplit=1)[1])
            except:
                pass
            finally:
                pass
        else:
            return True

print("\n"+"-"*70)
print(
    """
    -----------               ooooooooooo                 x         x
    -          -             o           o                 x       x
    -          -             o           o                  x     x
    -        -               o           o                   x   x
    ---------                o           o                    x x
    -        -               o           o                    x x
    -          -             o           o                   x   x
    -          -             o           o                  x     x
    ------------              ooooooooooo                  x       x
"""
)
print("\n"+"    Box    "+f"restart in {os.getcwd()},   size:{os.path.getsize(os.path.splitext(os.getcwd())[0])/1024}"+"KB"+"\n"+"-"*70)
for i in range(3):
    print()
print(terminal_info.info)
while 1:
    lang = input(terminal_info.start)
    if lang in sen.public.keys():
        print(sen.public[lang])
    else:
        if sen.syntax(lang):
            print(terminal_info.error(lang))
    print()









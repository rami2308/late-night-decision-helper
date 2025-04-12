# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 19:01:35 2025

@author: rkd23
"""

import time








print("🚨 Late Night Decision Checker 🚨")
print()
print("It's 3am and you're thinking about messaging your ex...")
print()

answer = input("Do you still want to do it? (yes/no): ")
print()

if answer.lower() == "yes":
    print("is it just because you're horny? think about it for a few moments...")
    time.sleep(3)
    answer=input("answer: ")
    if answer.lower()=="yes":
        print("I knew it! relax and forget about it... GOOD NIGHT")
    else:
        print("Are you gonna regret this tommorow?...think about it")
        time.sleep(3)
        answer=input("answer: ")
        if answer.lower()=="yes":
            print("Thought so! GOOD NIGHT")
        else:
            print("i think its a bad idea... good luck!")
        
        
else:
    print("Nice. You're already making smarter choices.")











































































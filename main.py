#!/usr/bin/env python3
 
import greetings

# define a function that calls your library definition below:
def lee_hello():
    greetings.lee.hello();

def ben_hello():
    greetings.ben.hello();
# add a call to your function in main, below the heading output: 
def main():
    print("Fall 2025 CSP 200 PR Yearbook")
    print("=============================")
    
    lee_hello()
    ben_hello()

# don't touch this!
if __name__ == "__main__":
    main()

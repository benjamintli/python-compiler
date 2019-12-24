# python-compiler
me learning how LLVM works


## Installation
```
$ sudo apt-get install llvm
$ sudo apt-get install build-essential
$ python3 -m virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Trying it out
1. generate the llvm linker file 
    ```
    $ python3 main.py <path to input code> <IR file name>
    ```
1. use llvm CLI to generate an object file
    ```
    $ llc -filetype=obj <IR file name>
    ``` 
1. use the .o file generated with the previous command and use a linker like gcc to create an executable
    ```
    $ gcc -no-pie <object file name> -o <executable name>
    ```
1. run the executable!
    ```
    $ ./<executable name>
    ```

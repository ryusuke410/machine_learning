# Day1



## setup

###  Docker

* `~` is the abbrebiation of the home directory of the user.

* In docker type `ls ~`.
  You can know the contents of the home directory.
  (and also you can infer what directory of your host OS is used
  as the home directory of docker prompt.)
  
* In your host, create a directory, say `atom/` for sharing at the
  directory you find in the step above.
  
* In docker, run the tesorflow image mounting `atom/
  
  ```
  docker run -v ~/atom:/root/atom -it <tensorflow image>
  ```
  

### Atom

Put the source files you write with Atom to `atom/` on your host OS,
so that you can access to the source files from tensorflow image.


## python


* `ipython` or `python` will run the interpreter of python.

* In a python interpreter, you can load a source file with 
  `execfile(<file name>)`, where `<file name>` must be a string,
  say, `~/atom/mysource.py`


### class

See `./MyClass.py` to enjoy some experiments with class in python.
(This experiments is based on [python tutorial]( "")).

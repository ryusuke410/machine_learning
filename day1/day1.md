# Day1



## setup

###  Docker

* `~` abbreviates the home directory of the user.

* Type `ls ~` in the docker prompt, then you can know the contents of
  the home directory.

* The following denotes the command on docker prompt:
  
  ```
  docker:~$ ls ~
  ```

* From the result of the above command, you can guess what directory
  of your host OS is used as the home directory of docker prompt.
  Write the directory as `DOCKER~`.
  
* In your host, create a directory, say `DOCKER~/atom/` for sharing:
  
  ```
  docker:~$ mkdir ~/atom
  ```
  
* In docker, run the tesorflow image mounting `DOCKER~/atom/`
  
  ```
  docker:~$ docker run -v ~/atom:/root/atom -it <tensorflow image>
  ```
  

### Atom

Put the source files you write with Atom to `DOKER~/atom/` on your
hostOS so that you can access to the source files from tensorflow
image.


## python


* `ipython` or `python` will run the interpreter of python:
  
  ```
  tensorflow:~# ipython[python]
  ```
  
  where `tensorflow:~#` represents the terminal on the container in
  which the tensorflow image is running.

* Exit from the python interpreter with `quit()`.

* Suspend the interpreter with `C-z`(`Ctrl` + `z`).
  And then a message like the following will appear:
  
  ```
  [2]+  Stopped                 ipython
  ```
  
  In this case, you can return to the procedure with `%2`, or kill it
  with `kill %2`.

* In a python*2* interpreter, you can load a source file with 
  `execfile(<file name>)`, where `<file name>` must be a string,
  say, `"~/atom/mysource.py"` For example,
  
  ```
  python:>>> execfile("~/atom/mysource.py")
  ```
  
  may run the python commands in `~/atom/mysource.py` and so the
  variables or methods defined in the sourcefile will be available
  in current python interpreter.
  
* For python3, use the following instead:
  
  ```python
  with open(<file name>) as f:
      exec(f.read())
  ```


### class

See [MyClass.py](./MyClass.py "MyClass.py") to enjoy some experiments
with class in python.
(This experiments is based on [python tutorial](
https://docs.python.org/3/tutorial/classes.html "class")).

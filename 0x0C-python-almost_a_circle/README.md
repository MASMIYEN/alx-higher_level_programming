# 0x0C. Python - Almost a circle

## Background Context

The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:

-   Import
-   Exceptions
-   Class
-   Private attribute
-   Getter/Setter
-   Class method
-   Static method
-   Inheritance
-   Unittest
-   Read/Write file

You will also learn about:

-   `args`  and  `kwargs`
-   Serialization/Deserialization
-   JSON

## Resources

**Read or watch**:

-   [args/kwargs](https://intranet.alxswe.com/rltoken/7gc6UzxSL81HcuAwklUbuQ "args/kwargs")
-   [JSON encoder and decoder](https://intranet.alxswe.com/rltoken/rGVU9mt57rVURGnjK6n4_Q "JSON encoder and decoder")
-   [unittest module](https://intranet.alxswe.com/rltoken/soictNXCPE18ASL3INoeew "unittest module")
-   [Python test cheatsheet](https://intranet.alxswe.com/rltoken/uI9iskBCcNo5pc7j9Vy86A "Python test cheatsheet")

## Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version  `2.8.*`)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should be documented:  `python3 -c 'print(__import__("my_module").__doc__)'`
-   All your classes should be documented:  `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
-   All your functions (inside and outside a class) should be documented:  `python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder  `tests`
-   You have to use the  [unittest module](https://intranet.alxswe.com/rltoken/soictNXCPE18ASL3INoeew "unittest module")
-   All your test files should be python files (extension:  `.py`)
-   All your test files and folders should start with  `test_`
-   Your file organization in the tests folder should be the same as your project: ex: for  `models/base.py`, unit tests must be in:  `tests/test_models/test_base.py`
-   All your tests should be executed by using this command:  `python3 -m unittest discover tests`
-   You can also test file by file by using this command:  `python3 -m unittest tests/test_models/test_base.py`
-   We strongly encourage you to work together on test cases so that you don’t miss any edge case

### 21. Let's draw it

![enter image description here](https://github.com/MASMIYEN/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/image_2023-10-16_082607011.png?raw=true)

Update the class  `Base`  by adding the static method  `def draw(list_rectangles, list_squares):`  that opens a window and draws all the  `Rectangles`  and  `Squares`:

-   You must use the  [Turtle graphics module](https://intranet.alxswe.com/rltoken/d16zMqYw0c7eQje2XgFvFg "Turtle graphics module")
-   To install it:  `sudo apt-get install python3-tk`
-   To make the GUI available outside your vagrant machine, add this line in your Vagrantfile:  `config.ssh.forward_x11 = true`
-   No constraints for color, shape etc… be creative!

```
guillaume@ubuntu:~/$ cat 101-main.py
#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)

guillaume@ubuntu:~/$ ./101-main.py
....

```

-   Uncommented line in  `/etc/ssh/ssh_config`  that said  `# ForwardX11 no`  and change  `no`  to  `yes`.
-   Then added line  `config.ssh.forward_agent = true`  to my Vagrantfile in addition to  `config.ssh.forward_x11 = true`.
-   Halted my vm with  `vagrant halt`  and started it back up with  `vagrant up --provision`  then  `vagrant ssh`.
-   If you get an error that looks like  `/usr/bin/xauth: timeout in locking authority file /home/vagrant/.Xauthority`, then enter  `rm .Xauthority`  (you may have to  `sudo`).
-   Logout and restart the vm with  `vagrant up --provision`.
-   Test with  `xeyes`. If Xquartz is installed on the Mac OS it should open in an Xquartz window.

**It is your responsibility to request a review for this task from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.**

**Repo:**

-   GitHub repository:  `alx-higher_level_programming`
-   Directory:  `0x0C-python-almost_a_circle`
-   File:  `models/base.py`
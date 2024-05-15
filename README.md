# AirBnB Clone - The Console
The console is the first part of the AirBnB Clone project of the ALX Software Engineering Program. In summary, it encompasses using a command line interpreter to execute the functionality below.

#### Functionality:
* Create a new object (eg: a new User or a new Place)
* Retrieve an object from a file
* Perform operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [Usage](#usage)
* [Authors](#authors)

## Environment
This project is depndent on Ubuntu 22.04 LTS using python3

## Installation
* Clone this repository: `git clone "https://github.com/goonerlabs/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* chmod +x console.py
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py

## Usage
### Interactive mode
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

# Non-interactive mode
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

# Using a file for input
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$


## Authors
Owolabi Adeyemi - [Github](https://github.com/goonerlabs) / [Twitter](https://twitter.com/hanswolfhart)

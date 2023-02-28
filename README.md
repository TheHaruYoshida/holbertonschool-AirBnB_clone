# hbnb - an AirBnB clone :city_sunrise:

    <img src="https://a0.muscache.com/airbnb/static/logos/belo-400x400.png">

## Description

The first step towards building a full web application, this repository contains a back-end console.

### Coding Style :technologist:
All files are written in Python programming language.

### Usage
The hbnb console should work in both interactive and non-interactive mode. In interactive mode, a prompt is printed and it waits for input from the user.
```
$ ./console.py
(hbnb)
```
And in non-interactive mode, a command should be piped:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Console Commands
| Command | Description |
| -------| ----------- |
| `help` | Displays help page |
| `EOF` | Quits the console |
| `quit` | Quits the console |
| `create <class>` | Creates a new instance of a given class with a unique ID and saves it to a JSON file |
| `show <class> <id>` | Prints the string representation of a class instance based on the class name and ID|
| `destroy <class> <id>` | Deletes an instance based on the class name and id and saves it to a JSON file |
| `update` | Updates an instance based on the class name and id by adding or updating attribute and saves changes to a JSON file |
| `all` | Prints all string representation of all instances based or not on the class name |

  
 ## Unit Testing
 Unit tests are stored in the *tests* directory. To run unit tests, run the following command:
 ```
 python3 -m unittest discover tests/test_models
 ```
  
 ## Authors 
- Bruno Carnales
- Santiago Vidarte

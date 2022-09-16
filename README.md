# BankProject

This is a project written in flask and represent a Bank restful api.

## Create a virtual environment

Virtual environments is comonly used if you dont want to install requirements of project in your main interpreter. For that reason you can get a copy of your interpreter in folder of project and active it for use in project.

For create an virtual environment you should install `python3-venv` package :

`apt-get install python3-venv`

But if you got an permission error use `sudo` before this command.

After that put your favorite name in the following command :

`python3 -m venv <name-of-folder>`

Ok, at this point your virtual environment is created. Congratulations !

For working with virtual environment need to "active" it :

`source <folder-name>/bin/activate`

If you use Windows dont need to write `source` before command.

At the end if you finished your work, can deactivate your virtual environment :

`deactivate`

# Usage

For start project and run code you must install requirements.

You can use `pip` to install requirements like this :

`pip install -r Requirements.txt`

And now you can run code with running `main.py`:

`python3 main.py`

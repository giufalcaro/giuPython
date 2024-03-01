### pip and virtual env commands

to install pkgs globaly 

python3 -m pip install requests # requests is the pkg name

python3 -m pip install requests==2.30.0 # this is how we install specific versions

python3 -m pip install -U requests # this is how to update pkgs

python3 -m pip uninstall requests # unistall pkgs

python3 -m pip list # lists all pkgs installed globaly 

### virtual envs are used to install non global modules 

python3 -m venv .venv # creates a virtual env folder for our project

source .venv/bin/activate # activate virtual env # we need to do this everytime we are working on a project

### then we can install pkgs localy 

pip install python-dotenv

pip install -r requirements.txt 

### we can also create a list of requirements for a project

pip freeze > requirements.txt

### to make the env work with vscode 
I had to update the settings.json with:

``` {
    "python.defaultInterpreterPath": "/Users/giulianofalcaro/Documents/PROJETOS/PYTHONCOURSE/virtualEnv/.venv/bin/python"
} ```

And then select the defaultInterpreterPath on the select interpreter menu of vscode

to run scritps I had to activate the env on the terminal and use python to run scripts instead of python3
# py-fastapi-react-nickramsay-dev

## Installation 
### Install a C compiler
Ensure you have a C compiler installed. `pyenv` requires a C compiler such as `gcc` or `clang`. 

Debian11 (bullseye) doesnt come with a C compiler. For Debian11 (bullseye), install `gcc` alongside a build tools install:
```sh
sudo apt update
sudo apt -y install build-essential libffi-dev libssl-dev zlib1g-dev
```

### Install `pyenv`
```sh

# download and run pyenv installer
curl https://pyenv.run | bash

# configure shell
SHELL_RC="$HOME/.bashrc" # change to .zshrc if need be
cat <<- EOF >> $SHELL_RC
    export PYENV_ROOT="\$HOME/.pyenv"
    export PATH="\$PYENV_ROOT/bin:\$PATH"
    eval "$(pyenv init -)"
EOF

# reset shell with pyenv configured
source $SHELL_RC

# install python3.11.3
pyenv install 3.11.3
pyenv local 3.11.3
poetry install
```

### Install poetry
```sh
curl -sSL https://install.python-poetry.org | python3 -

# add poetry to path
echo "export PATH=\"/home/server/.local/bin:\$PATH\"" >> $HOME/.bashrc
source $HOME/.bashrc
```

### Configure sudoers file
Add the following lines to your `/etc/sudoers` file.
```
Defaults    env_keep += "PYENV_ROOT"
#DEFAULTS    secure_path += "" 
```

## Usage
```sh
pyenv local 3.11.3
pyenv which python | xargs poetry env use
poetry install
sudo -E poetry run start
```

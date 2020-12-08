[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/u1234x1234/kdd2020-graph-adversarial-attacks-defence/blob/master/LICENSE)

# pydropbear

Lightweight SSH server shipped as a python package.

Features:

* Does not require system-wide installation
* Small size (<3MB with prebuilt binaries)
* An alternative to Openssh server or servers on top of [paramiko](https://github.com/paramiko/paramiko).

# Installation

```
pip install pydropbear==0.0.6
```

# Usage

Command line:
```bash
python -m pydropbear --port 8444
```
SSH server will be started in a foreground.

Now you can use ssh client:
```bash
ssh localhost -p 8444
```
Also you can start server in a background process:
```bash
python -m pydropbear --port 8444 --bg 1
```

As a library:
```python
from pydropbear import start_ssh_server
start_ssh_server(8444)
```

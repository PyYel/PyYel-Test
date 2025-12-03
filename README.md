
# PyYel – Private Library Installation Guide

This repository depends on three private Python packages:

- PyYel-DevOps
- PyYel-CloudOps
- PyYel-MLOps

All dependencies are declared in `requirements.txt`.  
To install them locally using pip, you must configure Git authentication using one of the supported methods below.

## Installing Dependencies

1. Create or activate your virtual environment:

```bash
python3 -m venv .venv
```

2. Activate your environement
```bash
# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate 
```

3. Setup a secret store for your Git token:
```
git config --global credential.helper store
```

4. Force login using your Git username and token as password:
```
git ls-remote https://github.com/PyYel/PyYel-DevOps.git
```

5. Install the libs as requirements:
```
pip install -r requirements.txt
```

## Adding PyYel libs as dependencies


# PyYel – Private Library Installation Guide

This repository depends on three private Python packages:

- PyYel-DevOps
- PyYel-CloudOps
- PyYel-MLOps

All dependencies are declared in `requirements.txt`.  
To install them locally using pip, you must configure Git authentication using one of the supported methods below.

## Installing PyYel libs as dependencies

### Using uv (recommended)

uv is a modern packet manager build upon python and pip for faster packet installation and management.

1. Install uv to your global python installation:

```bash
# You need Python already installed
pip install uv
```

2. Create a venv using uv:

```bash
# Replace .venv with your desired venv name (keeping .venv is recommended)
uv venv .venv
```

3. Activate it:

```bash
# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate 
```

4. Install the libs as requirements:

```bash
# Edit the requirements to cherry pick the extras you are going to use
uv pip install -r requirements.txt
```


### Using python 

1. Make a venv:

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

3. Install the libs as requirements:
```
pip install -r requirements.txt
```

## Adding PyYel libs as dependencies

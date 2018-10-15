# sketch

## Mandelbrot

`python mandelbrot.py`

## Windows Setup

1. Install Choco from <https://chocolatey.org/install>
2. Install python via `choco install python`
  1. Verify `python --version` is 3.7+
3. Open PowerShell (Admin) and `cd` this folder.
4. Create virtualenv via `python -m venv env`
5. Activate venv via `.\env\Scripts\Activate.ps1`
  1. You may see an UnauthorizedAccess error message. Follow the link in the
     message and run Set-ExecutionPolicy as needed. e.g.
     `Set-ExecutionPolicy -ExecutionPolicy Unrestricted`
5. `pip install -r requirements.txt`

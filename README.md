# HTMX + FastAPI Starter App

The concept is simple, this is a start app that includes the following modules:
- HTMX
- Uvicorn
- Jinja2
- FastAPI

On top of that, it has neat little QOL features such as:
- Hot reload
- Pre-cooked routes
- Defined requirements
- Neat package structure

This is all built for Python 3, btw.

# Deets

1. Clone this app however you see fit
2. Add a Python virtualnv, `.gitignore` assumes `.venv` but adjust to your liking
3. Source your new environment
4. Install requirements, `pip install -r requirements.txt`
5. Code your heart out

## Running it

To take advantage of the Hot Reload feature, just execute this application like so:
- MacOS and Linux: `DEBUG=true uvicorn app:app --reload`
- Windows:
  - `set DEBU=true`
  - `uvicorn app:app --reload`

Bummer for those using Safari, Hot Reloading doesn't seem to work there.  Just use some other browser for the time being.

~ Enjoy! ~

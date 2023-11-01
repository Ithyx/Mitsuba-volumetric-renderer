# An attempt at a simple volumetric integrator for Mitsuba 3

This project was an (unfinished) attempt at re-creating a volume path tracing integrator for the Mitsuba 3 renderer.
Here is a sample output it can produce:

![An example of what this integrator can make](images/example_render.png)

## How to run
### Prerequisites
* Python3 with the venv module (tested on python 3.11.5)
* A matplotlib display backend (most likely tk)

### Running the program
* python -m venv .venv
* source .venv/bin/active
* python -m pip install -r requirements.txt
* python src/main.py

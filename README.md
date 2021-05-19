# What is this

This is an exploration on the idea of static SSR and a complete
discontinuous break between build time and runtime. I have an
off-the-shelf SvelteKit app that I added a couple "airplane" routes
to, one is a parameterless list view and one is detail view that
uses an ID from route params. Dealing with dynamic routes in a
static SSR world is what this is all about.

Just to be extra sure they're separated I'm using Python for the
runtime part.

# Schedule of ports

* 3000: SvelteKit dev server in `/sv`
* 3001: A simple Python API server that gives you JSON on a 500ms delay, in `/api`
* 3002: A production-like Python web server that serves the statically
  rendered /build directory of SvelteKit, in `/web`

# Startup

The SvelteKit part is obvious, just `npm i` then `npm run dev`, then
`npm run build` to populate the `/build` folder which the Python web
server looks at to see everything running integrated.

For the Python apps, just be sure you're on Python 3.9 (`python -V`)
and run them with `python app.py`. The api one has dependencies on
Flask so you want a `pip install -r requirements.txt` (possibly should
be done in a venv but not sure if that's necessary), then 
`python app.py` to start up. I *love* Python the language but do not
love the package system. Wheel, pip, venv, virtualenv, who really
understands that stuff anyway?

# Flask framework 101

### create a virtual env

```bash
pipenv shell # move to venv
pipenv install <package> # install packages
```

### define env

```
export FLASK_APP=hello
export FLASK_ENV=development
```

### folder structure

templates

- jinja templating engine

static

- static files
    - url_for('static', filename="path/to/file")


### create a cookie
session[<key>] = "..."
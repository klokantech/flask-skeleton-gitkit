# Flask application skeleton

Flask application should be run directly with docker-compose.
There will be a different docker-compose.yml for production (draft is available
in `docker-compose.production.yml` and it will be stored in klokantech/deploy)
and no `docker-compose build` - usage of prebuilt docker images is assumed.

```shell
$ docker-compose build
$ docker-compose run --rm app /venv/bin/python3 manage.py db upgrade
$ docker-compose up
```

Sample accounts:

- john.doe@example.com
- admin@example.com


Production images must have explicit image names.
Production containers must have explicit container names if they
are run on the same machine as development.


Logging needs to be configured from docker-compose.yml via environment variables.

`LOG_LEVEL` and `LOG_FILE` should be configured there. Set `LOG_LEVEL` with one
from:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

to configure minimal logging level. `LOG_FILE` should be a path to log file, 
without this variable logger will outputs to stdout.

Logging example:
```
from flask import render_template

from ..base import app


@app.route('/')
def index():
    app.logger.debug("This is debug message")
    app.logger.info("This is info message")
    app.logger.warning("This is warning message")
    app.logger.error("This is error message")
    app.logger.critical("This is critical message")
    return render_template('index.html')
```

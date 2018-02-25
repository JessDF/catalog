#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/catalog/")

activate_this = '/var/www/catalog/catalog/venv/bin/activate_this.py'
with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

from catalog import app as application
application.secret_key = 'aitlWPNmkdTzjUsSpZHCj0gR'

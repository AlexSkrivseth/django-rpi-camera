from .settings import *

import os

# https://miniwebtool.com/django-secret-key-generator/
SECRET_KEY=os.getenv(
                        'DJANGO_SECRET_KEY',
                        'ive$3p@mv$h*l5iy#y3b&^4t@-kvjr!%vi$*5p_a9(yj86%94z')

DEBUG=False

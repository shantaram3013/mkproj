import datetime

from licenses.MIT import MIT
from licenses.GPL import GPLv3
from licenses.BSD import ZERO, TWO, THREE
from licenses.APACHE import APACHE2

year = datetime.datetime.now().date().strftime("%Y")

licenses = {
    "0BSD": ZERO,
    "2BSD": TWO,
    "3BSD": THREE,
    "Apache2": APACHE2,
    "GPLv3": GPLv3,
    "MIT": MIT,
}
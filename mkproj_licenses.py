import datetime

from licenses.MIT import MIT
from licenses.GPL import GPLv3

year = datetime.datetime.now().date().strftime("%Y")

licenses = {
    "MIT": MIT,
    "GPLv3": GPLv3
}
import nest
from nest import utils as nest_utils
import time

username = 'support@vistacourt.net'
password = '3856Vista!'
napi = nest.Nest(username, password)
temp = 0
fahrenheit = nest_utils.c_to_f(temp)
temp == nest_utils.f_to_c(fahrenheit)

while True:

    for structure in napi.structures:
        if structure.away == False:
            print 'Home'
        else:
            print 'Away'
    for device in structure.devices:
        print 'Celcius: %0.1f' % device.temperature
        print 'Fahrenheit:', fahrenheit

    time.sleep(10)



from nest import utils as nest_utils
temp = 23.5
fahrenheit = nest_utils.c_to_f(temp)
temp == nest_utils.f_to_c(fahrenheit)

#Converter
from sense_hat import SenseHat
sh = SenseHat()
off = (0, 0, 0)


def binary(time, colrow, direction, color):
    '''Takes a time format, a collumn/row number, a directional variable and a color value'''
    binary_str = "{0:8b}".format(time)
    for v in range(0, 8):
            if binary_str[v] == '1':
                if direction == 1:
                    sh.set_pixel(colrow, v, color)
                else:
                    sh.set_pixel(v, colrow, color)
            else:
                if direction == 1:
                    sh.set_pixel(colrow, v, off)
                else:
                    sh.set_pixel(v, colrow, off)


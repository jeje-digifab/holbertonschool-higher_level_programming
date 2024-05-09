#!/usr/bin/python3

for dec in range(0, 99):
    hexa = ""
    quotient = dec
    remainder = 0

    while quotient > 0:
        remainder = quotient % 16
        quotient = quotient // 16
        if remainder < 10:
            hexa = str(remainder) + hexa
        else:
            hexa = chr(remainder + 87) + hexa

    if len(hexa) == 0:
        hexa = "0"
    elif len(hexa) == 1:
        hexa = "0" + hexa

    print("{} = 0x{}".format(dec, hexa))

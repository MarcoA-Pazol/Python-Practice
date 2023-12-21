def celsius_to_farenheit():
    #This method transforms celsius to farenheit
    while True:
        #Variables
        celsius_input = int(input("Type how many celsius you want to transform to farenheit:"))
        farenheit_output = (celsius_input * (9/5)) + 32

        print(f"{celsius_input}°C = {farenheit_output}°F")

def degrees_to_radians():
    #This method transforms degrees to radians.
    while True:
        #Constants
        PI = 3.1416

        #Variables
        degrees_input = int(input("Type how many degrees you want to transform to radians:"))
        radians_output = degrees_input * (PI / 180)

        print(f"{degrees_input} degrees are {radians_output} radians.")

celsius_to_farenheit()
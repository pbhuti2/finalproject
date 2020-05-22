# welcome to unit converter
# convert units
# loop converting units
# give option to quit

'''
Created on May 8, 2020
@author: pbhuti2
'''
converto = True

while(converto == True):
    print("welcome to David's Converter")
    kilometers = input("Enter the number of kilometers you wish to convert or type yeet to stop: ")
    if kilometers.isdigit() == True:
        #deal numbers here
        miles = round( float(kilometers) / 1.609, 2)
        print(miles)
    else:
        #deal with words
        stop = "yeet"
        if kilometers == "yeet":
            break

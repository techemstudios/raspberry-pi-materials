"""
Title: Pi Material Count
Date: 08/07/2017

Material tracker for all materials needed for Rapsberry Pi classes and camps.

Python 2.7

"""

pis = {
    'Pi 2011.12': '2',
    'Pi Model B+ v 1.2': '3',
    'Pi Model A+ v 1.1': '1',
    'Pi 2 Model B v 1.1': '4',
    'Pi 3 Model B v 1.2': '5'
    }
materials = {
    '5.25V-2.4A Power Supply': '4',
    '8GB SD card': '4',
    '16GB SD card': '2',
    'Ribbon Cables': '6',
    'Breadboards': '3'
    }

needed_materials = {
    'Pi 3 Model B v 1.2': '2',
    '5.25V-2.4A Power Supply': '1',
    '8GB SD card or 16GB SD card': '5',
    'Breadboards': '2'
    }

active = True

while active: 
    show_me = raw_input("\nFor list of available pis type: 'pi'" + "\nFor a list of materials related to the pi type: 'materials'" + "\nType 'order' to see what needs to be ordered." + "\nType 'quit' to end session " + "\n")   
    
    if show_me == 'pi':
        for key, value in pis.items():
            print("\nModel: " + key)
            print("Count: " + value)
    
    elif show_me == 'materials':
        for key, value in materials.items():
            print("\nModel: " + key)
            print("Count: " + value)
            
    elif show_me == 'order':
        for key, value in needed_materials.items():
            print("\nPart: " + key)
            print("Count: " + value)

    elif show_me == 'quit':
        active = False
        print("\n\tThank you for using the Tech Em Studios materials tracker!")
        raw_input("\n\n\tpress the enter key to exit.")


    
        
    

    
    

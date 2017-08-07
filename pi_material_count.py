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

active = True

while active: 
    show_me = raw_input("\nFor list of available pis type: 'pi'" + "\nFor a list of materials related to the pi type: 'materials' :" + "\nType 'quit' to end session: " + "\n")   
    
    if show_me == 'pi':
        for key, value in pis.items():
            print("\nModel: " + key)
            print("Count: " + value)
    
    if show_me == 'materials':
        for key, value in materials.items():
            print("\nModel: " + key)
            print("Count: " + value)

    elif show_me == 'quit':
        active = False
        raw_input("\n\npress the enter key to exit.")


    
        
    

    
    

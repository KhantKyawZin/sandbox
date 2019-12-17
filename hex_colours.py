color ={"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
        "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
        "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
        "azure1": "#f0ffff", "azure2": "#e0eeee", "azure3": "#c1cdcd",
        "azure4": "#838b8b", "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

name_colour = input("Enter a name of the colour:(input 0 to exit) ")
while name_colour != "" or name_colour == "0":
    if name_colour == "0":
        print("Thanks for using the program :D")
        break
    print("The code for \"{}\" is {}".format(name_colour, color.get(name_colour)))
    name_colour = input("Enter a name of the colour:(input 0 to exit) ")

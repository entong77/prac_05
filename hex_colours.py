HEX_COLOURS = {"Honeydew1": "#f0fff0", "Honeydew2": "#e0eee0",
               "Honeydew3": "#c1cdc1", "Honeydew4": "#838b83",
               "Ivory1": "#fffff0", "Ivory2": "#eeeee0",
               "Ivory3": "#cdcdc1", "Ivory4": "#8b8b83",
               "Jade": "#00a86b", "Jasmine": "#f8de7e"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             HEX_COLOURS.get(colour_name)))
    colour_name = input("Enter a colour name: ")

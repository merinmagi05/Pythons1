#Print out all colors from color-list1 not contained in color-list2.
color_list1=set(["Black","Blue","Green","Red","Violet"])
color_list2=set(["White","Blue","Orange","Black","Green"])
print(color_list1)
print("The Colours from color_list1 not contained in colour_list2 is")
print(color_list1.difference(color_list2))
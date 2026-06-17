import Actions
import os

Filters = ["BLUR", "CONTOUR", "DETAIL", "EDGE ENHANCE", "EDGE ENHANCEMORE", "EMBOSS", "FIND EDGES", "SHARPEN", "SMOOTH", "SMOOTH MORE"]
smallFilters = [str(x)+ "." + Filters[x-1].title() for x in range(1, len(Filters)+1)]

print("Hello, this is a fast edit photo")
Again = True
count = 0
while Again: 

    print("Enter name's photo(Example: Example.png)")
    YourPhoto = input(">>>")
    Needed_photo = Actions.open_img(YourPhoto)

    while Needed_photo == "Again":
        print("Enter name's photo(Example: Example.png)")
        YourPhoto = input(">>>")
        Needed_photo = Actions.open_img(YourPhoto)

    print("You can enter either name of color like 'wheat' or RGB like that '255, 255, 255' or write 'empty' to skip")
    YourColor = input(">>>") 
    Color_Image = Actions.create_new_img(Needed_photo, YourColor)

    while Color_Image == "Again":
        print("You can enter either name of color like 'wheat' or RGB like that '255, 255, 255' or write 'empty' to skip")
        YourColor = input(">>>")
        Color_Image = Actions.create_new_img(Needed_photo, YourColor)

    print("Enter a filter(or a number) or 'empty' to skip:")
    print("\n".join(smallFilters))
    Your_Filter = input(">>>")
    Filtered = Actions.useFilter(Needed_photo, Your_Filter)

    while Filtered == "Again":
        print("Enter a filter(or a number) or 'empty' to skip:")
        print("\n".join(smallFilters))
        Your_Filter = input(">>>")
        Filtered = Actions.useFilter(Needed_photo, Your_Filter)
    Checkname = "Edited_"+YourPhoto
    name = YourPhoto
    if not os.path.exists(Checkname):

        if Color_Image == "skip":
            if Filtered == "skip":
                Needed_photo.save("Edited_"+name)
            else:
                Filtered.save("Edited_"+name)
        else:
            if Filtered == "skip":
                Blended = Actions.mixxa(Needed_photo, Color_Image)
                Blended.save("Edited_"+name)
            else:
                Blended = Actions.mixxa(Filtered, Color_Image)
                Blended.save("Edited_"+name)

        print("Saved!")
    else:
        count+= 1
        if Color_Image == "skip":
            if Filtered == "skip":
                Needed_photo.save("Edited"+str(count)+"_"+name)
            else:
                Filtered.save("Edited"+str(count)+"_"+name)
        else:
            if Filtered == "skip":
                Blended = Actions.mixxa(Needed_photo, Color_Image)
                Blended.save("Edited"+str(count)+"_"+name)
            else:
                Blended = Actions.mixxa(Filtered, Color_Image)
                Blended.save("Edited"+str(count)+"_"+name)
        print("Saved!")
    print("Do you want to edit another picture?(Y/N)")
    Again = input(">>>")

    if Again.upper() == "Y":
        Again = True
    else:
        Again = False

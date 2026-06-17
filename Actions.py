from PIL import Image, ImageFilter
from random import choice
import os

defaulting = ["black", "white", "wheat", "blue", "green", "red", "yellow", "purple"]
Filters = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SHARPEN", "SMOOTH", "SMOOTH_MORE"]

filter_dict = {
    "BLUR": ImageFilter.BLUR,
    "CONTOUR": ImageFilter.CONTOUR,
    "DETAIL": ImageFilter.DETAIL,
    "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
    "EDGE_ENHANCE_MORE": ImageFilter.EDGE_ENHANCE_MORE,
    "EMBOSS": ImageFilter.EMBOSS,
    "FIND_EDGES": ImageFilter.FIND_EDGES,
    "SHARPEN": ImageFilter.SHARPEN,
    "SMOOTH": ImageFilter.SMOOTH,
    "SMOOTH_MORE": ImageFilter.SMOOTH_MORE,
}

#Open Image
def open_img(imGName):
    try:
        Img = Image.open(imGName)
    except FileNotFoundError:
        print("No such file")
        return "Again"
    Img = Img.resize(Img.size)
    Img = Img.convert("RGBA")
    return Img

#Create new image
def create_new_img(imG, in_color):
    in_color.replace(" ", "")

    if in_color.lower() == "empty":
        return "skip"
    
    if in_color.isalpha():
        try:
            New = Image.new("RGBA", (imG.width, imG.height), in_color)
            New = New.resize(imG.size)

        except ValueError:
            original = choice(defaulting)
            New = Image.new("RGBA", (imG.width, imG.height), original)
            New = New.resize(imG.size)
            print(f"You entered the wrong color, and your color is {original}")
            print("Do you want to use this color?(Y/N)")
            s = input(">>>")
            if s == "N":
                print("Change the color")
                return "Again"
            return New
        return New
    else:
        try:
            R = int(in_color[:in_color.find(",")])
            G = int(in_color[in_color.find(",")+1:in_color.rfind(",")])
            B = int(in_color[in_color.rfind(",")+1:])
        except ValueError:
            print("Something went wrong...")
            print("Change the color")
            return "Again"
        RGB_tuple = (R, G, B)
        New = Image.new("RGBA", (imG.width, imG.height), RGB_tuple)
        New = New.resize(imG.size)
    return New

#Use filter
def useFilter(imG, Filter):
    if Filter.isdigit():
        Filter = int(Filter)
        try:
            Current_Filter = filter_dict[Filters[Filter-1]]
            New = imG.filter(filter=Current_Filter)
            return New
        except IndexError:
            print("You entered wrong number, change the Filter")
            return "Again"
        
    else:
        if Filter.lower() == "empty":
            return "skip"

        Filter = Filter.upper()
        Filter = Filter.replace(" ", "_")
        try:
            Current_Filter = filter_dict[Filter]
            New = imG.filter(filter=Current_Filter)
            return New
        except KeyError:
            print("You entered wrong Filter, change the Filter")
            return "Again"

def mixxa(imG, New):
    if New == "skip":
        print(imG)
        return imG
    mixed = Image.blend(New, imG, 0.5)
    return mixed

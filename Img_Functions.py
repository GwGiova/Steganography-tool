#This function controls the version of the Bitmap header
def look_At_Version(file_Bmp):

    #I go to offset 14 because there is a number that indicates the lenght of the next header
    #If the lenght is 40 it means it is a infoheader, otherwise a core header
    file_Bmp.seek(14)

    #I convert the size read to an int number
    #I read 4 bytes because the field occupies 4 bytes
    header_Size = int.from_bytes(file_Bmp.read(4), "little")

    #I check if it is an info header
    if(header_Size == 40):

        #BITMAPINFOHEADER
        return 0
    
    #I check if it is a core header
    elif(header_Size == 12):

        #BITMAPCOREHEADER
        return 1

#I call this function to look where the pixel data is.
#In BMP the location of the pixel data section is up to the program that creates the image
def find_Pixel_Data(file_Bmp):

    #I go to offset 10 because it tells me where the pixel data is
    file_Bmp.seek(10)

    #I convert the offset from hex to int
    offset = int.from_bytes(file_Bmp.read(4), "little")

    #I return the offset
    return offset

#I calculate the pixel data size, it can serve in future implementations if i want to check whether 
#The text that i inserted is too long for entering the image
def calculate_Pixel_Data_Size(file_Bmp, offset):

    #I go to offset 2 fetch the image dimension
    file_Bmp.seek(2)

    #Total file size, fetched by going offset 2 and reading the next 4 bytes
    file_Size = int.from_bytes(file_Bmp.read(4), "little")

    #I calculate the pixel data size, that is equal to the total file size - the offset where the pixel data is
    #*Almost all the time the pixel data is the last in the file but this isnt 100% true*
    pixel_Data_Size = file_Size - offset

    #I return the pixel data size
    return pixel_Data_Size
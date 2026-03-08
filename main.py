import ASCII_Conversions
import Img_Functions





#The "CORE" of the program, the function used to write the content in the file
def hide_Image(text_To_Hide, file_Bmp):

    #I retrieve the offset pixel data
    offset_Pixel_Data = Img_Functions.find_Pixel_Data(file_Bmp)

    #I go with the file pointer to the offset pixel data, because i want to write there
    file_Bmp.seek(offset_Pixel_Data)

    #I use a counter to count all the characters i inserted
    counter = 0

    #FOR used for every character in the text that i want to hide
    for character in text_To_Hide:

        #I convert the character of my text into a string of 8 bits, representing its byte format
        character_To_Bits = ASCII_Conversions.from_ASCII_To_Bit(character)

        #Now with this FOR i read the file's content byte at a byte
        #The "bit" variable represent every bit of the character i wrote 
        for bit in character_To_Bits:

            #I read a byte from the image (It shifts by 1 everytime the function is called)
            byte_From_The_Image = file_Bmp.read(1)

            #I convert the byte format to a string representing the byte into his bits
            #EX: "0x0A" --> "00001010"
            Bits_From_The_Byte = format(byte_From_The_Image[0], "08b")

            #I look if the last byte's bit correspond to the bit of the character
            #If it does, thats ok, otherwise i switch the bit
            if bit != Bits_From_The_Byte[-1]:

                #Switch the bit from 0 to 1
                if Bits_From_The_Byte[-1] == "0":
                    Bits_From_The_Byte = Bits_From_The_Byte[:-1] + "1"
                
                #Switch the bit from 1 to 0
                else:
                    Bits_From_The_Byte = Bits_From_The_Byte[:-1] + "0"

    
            counter += 1

            #I go to the previous file location (because by calling the file i shifted to 1 upward)
            file_Bmp.seek(-1,1)
            #I write the modified bit in the file
            file_Bmp.write(int(Bits_From_The_Byte,2).to_bytes(1,"little"))

    return counter

#I add a NULL character at the end of the text i inserted
def add_NULL_Character(file_Bmp, counter):

    #I find the offset (the same as before)
    offset = Img_Functions.find_Pixel_Data(file_Bmp)

    #I go to the offset + counter, it means:
    #I go to the offset + the number of the characters that i inserted, so the last character can be a NULL
    file_Bmp.seek(offset + counter)


    for i in range(8):

        #I read the byte from the image
        byte_From_The_Image = file_Bmp.read(1)

        #I convert the byte from hex to bits
        Bits_From_The_Byte = format(byte_From_The_Image[0], "08b")

        #The NULL characters corresponds to "00000000" so if i find a "1" i convert it into a 0
        #So i can have 8 consecutive 0s
        if Bits_From_The_Byte[-1] == "1":
            
            #Switching from 1 to 0
            Bits_From_The_Byte = Bits_From_The_Byte[:-1] + "0"

        #I go to the previous file location (because by calling the file i shifted to 1 upward)
        file_Bmp.seek(-1, 1)

        #I write the modified bit in the file
        file_Bmp.write(int(Bits_From_The_Byte, 2).to_bytes(1, "little"))

        




#Start of the program

#I create the file object, which represent the image in the file path
file = open("C:\\Users\\userl\\Desktop\\Steganography Tool\\Images\\bmp_24.bmp", "rb+")

#For both if and elif i call the function look_At_Version to see whether the file has
#A bitmap core header or a info header. Those variables are unused but can serve if a 
#Programmer wanted to make changes on this program

if(Img_Functions.look_At_Version(file) == 0):

    bitmap_Core_Header = False

    bitmap_Info_Header = True

elif(Img_Functions.look_At_Version(file) == 1):

    bitmap_Core_Header = True

    bitmap_Info_Header = False

#I ask for the text that the user wants to hide in the image
text = input("Insert the text that you want to hide in the image: ")

#I call the function used to hide the text in the image, i return a counter
#That counts the number of characters that i inserted
counter_Of_Character_Inserted = hide_Image(text, file)

#I add a NULL character to make the Steganography reader understand to stop reading after that
add_NULL_Character(file, counter_Of_Character_Inserted)

#I Close the file
file.close()
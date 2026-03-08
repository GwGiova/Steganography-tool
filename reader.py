import ASCII_Conversions
import Img_Functions

#I create the file object, which represent the image in the file path
file = open("C:\\Users\\userl\\Desktop\\Steganography Tool\\Images\\bmp_24.bmp", "rb+")

#I fetch the offset of the pixel data
offset = Img_Functions.find_Pixel_Data(file)

#I with the file pointer to the offset, where i will be reading the hidden message
file.seek(offset)

#Buffer used to contain groups of 8 bits (1 byte), that represent a character
letters_Buffer = []

#Counter that is used to calculate when i can read from the buffer.
counter = 0

#Hidden text in the image
hidden_Text = ""

#This cycle works until i call the break
while True:

    #I read the byte from the image
    byte_From_The_Image = file.read(1)

    #I convert the byte from hex to bits
    Bits_From_The_Byte = format(byte_From_The_Image[0], "08b")

    #I append to the buffer the last bit of the byte i just read
    letters_Buffer.append(Bits_From_The_Byte[-1])

    #I increment the counter
    counter += 1

    #I check if the buffer has 8 elements in it, if it has, it means that 
    #I've read a full character and i can decode it with the from_Bits_To_ASCII function
    if(counter % 8 == 0):

        #I check if in the buffer there is "00000000" which means i'm reading the "NULL" character
        #And that my message is finished
        if(letters_Buffer[0] == "0" and letters_Buffer[1] == "0" and letters_Buffer[2] == "0" and letters_Buffer[3] == "0" and letters_Buffer[4] == "0" and letters_Buffer[5] == "0" and letters_Buffer[6] == "0" and letters_Buffer[7] == "0"):

            #Used to exit from the While cycle
            break

        else:

            #I calculate the character corrisponding to the buffer value and add it to the hidden text
            hidden_Text += ASCII_Conversions.from_Bits_To_ASCII(letters_Buffer[0] + letters_Buffer[1] + letters_Buffer[2] + letters_Buffer[3] + letters_Buffer[4] + letters_Buffer[5] + letters_Buffer[6] + letters_Buffer[7])

            #I empty the buffer
            letters_Buffer = []

#I print the hidden text
print(hidden_Text)

#I close the file
file.close()

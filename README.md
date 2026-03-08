This programs allow you to hide a text inside a image.
The image must be in .bmp format to work and support **BITMAPCOREHEADER** or **BITMAPINFOHEADER**.
The program takes the image, calculate where the pixel data is, and start reading every byte forward.
Let's do a pratical example: I want to hide the word "hello" in the image.
The pixel data starts like this

     R          G          B             R          G         B
[00110110] [01010111] [00001111]    [01101011] [11010111] [00111010] ...

Those values inside every field represent the color intensity of every R-G-B color and initially are random, has no meaning for us.

If we change the LSB (Less Significant Bit) of every field, the color intensity will much be the same, no eye could see the change.

So in a few words this is what the program does:

You write the word / phrase that you want to hide.

The program takes the first letter / character and transform it in his ASCII code.

Ex: "hello" ---> 1st letter: h ----> In ASCII: 01101000

It compares the first bit of the ASCII character with the LSB of the first byte, if they are equal we move on to the second byte, 
otherwise we reverse the LSB value, to make it match the character first bit, and so on..

So the first byte's LSB represent the first bit of the character and so on.

The 9th byte's LSB will represent the 2nd character first bit.

When the function returns to the program another function is called: add_NULL_Character()
The NULL character serves to the image reader to understand when our text has finished.
It's simple to see it, because the null character is represented by all 0s.

The reader does the opposite.
It reads every LSB of every byte, in group of 8s and translate it in its ASCII character.
When the program sees 8 consecutive 0s, it understand that that is the NULL character and stops reading.

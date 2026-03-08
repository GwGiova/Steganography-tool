def from_ASCII_To_Bit(string):

    if string == " ":
        return "00100000"
    
    if string == "!":
        return "00100001"
    
    if string == '"':
        return "00100010"
    
    if string == "#":
        return "00100011"
    
    if string == "$":
        return "00100100"
    
    if string == "%":
        return "00100101"
    
    if string == "&":
        return "00100110"
    
    if string == "'":
        return "00100111"
    
    if string == "(":
        return "00101000"
    
    if string == ")":
        return "00101001"
    
    if string == "*":
        return "00101010"
    
    if string == "+":
        return "00101011"
    
    if string == ",":
        return "00101100"
    
    if string == "-":
        return "00101101"
    
    if string == ".":
        return "00101110"
    
    if string == "/":
        return "00101111"

    if string == "0":
        return "00110000"
    
    if string == "1":
        return "00110001"
    
    if string == "2":
        return "00110010"
    
    if string == "3":
        return "00110011"
    
    if string == "4":
        return "00110100"
    
    if string == "5":
        return "00110101"
    
    if string == "6":
        return "00110110"
    
    if string == "7":
        return "00110111"
    
    if string == "8":
        return "00111000"
    
    if string == "9":
        return "00111001"

    if string == ":":
        return "00111010"
    
    if string == ";":
        return "00111011"
    
    if string == "<":
        return "00111100"
    
    if string == "=":
        return "00111101"
    
    if string == ">":
        return "00111110"
    
    if string == "?":
        return "00111111"

    if string == "@":
        return "01000000"

    if string == "A":
        return "01000001"
    
    if string == "B":
        return "01000010"
    
    if string == "C":
        return "01000011"
    
    if string == "D":
        return "01000100"
    
    if string == "E":
        return "01000101"
    
    if string == "F":
        return "01000110"
    
    if string == "G":
        return "01000111"
    
    if string == "H":
        return "01001000"
    
    if string == "I":
        return "01001001"
    
    if string == "J":
        return "01001010"
    
    if string == "K":
        return "01001011"
    
    
    if string == "L":
        return "01001100"
    
    if string == "M":
        return "01001101"
    
    if string == "N":
        return "01001110"
    
    if string == "O":
        return "01001111"
    
    if string == "P":
        return "01010000"
    
    if string == "Q":
        return "01010001"
    
    if string == "R":
        return "01010010"
    
    if string == "S":
        return "01010011"
    
    if string == "T":
        return "01010100"
    
    if string == "U":
        return "01010101"
    
    if string == "V":
        return "01010110"
    
    if string == "W":
        return "01010111"
    
    if string == "X":
        return "01011000"
    
    if string == "Y":
        return "01011001"
    
    if string == "Z":
        return "01011010"

    if string == "[":
        return "01011011"
    
    if string == "\\":
        return "01011100"
    
    if string == "]":
        return "01011101"
    
    if string == "^":
        return "01011110"
    
    if string == "_":
        return "01011111"
    
    if string == "`":
        return "01100000"

    if string == "a":
        return "01100001"
    
    if string == "b":
        return "01100010"
    
    if string == "c":
        return "01100011"
    
    if string == "d":
        return "01100100"
    
    if string == "e":
        return "01100101"
    
    if string == "f":
        return "01100110"
    
    if string == "g":
        return "01100111"
    
    if string == "h":
        return "01101000"
    
    if string == "i":
        return "01101001"
    
    if string == "j":
        return "01101010"
    
    if string == "k":
        return "01101011"
    
    if string == "l":
        return "01101100"
    
    if string == "m":
        return "01101101"
    
    if string == "n":
        return "01101110"
    
    if string == "o":
        return "01101111"
    
    if string == "p":
        return "01110000"
    
    if string == "q":
        return "01110001"
    
    if string == "r":
        return "01110010"
    
    if string == "s":
        return "01110011"
    
    if string == "t":
        return "01110100"
    
    if string == "u":
        return "01110101"
    
    if string == "v":
        return "01110110"
    
    if string == "w":
        return "01110111"
    
    if string == "x":
        return "01111000"
    
    if string == "y":
        return "01111001"
    
    if string == "z":
        return "01111010"

    if string == "{":
        return "01111011"
    
    if string == "|":
        return "01111100"
    
    if string == "}":
        return "01111101"
    
    if string == "~":
        return "01111110"
    
    if string == "È":
        return "11001000"
    
    if string == "É":
        return "11001001"
    
    if string == "Ì":
        return "11001100"
    
    if string == "Ò":
        return "11010010"
    
    if string == "Ù":
        return "11011001"
    
    if string == "à":
        return "11100000"
    
    if string == "è":
        return "11101000"
    
    if string == "é":
        return "11101001"
    
    if string == "ì":
        return "11101100"
    
    if string == "ò":
        return "11110010"
    
    if string == "ù":
        return "11111001"
    

def from_Bits_To_ASCII(bits):

    if bits == "00100000":
        return " "
    
    if bits == "00100001":
        return "!"
    
    if bits == "00100010":
        return '"'
    
    if bits == "00100011":
        return "#"
    
    if bits == "00100100":
        return "$"
    
    if bits == "00100101":
        return "%"
    
    if bits == "00100110":
        return "&"
    
    if bits == "00100111":
        return "'"
    
    if bits == "00101000":
        return "("
    
    if bits == "00101001":
        return ")"
    
    if bits == "00101010":
        return "*"
    
    if bits == "00101011":
        return "+"
    
    if bits == "00101100":
        return ","
    
    if bits == "00101101":
        return "-"
    
    if bits == "00101110":
        return "."
    
    if bits == "00101111":
        return "/"

    if bits == "00110000":
        return "0"
    
    if bits == "00110001":
        return "1"
    
    if bits == "00110010":
        return "2"
    
    if bits == "00110011":
        return "3"
    
    if bits == "00110100":
        return "4"
    
    if bits == "00110101":
        return "5"
    
    if bits == "00110110":
        return "6"
    
    if bits == "00110111":
        return "7"
    
    if bits == "00111000":
        return "8"
    
    if bits == "00111001":
        return "9"

    if bits == "00111010":
        return ":"
    
    if bits == "00111011":
        return ";"
    
    if bits == "00111100":
        return "<"
    
    if bits == "00111101":
        return "="
    
    if bits == "00111110":
        return ">"
    
    if bits == "00111111":
        return "?"

    if bits == "01000000":
        return "@"

    if bits == "01000001":
        return "A"
    
    if bits == "01000010":
        return "B"
    
    if bits == "01000011":
        return "C"
    
    if bits == "01000100":
        return "D"
    
    if bits == "01000101":
        return "E"
    
    if bits == "01000110":
        return "F"
    
    if bits == "01000111":
        return "G"
    
    if bits == "01001000":
        return "H"
    
    if bits == "01001001":
        return "I"
    
    if bits == "01001010":
        return "J"
    
    if bits == "01001011":
        return "K"
    
    if bits == "01001100":
        return "L"
    
    if bits == "01001101":
        return "M"
    
    if bits == "01001110":
        return "N"
    
    if bits == "01001111":
        return "O"
    
    if bits == "01010000":
        return "P"
    
    if bits == "01010001":
        return "Q"
    
    if bits == "01010010":
        return "R"
    
    if bits == "01010011":
        return "S"
    
    if bits == "01010100":
        return "T"
    
    if bits == "01010101":
        return "U"
    
    if bits == "01010110":
        return "V"
    
    if bits == "01010111":
        return "W"
    
    if bits == "01011000":
        return "X"
    
    if bits == "01011001":
        return "Y"
    
    if bits == "01011010":
        return "Z"

    if bits == "01011011":
        return "["
    
    if bits == "01011100":
        return "\\"
    
    if bits == "01011101":
        return "]"
    
    if bits == "01011110":
        return "^"
    
    if bits == "01011111":
        return "_"
    
    if bits == "01100000":
        return "`"

    if bits == "01100001":
        return "a"
    
    if bits == "01100010":
        return "b"
    
    if bits == "01100011":
        return "c"
    
    if bits == "01100100":
        return "d"
    
    if bits == "01100101":
        return "e"
    
    if bits == "01100110":
        return "f"
    
    if bits == "01100111":
        return "g"
    
    if bits == "01101000":
        return "h"
    
    if bits == "01101001":
        return "i"
    
    if bits == "01101010":
        return "j"
    
    if bits == "01101011":
        return "k"
    
    if bits == "01101100":
        return "l"
    
    if bits == "01101101":
        return "m"
    
    if bits == "01101110":
        return "n"
    
    if bits == "01101111":
        return "o"
    
    if bits == "01110000":
        return "p"
    
    if bits == "01110001":
        return "q"
    
    if bits == "01110010":
        return "r"
    
    if bits == "01110011":
        return "s"
    
    if bits == "01110100":
        return "t"
    
    if bits == "01110101":
        return "u"
    
    if bits == "01110110":
        return "v"
    
    if bits == "01110111":
        return "w"
    
    if bits == "01111000":
        return "x"
    
    if bits == "01111001":
        return "y"
    
    if bits == "01111010":
        return "z"

    if bits == "01111011":
        return "{"
    
    if bits == "01111100":
        return "|"
    
    if bits == "01111101":
        return "}"
    
    if bits == "01111110":
        return "~"

    if bits == "11001000":
        return "È"
    
    if bits == "11001001":
        return "É"
    
    if bits == "11001100":
        return "Ì"
    
    if bits == "11010010":
        return "Ò"
    
    if bits == "11011001":
        return "Ù"
    
    if bits == "11100000":
        return "à"
    
    if bits == "11101000":
        return "è"
    
    if bits == "11101001":
        return "é"
    
    if bits == "11101100":
        return "ì"
    
    if bits == "11110010":
        return "ò"
    
    if bits == "11111001":
        return "ù"
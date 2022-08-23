alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def encrypt(text,shift):
  result = ''
  for char in text:
    index = alphabet.index(char)
    shifted = index + shift
    if shifted > len(alphabet)-1:
      difference = shifted - len(alphabet)
      result+= alphabet[difference]
    else:
      result += alphabet[shifted]

  print(result)

def decrypt(text,shift):
  result = ''
  for char in text:
    index = alphabet.index(char)
    shifted = index - shift
    if shifted < 0:
      difference = len(alphabet) + shifted
      result += alphabet[difference] 
    else:
      result += alphabet[shifted]

  print(result)

if(direction == 'encode'):
  encrypt(text,shift)
elif(direction == 'decode'):
  decrypt(text,shift)
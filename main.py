alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art

print(art.logo)
restart = 'yes'
while restart == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  def encrypt(text,shift):
    result = ''
    for char in text:
      if char in alphabet:
        index = alphabet.index(char)
        shifted = index + shift
        if shifted > len(alphabet)-1:
          difference = shifted - len(alphabet)
          result+= alphabet[difference]
        else:
          result += alphabet[shifted]
      else:
        result+=char
  
    print(result)
  
  def decrypt(text,shift):
    result = ''
    for char in text:
      if char in alphabet:
        index = alphabet.index(char)
        shifted = index - shift
        if shifted < 0:
          difference = len(alphabet) + shifted
          result += alphabet[difference] 
        else:
          result += alphabet[shifted]
      else:
        result += char
  
    print(result)
  
  if(direction == 'encode'):
    encrypt(text,shift)
  elif(direction == 'decode'):
    decrypt(text,shift)
  else:
    print("INVALID REQUEST")

  restart = input("Do you want to restart? 'yes' or 'no' >> ")
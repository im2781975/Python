import string
letter = list(string.ascii_lowercase)
def encryption(text, shiftKey):
    cypherText = ""
    for i in text:
        if i in letter:
            position = letter.index(i)
            NewPos = (position + shiftKey) % 26
            cypherText += letter[NewPos]
        else:
            cypherText += i
    print(f"After Encryption Text is: {cypherText} ")
def decryption(text, shiftKey):
    PlainText = ""
    for i in text:
        if i in letter:
            position = letter.index(i)
            NewPos = (position - shiftKey) % 26
            PlainText += letter[NewPos]
        else:
            PlainText += i
    print(f"After Decryption Text is: {PlainText} ")
Flag = False
while not Flag:
    ToDo = input("'Encrypt' for encryption, 'Decrypt' for decryption: ")
    text = input("Enter message: ").lower()
    shift = int(input("Type Shift Key: "))
    if ToDo == 'Encrypt':
        encryption(text, shift)
    elif ToDo == 'Decrypt':
        decryption(text, shift)
    Again = input("Enter 'Yes' for continue 'No' for exit")
    if Again == 'No':
        Flag = True

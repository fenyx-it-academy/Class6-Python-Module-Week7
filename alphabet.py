# import string
# def letters_file_line(n):
#    with open("words.txt", "w") as f:
#         alphabet = string.ascii_uppercase

#         for i in range(0,len(alphabet),n):
#                 x=alphabet[i:n]
#                 f.writelines(x)
      
# print(letters_file_line(12))

#none donduruyor birsey eksik

import string
def letters_file_line(n):
   with open("words1.txt", "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(3)
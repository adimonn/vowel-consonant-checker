#Program to check character is vowel or not using elif - else.
print ("This is a program developed by adimonn. Enter a alphabetic character (a-z), (A-Z) etc. to check if it is a vowel or consonant.")
c = input("Enter The Alphabet:")
if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
 print("\nIt is a Vowel.")
elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
    print ("\nIt is a Vowel.")
else:
    print("\nIt is a Consonant.")
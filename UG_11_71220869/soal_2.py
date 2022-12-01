print ("Alat Pengecek Palindrome")
print ("Masukan kata anda")
abc = str(input(">> "))
print ("")
def funPalindrome():
    if abc == abc[::-1]:
        print ("Palindrome")
        print ("Jika dibalik ",abc[::-1])
    else:
        print ("Bukan Palindrome")
        print ("Jika dibalik ",abc[::-1])

funPalindrome()
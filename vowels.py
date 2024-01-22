def Check_Vow(string,vowels):
  final=[each for each in string if each in vowels]
  print(len(final))
  print(final)
string=input("Enter string:")
vowels="AaEeIiOoUu"
Check_Vow(string,vowels);

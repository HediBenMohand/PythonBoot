def reverse(lachaine):
  text1 = lachaine
  text2 = ""
  for lettre in text1:
    text2 = lettre + text2
  
  print(text2)



reverse('bonjour')

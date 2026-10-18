words = {"Assume": "fərz etmək"}
def start_quiz():
  score=0

  for word, meaning in words.items():
    print("\nBu sözün mənası nədir?")
    print(word)

    answer=input("Cavab -").strip().lower()
  
    if answer==meaning:
      score=score+1
      print("Düz cavab!")
    else:
      print("Yanlışdır")
      print("Mənası",meaning,"deməkdir.")
    
  print("Quiz yekunlaşdı!")
  print("Nəticən isə",score,"/",len(words))


start_quiz()

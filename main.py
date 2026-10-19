import random
words = {"Assume": "fərz etmək","Encounter": "rastlaşma","Assess": "qiymətləndirmək"}
def start_quiz():
  score=0
  questions = list(words.items())
  random.shuffle(questions)
  for word, meaning in questions:
    print("\nBu sözün mənası nədir?")
    print(word)

    answer=input("Cavab - ").strip().lower()
  
    if answer==meaning.lower():
      score=score+1
      print("Düz cavab!")
    else:
      print("Yanlışdır")
      print("Mənası",meaning.upper(),"deməkdir.")
    
  print("Quiz yekunlaşdı!")
  print("Nəticən isə",score,"/",len(words))
  
start_quiz()

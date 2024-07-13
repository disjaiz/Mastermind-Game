import random

def check_mirroring(real_list, sample_list):
  temp_list = []
  
  for index in range(0,len(real_list)):
    if real_list[index] == sample_list[index]:
      temp_list.append(real_list[index])
    else:
      temp_list.append("-1")
 
  return temp_list
  
def mastermind():
  actual_num = str(random.randint(1000,9999))
  print(actual_num)
 
  actual_list =list(actual_num)
  total_digits = len(actual_list)
  game_on = True
  attempt = 1
  plural =""
  

  while game_on :
    guessed_num = input(f"Guess the {total_digits} number: ")
    if len(guessed_num)!= total_digits:
      print("Invalid number of digits! Please try again.\n")
      continue
  
    user_list= list(guessed_num)
  
    temp_list = check_mirroring(actual_list, user_list )
    is_match= False
  
    if temp_list== actual_list:
      is_match= True
    
    temp_list = list(map(lambda x: x.replace("-1", "x"),temp_list))
    if is_match:
      print(f"Horrayy! You guessed it right in {attempt} attempt{plural}.\n")
      play_again= input("Do you want to continue playing? Yes/No: ")
      if play_again == "Yes":
        mastermind()
      else:
        game_on = False
    else:
      print(f"O oh! You were not totally right.\nThis is your guess: {temp_list}\n")
      attempt+=1
      plural ="s"
      continue 

mastermind()

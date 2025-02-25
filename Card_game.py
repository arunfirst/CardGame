
import random
# class CARD_GAME():
#     def play_card(self,hum,com):
#         hum_count=0
#         com_count=0
#         print(f"computer choice : {com}" )
#         # t1=com.values()
#         # print("ggggggg",t1,type(t1))
#         for i,k in
        
#         if hum==t1:
#             return "player won the game or Computer Won the game"
#         elif hum > t1:
#             hum_count+=1
#             return  "Human won the game"
#         elif hum <t1:
#             com_count+=1
#             return  "Computer won the game"
        



# cards={"A":500,"k":450,"Q":300,"j":250,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
# # cards=["A","k","Q","j",2,3,4,5,6,7,8,9,10]
# # com_choice=random.choice(cards)
# c1=CARD_GAME()
# print(c1.play_card((input("Enter your card : ")),cards))




  
# 2nd way to solve 
import random
class CARD_GAME():
    cards=["A","k","Q","J","2","3","4","5","6","7","8","9","10"]
    print("")
    def __init__(self,is_human=True): 
        self.is_human = is_human
        
    def play_card(self):
        if self.is_human:
            print("you are player:")
            while True:
                card=input("Enter your card : ")
                if card in self.cards:
                    # print("card is:",card,type(card))
                    break
                else:
                    print("Enter the card like =>",self.cards)
            return card
            
        else:
            print("You are Computer:" )
            com_card=random.choice(self.cards)
            print("computer Choice :",com_card)
            return com_card
            
            
h1=CARD_GAME()
c1=CARD_GAME(False)
player_choice=h1.play_card()    
com_choice=c1.play_card()
# print("computer Choice :",com_card)

# here we are checking or counting match b/w player and computer 
com_count=0
player_count=0

i=1
while i<=5:

    if com_choice is None:
        print("Error : computer choice is null")
    else:
        if str(player_choice)==com_choice :
            print("match Draw !!!!")
            
        elif str(player_choice) > com_choice:
            print("Player won the match")
            player_count+=1
            
        else:
            print("Computer won the match")
            com_count+=1
    i+=1
    break
    

print()
print("Player won the match Times:",player_count)
print("Computer won the match Times:",com_count)
print()
if player_count==com_count:
    print("Series Draw !!!!")
elif player_count>com_count:
    print("Player won the series")
else:
    print("Computer won the series")
    
    
    

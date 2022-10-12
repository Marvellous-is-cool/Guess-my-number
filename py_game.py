





#-----------------------------------------
#Enter any random two numbers which must be an integer.                                 e.g.                               -----------                                  0                                            1                                 ------------
      #Hit enter to move to another line when providing input !#
#-----------------------------------------


import random

try:
    class VagueList:
        def __init__(self, cont):
            self.cont = cont

        def __getitem__(self, x):
            trophy = "\n    🏆"
            inp = int(input())
            
            if inp == None:
                print("To start the game, you have to enter any random two numbers -- The numbers should be an integer (i.e. 1, 2, 3, e.t.c)")
            elif type(inp) == str:
                print("[ERROR] Oops!!. You entered a string format instead \n '{ }' is a string format. You can only enter an integer e.g 1, 2, 3. \n \n Input must be two numbers \n\n\n e.g. \n --------------------- \n 1 \n 2 \n ---------------------- ".format(inp))
            else:
                if inp > 2:
                    inp = random.randint(0, 2)
                b = self.cont[x + random.randint(0, 2)]
                a = random.randint(0, inp)
                
                if a == 0:
                    a = "love"
                    
                if a == 1:
                    a = "you"
                    
                if a == 2:
                    a = "ever"
                
                print("{0} ---- {1}".format(b, a))
                
                
                if b == a:
                    print("=" * 10 + "You win!!\n")
                    print(trophy)
                    
                else:
                    print("\n" + "=" * 10 + "You lose!!\n\n")

#---------------------------------------------    
   
    print(
        "Prediction Table \n ------------------ \n Enter {0} and {1} \n next time buddy\n ================ \n\n".format(
            random.randint(0, 2), random.randint(0, 2)))
   
    vague_list = VagueList(["Durr", "daraa", "love", "you", "ever"])
    vague_list[2]
    vague_list[2]
    
    print("\n\n\n[i] Win the both boards to get two trophies !!\nYou can always try again if you lose ☺️")
    
    print("\n\n\n[HOW TO PLAY]\n There are two boards shared by you and the computer. Yours is on the right side while the computer's is on the left side. The computer will say a word in each board, and you also have to say the same word in each board. \n\nEnter two random numbers (e.g 1 and 2), each number for each board, which will randomly be converted to any of these three words ---- love, you and ever.\nIf any of the words in each board matches the one with the computer, you win and so gets a trophy. Win the both boards to earn two TROPHIES!\n\n You can also make use of the prediction table 🤗")
    
   
 #---------------------------------------------    

except ValueError:
    print("[ERROR]\n Oops!!. You entered a string format instead \n You can only enter integers e.g 1, 2, 3.\n\n.         (You also get this error when you input nothing.) \n\nInput must be two numbers \ne.g. \n --------------------- \n 1 \n 2 \n ----------------------\n Hit enter to move to another line when providing input !")
    
    
    print("\n\n\n[HOW TO PLAY]\n There are two boards shared by you and the computer. Yours is on the right side while the computer's is on the left side. The computer will say a word in each board, and you also have to say the same word in each board. \n\nEnter two random numbers (e.g 1 and 2), each number for each board, which will randomly be converted to any of these three words ---- love, you and ever.\nIf any of the words in each board matches the one with the computer, you win and so gets a trophy. Win the both boards to earn two TROPHIES!\n\n You can also make use of the prediction table 🤗")
    
except EOFError:
    print("[X] You will need two inputs to get your two trophies. \n\n e.g. \n --------------------- \n 1 \n 2 \n ----------------------Hit enter to move to another line when providing input !")

except:
    print("To start the game, Enter any random two numbers -- The numbers should be an integer e.g. 1, 2, 3, etc.(we recommend choosing from 0 to 2 only)\n\ne.g. \n --------------------- \n 1 \n 2 \n ----------------------Hit enter to move to another line when providing input !")
    
    print("\n\n\n[HOW TO PLAY]\n There are two boards shared by you and the computer. Yours is on the right side while the computer's is on the left side. The computer will say a word in each board, and you also have to say the same word in each board. \n\nEnter two random numbers (e.g 1 and 2), each number for each board, which will randomly be converted to any of these three words ---- love, you and ever.\nIf any of the words in each board matches the one with the computer, you win and so gets a trophy. Win the both boards to earn two TROPHIES!\n\n You can also make use of the prediction table 🤗")
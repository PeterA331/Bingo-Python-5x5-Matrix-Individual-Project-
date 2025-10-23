#bingo_test1
#Generating a random matrix is accomblished
# Let player chose 5 diffrent numbers is accomblished
#...working with comparing what player choesed with bingo brickor(finished)
# comparing is successeded, and matrix_game show the matched number as "X"
# (in progress start):
# we are going to check if we have bingo in matrix_random after comparing...
#... with player_numbers list

#(end)
import random

row=5
column=5
bingo_filling=25
Rando_number=0
point="."
Kriss="x"

row_random=0
column_random=0



random_true_false = [[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]

matrix=[[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
#one row
One_row=[] # store first 25 random number between 1-25 in 1D list


matrix_random= [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

matrix_random_orginal= [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]

#In matrix_game player can see if he get bingo by showing "x"
matrix_game=[]

print("matrix_game:")
for i in range(5):
    line = []  # Create a new row
    for j in range(5):
        line.append(point)  # Fill the row with zeros
        matrix_game.append(line)  # Add the row to the matrix
        print(matrix_game[i][j], end=' ')
        
    print()

print()

"""
print("random_true_false :")
for i in range(5):
    for j in range(5):
        print(random_true_false[i][j], end=' ')
    print()  # Move to next line after each row
"""
#generating matrix_random in one_row:
while bingo_filling > 0:
    row_random = random.randint(0, 4 )
    column_random = random.randint(0, 4 )
    
    if random_true_false[row_random][column_random] ==0:
            random_true_false[row_random][column_random] = 5
            Rando_number=matrix[row_random][column_random]
            #temporary_test*******
            Rando_number=int(Rando_number)

            One_row.append(Rando_number) 
            bingo_filling =bingo_filling-1
print()        
print()
print("matrix_random")
#for b in range(5):
    #for d in range(5):
        #print(matrix_random[b][d], end=' ')
    #print()  # Move to next line after each row

#print(One_row)
x=len(One_row)
print("x=", x)

#organize matrix_random in bricka:
print("\nmatrix_random(Hidden in game):")    
index=0
for i in range (5):
  for j in range (5):
     matrix_random[i][j]=One_row[index]
     
     matrix_random[i][j]=int(matrix_random[i][j])
     
     if One_row[index] > 9:
         print(matrix_random[i][j], end='  |')
     else:
         print(matrix_random[i][j], end='   |')  
     index+=1
  print()  # Move to next line after each row

print()        
print()

"""
print("random_true_false")
for i in range(5):
    for j in range(5):
        print(random_true_false[i][j], end=' ')
    print()  # Move to next line after each row 
"""

#The player, chose, player can't chose the same number more than one time:
print("Play Bingo by insert 10 diffrent number between 1 and 25")
print("All numbers you insert will be replaced by (x)")
player_numbers=[ ] #store what player choeses 
number=0
numberr=0
counter=5 #counter:player can choese 5 diffrent number
index1=0
langdOFlist=1
iteration=0
omgang=2
xx=len(player_numbers)
print("xx:", xx)
#Check if the number between 1 and 25
while omgang>0:
        while counter>0:
            
            numberr=input("Chose five numbers between 1 and 25:")
            number=int(numberr)
            
            print("number is:", number)
            
            if(number >0 and number <26):
                
                if len(player_numbers)>1 or len(player_numbers)==1 :
                    for j in range((len(player_numbers))):
                        if number!=player_numbers[j]:
                            iteration=iteration+1
                            
                        if j==((len(player_numbers))-1):
                            print("You get j equal to last index") 
                            if iteration ==((len(player_numbers))):
                                player_numbers.append(number)
                                langdOFlist=len(player_numbers)
                                print("langdOflist:", langdOFlist)
                                print(player_numbers)
                                counter=counter-1
                                iteration=0
                                
                            else:
                                print("you insert a number more the one time")
                                iteration=0
                else:
                        if len(player_numbers)==0 :
                            player_numbers.append(number)
                            langdOFlist=len(player_numbers)
                            print("langdOflist:", langdOFlist)
                            print(player_numbers)
                            counter=counter-1
            else:
                print("The number out of range(1-25)")
        counter=5    
        #########################  

        #compare player's choeses with matrix_random, every match will be a "X" in matrix_game,
        #the comparing is going between player_numbers list and the hidden matrix_random list,
        #as mentioned if it get match, put "X" instead of point in matrix_game
        match=0
        counter1=0
        
        """
        for i in range(len(matrix_random)):
            for j in range(len(matrix_random[i])):
                if player_numbers[counter1]==matrix_random[i][j]:
                    matrix_game[i][j]= "X"#77 #Kriss
                    match+=1
                else:
                    matrix_game[i][j]="." #88 #point  
            counter1+=1    
        """
        """
        print("matrix_game after comparing:")
        for i in range(len(matrix_random)):
            for j in range(len(matrix_random[i])):
                print(matrix_game[i][j], end=' ')
            print()

        print()
        """
        #################*******************##############
        #replace all matched numbers from player_numbers list with zero in matrix_random list
        for e in range(len(player_numbers)):
            for i in range(len(matrix_random)):
                for j in range(len(matrix_random[i])):
                    if matrix_random[i][j]==player_numbers[e]:
                        matrix_random[i][j] = 0
                        match += 1
                    
                #counter1+=1  
        #################*******************##############  
        """
        # print matrix_random with match zero
        print("matrix_random with match zero")
        for b in range(len(matrix_random)):
            for d in range(len(matrix_random[b])):
                if matrix_random[b][d]<10:
                   print(matrix_random[b][d], end='  ')
                else:
                    print(matrix_random[b][d], end=' ')  
            print()  # Move to next line after each row
        """
        #################*******************##############
        # matrix_game after comparing
        # where ever there is a zero in matrix_random list, will be replaced by "x"...
        #... in matrix_game, if not zero, replace with point "."
        print("matrix_game after comparing:")
        for i in range(len(matrix_random)):
            for j in range(len(matrix_random[i])):
                
                if matrix_random[i][j]==0:
                    matrix_game[counter1]=Kriss
                else:
                    matrix_game[counter1]=point
                counter1+=1       
        print()

        print()
        counter1=0
        #################*******************##############
        #print matrix_game after comparation:
        for i in range(5):
            for j in range(5):
                print(matrix_game[counter1], end=' ')
                counter1+=1
            print()    
        #################*******************##############
        # check lodratt in matrix_random list:
        indicate=0

        for j in range((len(matrix_random))): # coulumn
          for i in range(len(matrix_random[j])-1): # Row
            
            if matrix_random[0][j]==matrix_random[i+1][j]:
                indicate=indicate+1
            
            if i==((len(matrix_random))-2):       
                    if indicate!=((len(matrix_random))-1):
                        
                        indicate=0 
                        
                    else:
                        
                        print("All columns are matched in: {0} , BINGO!!".format(j)) 
                        indicate=0    

        indicate=0

        #################**********###############
        # check vagratt in matrix_random list:
        for i in range((len(matrix_random))):
          for j in range((len(matrix_random[i]))-1):
            
            if matrix_random[i][0]==matrix_random[i][j+1]:
                indicate=indicate+1
            
            if j==((len(matrix_random[i]))-2):       
                    
                    if indicate!=((len(matrix_random[i]))-1):
                        
                        indicate=0
                        
                    else:
                        
                            print("All item in this row are matched in matrix:({0}), BINGO!!".format(i))
                            indicate=0   

        indicate=0
        indicate1=0
        ##################*******************##################
        # chech diagonalt in matrix_random
        # from the high left to buttom right
        for i in range((len(matrix_random)-1)):
        
            #if i!=2:
            if matrix_random[len(matrix_random)-1][len(matrix_random)-1]==matrix_random[i][i]:
                indicate=indicate+1
            
            if i==((len(matrix_random[i]))-2):       
                    
                    if indicate!=((len(matrix_random))-1):
                        
                        indicate=0
                        
                        
                    else:
                        
                            print("All item in this diagonal are matched in matrix, BINGO!!!")
                            indicate=0   
                    
        ###############*************################
        # chech diagonalt in matrix_random
        # from the high right to buttom left*
        for i in range((len(matrix_random)-1)):
        

                if matrix_random[len(matrix_random)-1][0]==matrix_random[i][5-i-1]:
                #diagonal2 = diagonal2 + m[i][4-i-1];
                    indicate1=indicate1+1
                #indicate=0
                
                if i==((len(matrix_random[i]))-2):       
                    
                    if indicate1!=((len(matrix_random))-1):
                        #print("No match,from the high right to buttom left")
                        indicate1=0
                        #i=(len(matrix))-1
                        #break
                    else:
                        #if indicate==1:  #i==((len(matrix))-1)
                        print("**All item in this diagonal are matched in matrix, BINGO!!!**")
                        indicate1=0     
        ##############**************################
        indicate=0 
        indicate1=0  
        #print("indicate1:",indicate1)
        print()

        omgang=omgang-1
answer="."      
item=0  
print("Do you want to see the matrix ?")
answer=input()
answer=answer.lower()
if answer=="yes":
     for i in range(len(matrix_random)):
          for j in range(len(matrix_random[i])):
               if One_row[item] > 9:
                  print(One_row[item], end='  |')
               else:
                  print(One_row[item], end='   |')  
                  
               item+=1
          print() 
print()                      
print("END of program")
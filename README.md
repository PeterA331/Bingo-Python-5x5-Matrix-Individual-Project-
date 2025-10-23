# Bingo-Python-5x5-Matrix-Individual-Project-

Developed a terminal-based bingo game in Python that generates a random 5x5 card, receives 
player's choices, and marks hits in real-time. Implemented checks for rows, columns, and 
diagonals to determine Bingo.
Project Details
- Technologies Python standard library, lists and matrices (2D lists), control flows, input
validation
- Random Generation Creates a 5x5 card with unique numbers 1–25 via a helper matrix
that prevents duplicates
- User Interaction The player inputs unique numbers within the valid range; incorrect or
duplicate selections are handled robustly
- Matching and Rendering Hits are marked as 'x' in a display matrix; non-hits are shown as
a dot ('.') for a clear overview
- Win Logic Algorithms to detect a full row, column, and both diagonals (BINGO) after
each round


- Data Structure Design Separate matrices for the original card, status, and display to
simplify logic and debugging
- Testing and Verification Manual test cases for input, duplicate protection, boundary
values, and win conditions, with console output for traceability
- Future Development (Suggestions) Scorekeeping, multiple game rounds, unit tests, and
modular separation into functions and classes for better reusability

Here is an example runing for the program:

matrix_game:
. . . . . 
. . . . .
. . . . .
. . . . .
. . . . .



matrix_random
x= 25

matrix_random(Hidden in game):
23  |24  |14  |5   |25  |
18  |4   |3   |17  |1   |
7   |20  |12  |2   |15  |
16  |8   |21  |6   |10  |
9   |19  |11  |22  |13  |


Play Bingo by insert 10 diffrent number between 1 and 25
All numbers you insert will be replaced by (x)
xx: 0
Chose five numbers between 1 and 25:55
number is: 55
The number out of range(1-25)
Chose five numbers between 1 and 25:4
number is: 4
langdOflist: 1
[4]
Chose five numbers between 1 and 25:8
number is: 8
You get j equal to last index
langdOflist: 2
[4, 8]
Chose five numbers between 1 and 25:8
number is: 8
You get j equal to last index
you insert a number more the one time
Chose five numbers between 1 and 25:6
number is: 6
You get j equal to last index
langdOflist: 3
[4, 8, 6]
Chose five numbers between 1 and 25:9
number is: 9
You get j equal to last index
langdOflist: 4
[4, 8, 6, 9]
Chose five numbers between 1 and 25:33
number is: 33
The number out of range(1-25)
Chose five numbers between 1 and 25:1
number is: 1
You get j equal to last index
langdOflist: 5
[4, 8, 6, 9, 1]
matrix_game after comparing:


. . . . .
. x . . x
. . . . .
. x . x .
x . . . .

Chose five numbers between 1 and 25:1
number is: 1
You get j equal to last index
you insert a number more the one time
Chose five numbers between 1 and 25:88
number is: 88
The number out of range(1-25)
Chose five numbers between 1 and 25:7
number is: 7
You get j equal to last index
langdOflist: 6
[4, 8, 6, 9, 1, 7]
Chose five numbers between 1 and 25:15
number is: 15
You get j equal to last index
langdOflist: 7
[4, 8, 6, 9, 1, 7, 15]
Chose five numbers between 1 and 25:15
number is: 15
You get j equal to last index
you insert a number more the one time
Chose five numbers between 1 and 25:14
number is: 14
You get j equal to last index
langdOflist: 8
[4, 8, 6, 9, 1, 7, 15, 14]
Chose five numbers between 1 and 25:20
number is: 20
You get j equal to last index
langdOflist: 9
[4, 8, 6, 9, 1, 7, 15, 14, 20]
Chose five numbers between 1 and 25:25
number is: 25
You get j equal to last index
langdOflist: 10
[4, 8, 6, 9, 1, 7, 15, 14, 20, 25]
matrix_game after comparing:


. . x . x
. x . . x
x x . . x
. x . x .
x . . . .

Do you want to see the matrix ?
yes
23  |24  |14  |5   |25  |
18  |4   |3   |17  |1   |
7   |20  |12  |2   |15  |
16  |8   |21  |6   |10  |
9   |19  |11  |22  |13  |

END of program

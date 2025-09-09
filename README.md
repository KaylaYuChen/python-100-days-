# python-100-projects-
Sharing my journey of learning Python from scratch —  through Dr. Angela Yu’s Code Course.  
This repository contains the projects I build each day — from exercises to full applications.

---

## 🚀 Goals
- Complete all 100 projects  
- Document learning progress daily  

---

## 📅 Projects

### ✅ Day 5: Password Generator 🔑
A program that generates secure random passwords using letters, numbers, and symbols.  
It includes two modes:  
- **Easy Level** → Characters are ordered (letters, then symbols, then numbers)  
- **Hard Level** → Characters are randomized using `random.shuffle()`  

- Practiced **for loops** and list building  
- Reinforced using **random.choice()** for random selection  
- Used string concatenation (`+=`) to build the password 

**Code:** [`Day05/password_generator.py`](Day05/password_generator.py)  
**Sample Output:**
```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
3

Easy password (ordered): ghKD$+84
Unshuffled list: ['g', 'h', 'K', 'D', '$', '+', '8', '4']
Shuffled list: ['$', 'h', 'g', 'K', '+', 'D', '4', '8']
Your hard password is: $hgK+D48
```

### ✅ Day 4: Rock, Paper, Scissors ✊📄✂️
A simple Python game where the player chooses Rock, Paper, or Scissors and competes against a random computer choice.  
This project reinforced **conditionals**, **lists**, and **random number generation**.

- Practiced using **lists** for ASCII art storage  
- Learned **random.randint()** for computer choice  
- Built game logic with **nested conditionals**  

**Code:** [`Day04/rock_paper_scissors.py`](Day04/rock_paper_scissors.py)  

**Sample Output:**
Case 1 – You choose Rock (0), Bunny chooses Paper (1):
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:
```
You chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Your bunny chose:

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

You lose!
```
Case 2 – You choose Scissors (2), Bunny chooses Paper (1):
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:
```
You chose: 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Your bunny chose:

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

You win!

```
Case 3 – You and Bunny both choose Rock (draw):
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:
```
You chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Your bunny chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

It's a draw!
```


### ✅ Day 3: Treasure Island 🏝️
A text-based adventure game where the player chooses their own path to (hopefully) find the treasure.  
This project used **conditionals** (`if`, `elif`, `else`) and **input normalization** (`.strip().lower()`) to handle user choices.  

- Practiced **nested conditionals**  
- Learned to **normalize user input** with `.strip().lower()`  
- Added **ASCII art** for a more fun intro 🎨  

**Code:** [`Day03/treasure_island.py`](Day03/treasure_island.py)  

**Sample Output:**
```
*********************************************************************************
                                       ` )
                              (         (
                               )      (
                             )          )
                            (          ( ,
                           _ _)_      .-).
                .--._ _.--'.',-.\_.--' (_)`.
              .'_.   `  _.'  `-'    __._.--;
             /.'  `.  -'     ___.--' ,--.  :       o       ,-. _
            : |  o()|       ,'  .-'`.(   |  '      (   o  ,' .-' `,
           :  `.  .'    ._'-,  \   | \  ||/        `.{  / .'    :
          .;    `'    ,',\|\|   \  |  `.;'     .__(()`./.'  _.-'
          ;           |   ` `    \.'|\\ :      ``.-. _ '_.-'
         .'           ` /|,         `|\\ \        -'' \  \
         :             \`/|,-.       `|\\ :         ,-'| `-.
         :        _     \`/  |   _   .^.'\ \          -'> \_
         `;      --`-.   \`._| ,' \  |  \ : \           )`.\`-
          :.      .---\   \   ,'   | '   \ : .          `  `.\_,/
           :.        __\   `. :    | `-.-',  :               `-'
           `:.     -'   `.   `.`---'__.--'  /
            `:         __.\    `---'      _'
             `:.     -'    `.       __.--'
              `:.          __`--.--'\
---------------- `:.      --'     __   `.--------------------------------------

*******************************************************************************
Welcome to Treasure Island.
Your mission is to find the treasure.

You're at a cross road. 
Where do you want to go? Type "Left" or "Right": left

You've come to a lake. 
There is an island in the middle of the lake. 
Type "wait" to wait for a boat. 
Type "swim" to swim over: wait

You've arrived at the island unharmed. 
There is a house with 3 doors. 
One red, one yellow, and one blue. 

Which color do you choose? red

🔥 You just opened the door to the dungeon of dragons.  
The dragons are hungry... 🐉 Game Over.

```

### ✅ Day 2: Tip Calculator 💵
Tip Calculator calculates how much each person should pay when splitting a restaurant bill, including tip.  
The program asks for the total bill, tip percentage, and number of people, then outputs the split amount.  

- Practiced **numbers and math operations**  
- Learned about **type conversion** (`int()`, `float()`)  
- Used **round()** for decimal precision  
- Introduced to **f-strings** for cleaner output  

**Code:** [`Day02/tip_calculator.py`](Day02/tip_calculator.py)  

**Sample Output:**
```
Welcome to the Tip Calculator!
What was the total bill? $124.56
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
Each person should pay: $19.90
```

### ✅ Day 1: Band Name Generator 🎵
The program asks the user for their favorite city and childhood pet, then generates a personalized band name. 
- Practiced string concatenation with `+`
- Learned about input() for collecting user input
- Added emojis for a more fun user experience 🎸🐶🌆✨  

**Code:** [Day01/band_name_generator.py](https://github.com/KaylaYuChen/python-100-days-/blob/main/Day01/band_name_generator.py)

**Sample Output:**
```
🎸 Welcome to the Band Name Generator! 🎤
I will help you create a fun name for your band.

🌆 What is the name of your favorite city?
Paris
🐶 What is the name of your childhood pet?
Max

✨ Your band name could be: Paris Max ✨
```


---

## 🌟 Connect
- [LinkedIn](https://www.linkedin.com/in/kaylayuchen)  
- [GitHub](https://github.com/KaylaYuChen)

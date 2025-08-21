print('''
*******************************************************************************
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
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You\'re at a cross road. Where do you want to go? '
                  'Type "Left" or "Right"').strip().lower()
if direction == "left":
    action = input('You\'ve come to a lake. '
                   'There is an island in the middle of the lake. '
                   'Type "wait" to wait for a boat. '
                   'Type "swim" to swim over.')
    if action == "wait":
        choice = input("You've arrived at the island unharmed. "
                       "There is a house with 3 doors. "
                       "One red, one yellow, and one blue. "
                       "Which color do you choose?").strip().lower()
        if choice == "yellow":
            print("You found the treasure of gold! Dig in and You WIN!")
        elif choice == "red":
            print("You just opened the door to the dungeon of dragons. The dragons are hungry. Game Over.")
        elif choice == "blue":
            print("You stepped in and found yourself falling from the sky. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You forgot you couldn't swim. Game Over.")

else:
    print("You got attacked by a snake. Game Over.")



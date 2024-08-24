import time, pyfiglet, sys

class TypeMasterGame:
    def __init__(self):
        self.levels = {
            'Easy': ['this cat ate the harry juice while the down bird fat tree behind same girl best dog order you and star dash word begun within and off between lemon thing eight banana upper sugar name monica ring up a funny water romance number',
                     'cocky pink has owl sherlock blue turtle neck yellow zoo and who in without far sleep ice fish and shark four run way in new the soon bed up left right she like what general face cycle check oven frog moon london school weird fun vet'
                    ],
            'Medium': ['floppy giant elephant queen granted fascinating parking tough rabbit painful not vacuum congrats hyper twelve everyone must pregnant the violet joke determine the further things looking tomorrow passport ignoring physical temper',
                       'cooking storm launch teamwork vital adaptable passion around power success victory sebastian because achieve dynamic fearless whose cyclone schedule russia movie particular challenge exception tickets sweater exercise license'
                    ],
            'Hard': ['christmas beautiful empathy remarkable logic extraordinary shortage cocktail responsibility do development consistent determination a perseverance inbox intelligent present garbage wedding handcuff troublesome wednesday exaggerate',
                     'although rhinoceros and appearance intelligent browse wonderful independence barn reasonable does homesick hippopotamus approach censorious weakness strength opportunity threat membership in harmless restaurant pregnant calendar',
                    ]
        }
        self.mistakes = 0 
        self.round = 0

    def start_the_game(self, round):
        while True:
            words_list = self.levels[round]

            for i in range(0, len(words_list)):
               self.round +=1
               # reset mistakes
               self.mistakes = 0
               print('\n')
               print('──────── Round', self.round, ' ๋࣭ ⭑────────:')
               print('\n')
               print(words_list[i])
               print('\n')

               # Start the timer
               start_time = time.time()  
               user_input = input()
               # Stop the timer
               end_time = time.time() 

               # Calculate the elapsed time
               elapsed_time = end_time - start_time
               minutes = int(elapsed_time // 60)
               seconds = int(elapsed_time % 60)
               # Calculate words per minutes
               wpm = (len(words_list[i].split()) / elapsed_time) *60 
               print('\n')

               # Test user input: are they the same length? 
               if len(user_input) == len(words_list[i]): 
                   # Iterate through the characters 
                   for j in range(0, len(user_input)):
                      if user_input[j] != words_list[i][j]:
                        self.mistakes += 1

               else: # Not the same length 
                    # Find the minimum length
                    min_length = min(len(user_input), len(words_list[i]))   
                    # Iterate through the characters
                    for j in range(0, min_length): 
                        if user_input[j] != words_list[i][j]:   
                            self.mistakes += 1
                    # Add the difference in length to the mistakes
                    self.mistakes += abs(len(user_input) - len(words_list[i]))
        
               # Show feedback
               print('Mistakes: ', self.mistakes)
               print(f'Elapsed time: {minutes} minutes {seconds} seconds')
               print(f'Words Per Minutes: {wpm:.2f} words')

               if wpm<20:
                   print('You\'re Slow! 🐌')
               elif wpm<40:
                   print('You\'re Average! 🧚‍♀️')
               elif wpm<60:
                   print('You\'re Decent! ⭐')
               else: # >60
                   print('You\'re Fast! 🚀')
               print('\n')

               # Reached the end of the round
               if self.round == 2 or self.round == 4 or self.round == 6:
                    print('You\'ve Reached the End of the Round >ᴗ<!')
                    choice = input('Do You Want to Keep Playing? Write Anything to Keep Playing or no to Quit: ')           
                    if choice.lower() == 'no':
                      print('Thanks for Playing 𓍢ִ໋🌷͙֒ ')
                      sys.exit(0)
                    else:
                        self.mistakes = 0
                        self.level_choice()
                
               # Choices after receiving the feedback
               while True:
                     choice = input('Choose:\n1. Next Round๋࣭ ⭑\n2. Change Category๋࣭ ⭑\n3. Quit๋࣭ ⭑\nYour Choice: ')
                     if choice== '1':
                            break
                     elif choice== '2':
                            self.mistakes = 0
                            self.level_choice()
                            # was break
                     elif choice== '3':
                          print('Thanks for playing! 𓍢ִ໋🌷͙֒ ')
                          sys.exit(0)
                     else:
                          print('Invalid Choice! Please Enter a Number between 1 and 3')
    
    def level_choice(self):
        print('Choose a Category:\n1. Easy ๋࣭ ⭑\n2. Medium๋࣭ ⭑\n3. Hard๋࣭ ⭑')
        while True:
            choice = input('Your Choice: ')
            if choice == '1':
                self.start_the_game('Easy')
                break
            elif choice == '2':
                self.start_the_game('Medium')
                break
            elif choice == '3':
                self.start_the_game('Hard')
                break
            else:
                print('Invalid Choice! Please Enter a Number between 1 and 3')    

def main():
    title = pyfiglet.figlet_format('Type Master', font = 'starwars')
    print(title, '──────── Developed by: Zainab ₊⊹', '\n')
    print('Type The Words as Fast as You Can! ⏩ \n')
    time.sleep(2)

    game = TypeMasterGame()
    print('Before playing the game I have a few things to explain: \n1) At first, choose a category: Easy, Medium, or Hard and each category has 2 rounds.')
    print('2) After the end of each round you\'ll receive a feedback of time, number of mistakes, words per minute(wpm), and your typing speed.')
    time.sleep(2)
    print('3) Then you can choose to continue to the next round, change category, or quit to terminate the game.')
    print('4) The words are all in lower-case. So, make sure to type the words exactly as they appear.\n')

    choice = input('Are You Ready for Some Fun? Write Anything to Play or no to Quit: ')
    if choice.lower() == 'no':
        print('Goodbye! 𖹭')
        sys.exit(0)
    else: 
        print('Let the Game Begin >ᴗ<!!')
        time.sleep(1)
        game.level_choice()

if __name__ == "__main__":
    main()
    sys.exit(0)
    
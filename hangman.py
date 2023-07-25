import random
from hangman_words import words
from hangman_art import logo, stages

print(logo)
#word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(words)

# Testing code
#print(f'The chosen word is {chosen_word}.')

display = []
word_length = len(chosen_word)
lives = 6
for letter in range(word_length):
  display.append("-")
print(" ".join(display))

while "-" in display:
  guess = input("Guess a letter:").lower()
  
  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    '''print(f'Curent position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}')'''
    if guess ==  letter:
      display[position] = letter
  
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    print(stages[lives])
    if lives == 0:
      print(f'The chosen word is {chosen_word}.')
      print("You lose")
      break
  print(f"{' '.join(display)}")
else:
  print("You win")
  
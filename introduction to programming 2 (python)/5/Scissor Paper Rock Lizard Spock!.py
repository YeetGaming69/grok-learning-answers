RULES = {
  ('scissors', 'paper') : 'Scissors cut Paper',
  ('paper', 'rock') : 'Paper covers Rock',
  ('rock', 'lizard') : 'Rock crushes Lizard',
  ('lizard', 'spock') : 'Lizard poisons Spock',
  ('spock', 'scissors') : 'Spock melts Scissors',
  ('scissors', 'lizard') : 'Scissors decapitate Lizard',
  ('lizard', 'paper') : 'Lizard eats Paper',
  ('paper', 'spock') : 'Paper disproves Spock',
  ('spock', 'rock') : 'Spock vaporizes Rock',
  ('rock', 'scissors') : 'Rock breaks Scissors'
}
h1 = input('Hand 1: ')
h2 = input('Hand 2: ')
winner = RULES.get((h1, h2), RULES.get((h2, h1), 'Tie'))
print(winner) 

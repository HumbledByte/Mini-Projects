best_legend  = 'Pathfinder'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != best_legend and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Who do you think the best legend is?: ')
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print('Out of guesses')
else:
    print('Correct!')
words = {'miserable' : 'depressed',
         'stumped off' : 'walked noisily in anger'}
word_selected = input('Which word do you want to know?').lower()
if word_selected in words:
    print(f'The meaning of {word_selected} is {words[word_selected]}.')
else:
    print('Error. Try again.')


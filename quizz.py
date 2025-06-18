# vores episke sovse spørgskema quizz

points = 0

print('Velkommen til sovse quizzen! Hvilken sovs er du?')
print('Tryk på en tast for at starte!!!1!')

print('Spørgsmål 1: Kan du lide at stå tidligt op?')
print('1: JEG ELSKER AT STÅ TIDLIGT OP')
print('2: JEG HADER AT STÅ TIDLIGT OP')
print('3: jeg gør det gerne, men ikke af egen vilje')
print('4: hvad er søvn?')

points = int(input('indtast dit svar'))

print('Spørgsmål 2: hvad er din livret?')
print('1: lasagne')
print('2: pizza')
print('3: sushi')
print('4: taco')

points = points + int(input('indtast dit svar'))

if points >= 7:
    print('Du er en hollandaise!')

elif points > 1 and points < 3:
    print('Du er teriyaki!')

elif points > 2 and points < 5:
    print('Du er bernaise!')

elif points < 7 and points > 4:
    print('Du er brun!')

else:
    print('Du er ikke sovs?')

print('tryk på en tast for at lukke programmet')

if input():
    print('goodbye')

else:
    print('...')
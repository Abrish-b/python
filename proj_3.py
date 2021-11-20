#!/usr/bin/python3
# import this
import sys
str1 = "Holberton"
str2 = "School"
# method1
str1 = str1 + " " + str2
print("Welcome to {}!".format(str1))
# method2
str1 += (" " + str2)


# proj 2

word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:8]
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))

# proj 3
# import this

# proj 4
sys.stdout.write("""
 ___________________________________________
|  _______________________________________  |
| / .-----------------------------------. \ |
| | | /\ :                        90 min| | |
| | |/--\:....................... NR [ ]| | |
| | `-----------------------------------' | |
| |      //-\\   |         |   //-\\      | |
| |     ||( )||  |_________|  ||( )||     | |
| |      \\-//   :....:....:   \\-//      | |
| |       _ _ ._  _ _ .__|_ _.._  _       | |
| |      (_(_)| |(_(/_|  |_(_||_)(/_      | |
| |               low noise   |           | |
| `______ ____________________ ____ ______' |
|        /    []             []    \        |
|       /  ()                   ()  \       |
!______/_____________________________\______!                 
 """)

sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
sys.exit(1)

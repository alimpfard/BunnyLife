# BunnyLife
An answer to a question.

the only CS file is the C# answer (WIP) (when i feel like it)\n
Rules: (also in Rules.txt)
**Write a Program that creates a linked list of bunny objects**

_Each bunny must have:
	Sex: Male/Feamle at creation time 50/50 chance
	Color: White, Brown, Black, Spotted
	Age: 0-10 Yrs old
	Name: Randomly chosen at creation time from a list of bunny names
	radioactive_mutant_vampire_bunny: true/false (at creation time 2% chance)__

*At program initialization 5 bunnies must be created and given random colors
each turn afterwars, the bunnies age 1 year.*

*So long as there is at least one adult male bunny (age >= 2yrs) for any female bunny in the list, a new bunny is created each turn.*

__new bunnies born should be the same color as their mother.
  if age>10 bunny dies
  if a radioactive bunny is born, it turns exactly one non-radioactive bunny to a radioactive one
  radioactive bunnies are excluded from breeding
  radioactive bunnies don't die until they reach age 50
  The program should print a list of all the bunnies in the colony each turn along with all the details, sorted by age
the program should print out the events.
if the population exceeds 1000, a shortage happens, and exactly half the bunnies randomly die.__

* Real time, each turn = 2s, 1 sec pause between any announcement
* ** Allow the user to hit the K button to kill half of all the rabbits, randomly
**** Modify the program to put all the rabbits in a 80*80 grid, they move one space randomly each turn.
	m,M,f,F,X
	X turns only the adjacent bunny
	babies are born in the empty square next to the mother, not empty? not born

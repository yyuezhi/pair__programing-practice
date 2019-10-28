# Colab Exercise

Time to collaborate! This is a pair programming exercise.

## Before coding
One of you should do the following:
1. Clone this repository.
2. Make a new repository under your own name.
3. Add your friend as a collaborator of the repository.
4. Change the git remote origin to your repository.
5. Push to that repository.

After the above steps, the other person should clone that repository, **not this one**.

## Programming tasks
Your goal is to complete the `ascii.py` program. *You should be using python3*

There are 2 functions that you have to complete. Each of you should do one.
1. computeSimple
  - take in a string
  - convert that string into ascii decimal code by characters
  - return the sum of the ascii decimal codes
2. computeByIndex
  - take in a string
  - convert that string into ascii decimal code by characters
  - multiply each ascii decimal code by the index of the character of the input string (*index starts from 0*)
  - return the sum of the multiplication results

## Important notes
Each of you should create a `git branch`, and push accordingly. Then, make pull requests, and conduct code reviews before merging to `master`.

## Test cases
First line is the string input. Second and third lines are the output.

```
string
sumSimple: 663
sumByIndex: 1614
```

```
0123456789
sumSimple: 525
sumByIndex: 2445
```

```
Sean is ridiculous sometimes...
sumSimple: 2918
sumByIndex: 43055
```

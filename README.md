# M.I.A_Phase1_Tasks

## Gru vs Vector simulation

I first created the outline of the game using simple print statements

 I then created a parent class for both Villains since they share the same attributes

This sets some default attributes for each object created from it aka the Villains.
```python

class Villain():

```

When it's a specific Villains turn I run his function which
redirects you to one of two functions depending on your choice of input

```python
 def Gru(): #gru's turn
```

The same goes for the other villain.

One of these choices is the shields function which displays the shields available
and allows you to apply them

```python
def GruShields():
```

The other one is the Weapons function which displays the Weapons available 
and then proceeds to invoke the dmg function which applies damage to the opponent with respect to his shield

```python
def VectorWeapons():
def dmg(obj, dmg):

```
The Validate Input function strips the string of any whitespace and makes sure that the string you entered isn't empty 
it then converts it into an integer, if it can't be converted it will throw an error which will redirect you to the beginning of the loop inside
the function

```python
def validate_input(prompt):
```

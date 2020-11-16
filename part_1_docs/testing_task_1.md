### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else # colon missing
      return False
   
# should say 'def' rather than dif. # comma missing between card1 & card2
  dif highest_card(self, card1 card2): 
  if card1.value > card2.value: # indentation incorrect on line 28, 29, 30 & 31 (should all be taken in to the right)
    return card # should be card1
  else:
    return card2
  


def cards_total(self, cards):
  total # = 0 missing
  for card in cards:
    total += card.value
    return "You have a total of" + total # indentation incorrect 
    # missing space at end of string ""You have a total of " 
    # total should be a string not and int - change to str(total) 
  
```

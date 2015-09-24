# Pokemon-Lottery-Calculator
Calculate the odds of winning each tier of lottery prize in the Pokémon games. Uses Python 3.

First, read [this article](http://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Lottery_Corner) to understand how the lottery works in the Pokemon games.

Matching is done from rightmost digit to leftmost digit, so if the current lottery number of the day is 55555, a Pokémon with the
id 55550 is considered to have 0 digits matched, while a Pokémon with the id 55505 is considered to have matched one digit
(the rightmost one).

usage: lotto.py [-h] [--generate] N [N ...]

For example: ```python lotto.py --generate 50``` will generate 50 random, unique trainer ids and then calculate the odds for
that set of ids. Here is one possible result set for 50 random ids:

```
Results:
0 digits:       0 |     0.0%
1 digit:    39982 | 61.0077%
2 digits:   22276 | 33.9905%
3 digits:    2950 |  4.5013%
4 digits:     278 |  0.4242%
5 digits:      50 |  0.0763%

At least 1: 65536 |   100.0%
At least 2: 25554 | 38.9923%
At least 3:  3278 |  5.0018%
At least 4:   328 |  0.5005%
```

If the ```--generate``` option is not specified, then the script calculates the odds using user supplied trainer ids.

For example: ```python lotto.py 12345 1337 33333 0 65535``` will use those five trainer ids to calculate the odds.

How to interpret the results? The first table displays the number of lottery ids for each tier of prize as well as the
percentage chance. In the sample table above, there is a 0% chance to match 0 digits because there are no lottery numbers that
would not match at least 1 digit in our 50 id set. The second table shows the chance of matching at least a certain number of
digits. Our sample set has a 100% chance of at least matching 1 digit, with a roughly 39% chance of matching
at least two digits.

What does this mean? Each unique id you get from trading with other players will increase the chances of winning the lottery.
At 20 unique ids, there is a decent chance of securing a 100% chance of at least a single digit match every time you play the
lottery. At 50 unique ids, you already have a roughly 40% chance of winning at least the 2 digit prize or above. Of course,
if you are unlucky and get a set such as 11111, 11211, 11311, 11411, 11511, and so on, then your odds for winning are
significantly lowered, but such a set is unlikely to occur.

Time complexity O(n).
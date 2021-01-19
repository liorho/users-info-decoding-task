# Users Info Decoding Task

## The Challenge
I'd become a decoder for a couple of hours and accepted a challenge (from a big cyber company):
write a short script which decode a coded file (the `ex_v7.txt` file) and extract users info from it

## The Hint
I'd given one user info:
```
first name: Cary
last name: Thompson
phone: 0467674021
time: 2013-06-11 15:57:19
```

## The Solution
So that's exactly what I did - I found a pattern and created the `decoder.py` file to extract the users info from the `ex_v7.txt` file.
Instead of just printing the users dictionaries, the script creates another `.txt` file with the users decoded info (`users_info.txt`) 🤘
***
### Running This Thing
1. Clone the repo
2. Delete the `users_info.txt` file
3. Run `python decoder.py`
4. See the magic ✨

### Tech
* python
* regex


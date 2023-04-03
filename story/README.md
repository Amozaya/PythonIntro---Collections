# Python-man - superhero story

## Dictionary

First part of code creates a dictionary that stores our story. It split into 3 keys:

*Start

*Middle

*End

```commandline
story1 = {
    "start": "Our hero was a regular student who got once bit by a radio-active Python and got programming super powers.",
    "middle": "Once, an evil corporation created a computer virus that meant to spread around the world and corrupt every computer.",
    "end": "Our hero used his programming skills to stop the virus from spreding and save the world from chaos."
}
```

### Check the dictionary data and type
This code print the dictionary and it's type to ensure it's correct
```commandline
print(story1)
print(type(story1))
```

### Print keys and values separately
This part of code just prints Keys and Values separately
```commandline
print(story1.keys())
print(story1.values())
```

### Add hero name to the dictionary
This code adds a new pair to the dictionary
```commandline
story1["hero"] = "Python-man"
```


### Final result
Now it's a final part of the code that prints the story by each key individually in order
```commandline
print(story1["hero"])
print(story1["start"])
print(story1["middle"])
print(story1["end"])
```
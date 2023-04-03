story1 = {
    "start": "Our hero was a regular student who got once bit by a radio-active Python and got programming super powers.",
    "middle": "Once, an evil corporation created a computer virus that meant to spread around the world and corrupt every computer.",
    "end": "Our hero used his programming skills to stop the virus from spreding and save the world from chaos."
}

print(story1)
print(type(story1))

print(story1.keys())
print(story1.values())

story1["hero"] = "Python-man"

print(story1["hero"])
print(story1["start"])
print(story1["middle"])
print(story1["end"])
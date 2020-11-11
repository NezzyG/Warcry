import random


names = {
    "fname": [
         "Robik",
         "Mihai",
         "Radu",
         "Diab",
         "Teo",
         "Irina",
         "Bogdan",
         "Goerge",
         "Stefan",
         "Paul",
         "Vasile",
         "Ovidiu",
         "Florin",
         "Cornel",
         "Matei",
         "Tyrone",
         "Robik",
         "Romeo",
         "Costel",
         "Marinica",
         "Leana",
         "Atimut",
         "Chad",
         "Jamal",
         "Putifric",
         "Slobozel",

    ],

    "lname":[
        "Giosan",
        "Stancu",
        "Chraif",
        "Popa",
        "Botez",
        "Paladi",
        "Bombardieru",
        "Dumitru",
        "Ionesc",
        "Ciobanu",
        "Florea",
        "Nagy",
        "Constantinescu",
        "Cojocaru",
        "Don Pulon",
        "Fantastik",
        "Abagiu",
        "Whisperwind",
        "Stormrage",
        "Thunderwrath",
        "Truthseeker",
        "Lights bane",
        "Slayer of the meek",
        "Poxbringer",
        "cronescovici",
        "Fara Frik"

     ],
    "nickname":[
        "\"Faggot\"",
        "\"Gotta gas em all\"",
        "\"I aint afraid of no Zog\"",
        "\"Going mental on the oriental\"",
        "\"Spook the spooks\"",
        "\"Pulling the trigger on every nigger\"",
        "\"the beaner brainer\"",
        "\"One man klan\"",
        "\"the mongoloid murdering maniac\"",
        "\"The racial pain hurricane\"",
        "\"The nigger grave digger\"",
        "\"Kebab shishkebab\"",
        "\"Slope slicer\"",
        "\"Chopping the ching-chong\"",
        "\"Going rambo on sambo\"",
        "\"Drowned the chink in the Kitchen Sink\"",
        "\"Three reichs and you're out\"",
        "\"Straight outta Auschwitz\"",
        "\"Kike on a spike\"",
        "\"Gassing Schlomo in slo-mo\"",
        "\"Ten-ton terror of Tel'aviv\""


    ]

}
races=["orc","human","elf","undead"]


def get_name():
    fname = random.choice(names["fname"])
    lname = random.choice(names["lname"])
    return f"{fname} {lname}"


def get_nickname():
    return random.choice(names["nickname"])


def get_random_race():
    return random.choice(races)


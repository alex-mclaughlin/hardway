from sys import exit


def start():
    name = input("\nHello and welcome to Clique Brands. May I have your name? ")

    if type(name) == int:
        print("You go by a number? Get it fam but I need a name please, try again ")
        start()
    else:
        print("Welcome {}. \nYou are a top designer and we need your expertise.\n".format(name))
        project = input("Will you be designing a capsule or a single piece for the collection? " )
        project_selector(project)

#this function forces user to choose either capsule or single piece
def project_selector(project):
    if "capsule" in project:
        capsule()
    elif "piece" in project:
        piece()
    else:
        print ("You did not choose capsule or singe piece. Please try again. ")
        project_selector(input("Will you be designing a capsule or a single piece for the collection? " ))

def capsule():
    print ("Capsule it is!")
    weeks = int(input("\nHow many weeks do we have to complete the capsule design? "))
    if weeks > 26:
        print ("You have way too much time, why don't you try a single piece! ")
        piece()
    elif 9 < weeks <= 26:
        cap_count = 4
        capsule_picker(cap_count)
    elif 6 < weeks <= 9:
        cap_count = 3
        capsule_picker(cap_count)
    elif 3 < weeks <= 6:
        cap_count = 2
        capsule_picker(cap_count)
    elif 0 < weeks <= 3:
        cap_count = 1
        capsule_picker(cap_count)
    else:
        print ("I need a number of weeks, thanks. ")
        capsule()

def capsule_picker(cap_count):
    print ("\nDue to the number of weeks you have, you will be able to choose {} capsule pieces".format(cap_count))

    list_a = []
    while int(len(list_a)) < cap_count:
        name = input("\nChoose a capsule item: \nActive \nBoots \nHeels \nAccesories \nTops \nBottoms\n>>>" )
        list_a.append(name)
    print ("\Here are capsule items you will design:", ", ".join(list_a))


def piece():
    print ("You will design a single piece for a fabulous collection!")


start()

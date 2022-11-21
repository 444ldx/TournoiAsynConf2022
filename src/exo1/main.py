def exercice1():
    print(" ")
    print("Exercice 1 : Nommons les étoiles")
    print(" ")
  
    mission_code = str()
    steps = list()
    step_number = 1
    
    while True:
        step = input(f"Entrez l'étape numero {step_number} : ")
        if len(step) == 0:
            break
        steps.append(step)
        step_number += 1
    
    initials_steps = [step[:1].upper() for step in steps]
    
    for i in range(len(steps)):
        if not steps[i][:1] in mission_code:
            mission_code += initials_steps[i] + str(len(steps[i])-1)
        else:
            number = 1
            for i2 in range(len(steps[i])):
                if not steps[i][:1+number] in mission_code:
                    mission_code += steps[i][:1].upper() + steps[i][1:1+number].lower() + str(len(steps[i])-1-number)
                    break
                number += 1

    print(" ")
    print(mission_code)
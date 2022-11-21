import base64

def tri_insertion(L):
    N = len(L)
    for n in range(1,N):
        key = L[n]
        j = n-1
        while j>=0 and L[j] > key:
            L[j+1] = L[j]
            j = j-1
        L[j+1] = key

def exercice4():
    print(" ")
    print("Exercice 4 : La supernova")
    print(" ")
  
    code_system = str()
    step_number = 1
  
    while True:
        code_system_input = input(f"Entrez le code secret du système (ligne {step_number}) : ")
        if len(code_system_input) == 0:
            break 
        code_system = code_system + code_system_input
        step_number += 1
    
    code_system = str(base64.b64decode(code_system))
    handling_code_system = code_system.replace("b'", "").split("}")
    handling_code_system_step_2 = list()
    handling_code_system_step_3 = list()
    final_json = list()
    tri = dict()
    stars_distances = list()
    
    for i in range(len(handling_code_system)):
        handling_code_system_step_2.append(handling_code_system[i].split(","))
       
    for i in range(len(handling_code_system_step_2)):
        for i2 in range(len(handling_code_system_step_2[i])):
            handling_code_system_step_2[i][i2] = handling_code_system_step_2[i][i2].replace(" ", "").replace('"', "").replace("\\n", "").replace("{", "").replace("[", "").replace("]", "")
    
    for i in range(len(handling_code_system_step_2)):
        for i2 in range(len(handling_code_system_step_2[i])):
            handling_code_system_step_3.append(handling_code_system_step_2[i][i2].split(":"))
            
    premier = 0
    for i in range(len(handling_code_system_step_3)//5):
        final_json.append(handling_code_system_step_3[premier:premier+4])
        premier += 5
    
    for i in range(len(final_json)):
        tri[int(final_json[i][2][1])] = i
    
    stars_distances = list(tri.keys())
    
    for i in range(len(stars_distances)):
        stars_distances[i] = int(stars_distances[i])

    tri_insertion(stars_distances)
    
    for elem in stars_distances:
        print(" ")
        print(f"Nom : {final_json[tri[elem]][0][1]}")
        print(f"Taille : {final_json[tri[elem]][1][1]} km")
        print(f"Masse : {final_json[tri[elem]][3][1]} tonnes")
        print(f"Distance à l'étoile : {final_json[tri[elem]][2][1]} km")
        print(" ")
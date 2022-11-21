def adjoining(alphabet, area_map, case):
  result = list()
  for i in range(len(alphabet)):
    for character in alphabet[i]:
      if character == case[:1]:
        try:
          if area_map[alphabet.index(character)].get(character)[int(case[1:2])
                                                                - 1] == "_":
            print(True)
            result.append(f"{character}{int(case[1:2])-1}")
        except:
          pass

        try:
          if area_map[alphabet.index(character)].get(character)[int(case[1:2])
                                                                - 2] == "_":
            print(True)
            result.append(f"{character}{int(case[1:2])-2}")
        except:
          pass

        try:
          if area_map[alphabet.index(character) - 1].get(alphabet[i - 1])[int(
              case[1:2])] == "_":
            print(True)
            result.append(f"{alphabet[i-1]}{int(case[1:2])}")
        except:
          pass

        try:
          if area_map[alphabet.index(character) + 1].get(
              alphabet[i + 1])[int(case[1:2]) - 1] == "_":
            print(True)
            result.append(f"{alphabet[i+1]}{int(case[1:2])}")
        except:
          pass

        return result


def exercice5():
  print(" ")
  print("Exercice 5 : Attaque de météorite")
  print(" ")

  area = list()
  X_position = str()
  V_position = str()
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  step_number = 1
  while True:
    area_input = input(
      f"Entrez le plan du champ d'astéroïdes (ligne {step_number}) : ")
    if len(area_input) == 0:
      break
    area.append(area_input)
    step_number += 1

  for i in range(len(area)):
    area[i] = list(area[i].strip())

  area_map = [""] * len(area)

  for i in range(len(area)):
    area_map[i] = {alphabet[i]: []}
    for i2 in range(len(area[i])):
      area_map[i][alphabet[i]].append(area[i][i2])
      if area[i][i2] == "V":
        V_position = alphabet[i] + str(i2 + 1)
      elif area[i][i2] == "X":
        X_position = alphabet[i] + str(i2 + 1)

  print(" ")
  print(f"X -> {X_position}")
  print(f"V -> {V_position}")
  print(" ")
  print("Matrice : ")
  print(area_map)

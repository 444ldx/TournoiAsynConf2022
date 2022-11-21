def exercice2():
    print(" ")
    print("Exercice 2 : Mission Phantom 2064")
    print(" ")
  
    features = input("Caractéristiques du vaisseau : ")
    duration = input("Temps de trajet : ")
    
    handling_features = features.split(";")
    final_features = list()
    
    for e in handling_features:
        a = e.split("=")
        final_features.append(a)
    
    for i in range(len(final_features)):
        if i > 0:
            result = str()
            for character in final_features[i][1]:
                if character.isdigit():
                    result += character
            try:
                final_features[i][1] = int(result)
                duration = int(duration)
            except:
                raise Exception("Les valeurs des caractérisiques et/ou le temps de trajet doient être des nombres entiers !")

    try:
        calcul = final_features[1][1]*final_features[2][1]*duration*24
    except:
      raise Exception("Les caractéristiques ne sont pas au bon format !")

    print(f"\n{round(calcul, 2)} €")
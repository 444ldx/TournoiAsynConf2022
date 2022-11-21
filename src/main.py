import exo1.main as exo1
import exo2.main as exo2
import exo3.main as exo3
import exo4.main as exo4
import exo5.main as exo5

def main():
  print("---- ASYNCONF2022, Projet de ldx ----")
  print(" ")
  print("Exercice 1 à 4 totalement fonctionnels.")
  print("Exercice 5 partiellement fonctionnel.")
  print(" ")
  choice = input("Quel exercice voulez-vous voir ? ")

  if choice == "1":
    exo1.exercice1()
  elif choice == "2":
    exo2.exercice2()
  elif choice == "3":
    exo3.exercice3()
  elif choice == "4":
    exo4.exercice4()
  elif choice == "5":
    exo5.exercice5()
  else:
    print("Oups, exercice introuvable !")

main()
#Proměnná se jménem 
jmeno = "Otakar" 

#Vypíše jmeno male
male_jmeno = 'Otakar'.lower()
print(male_jmeno)

#Vypíše počet vyskytu j ve jméně
pocet_jmeno = 'Otakar'.count("j")
print(pocet_jmeno)

#Shoda hesla 
heslo_puvod = input("Vložte své heslo: ")
heslo_nové = input("Vložte své heslo: ")

if heslo_puvod == heslo_nové:
    print("Hesla jsou stejné.")
else:
    print("Hesla nejsou stejná.")

#Seznam s pěti hodnotami
seznam = [16, "kartel", 98, "projektor", "herdek"]

#Vypíše první a prostřední hodnotu seznamu 
prvni = seznam[0]
print(prvni)
stred = seznam[3]
print(stred)

#Zaměna hodnoty v seznamu 
seznam[1] = "auto"
seznam[2] = 89
seznam[4] = "zelená"
print(seznam)
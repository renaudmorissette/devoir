nom_dict = {"nom": "Renaud", "age": 18, "ville": "St-jean"}
print(nom_dict["ville"])
nom_dict["profession_future"] = "ingénieur"
nom_dict["age"] = 20
del nom_dict["ville"]
etudiant = {"nom": "Gates", "prenom": "Bill", "age": 18, "notes": {"maths": 16, "français": 13, "chimie": 10}}

print(etudiant["notes"]["chimie"])
etudiant["anglais"] = 16
for cle, valeur in etudiant["notes"].items():
    print(f"La clé {cle} a pour valeur {valeur}")

aaa
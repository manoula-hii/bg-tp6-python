
# listes, slide 26

students = [
    (1000, "john", "doe", 14, 5),
    (2000, "bob", "carlton", 7, 1),
    (3000, "rayan", "smith", 13, 3)
]

#Fonctions, slide 40

def B(note: float) -> bool:
    return note >= 10

#Boucles, slide 38 et Conditions if/else, slide 35

def A(students: list) -> list:
    resultats = []

    for student in students:
        matricule = student[0]
        note = student[3]

        if B(note):
            resultat = "ADMIS"
        else:
            resultat = "AJOURNE"

        resultats.append({
            "mat": matricule,
            "result": resultat
        })

    return resultats


def C(students):
    for student in students:
        if B(student[3]):
            print(student[0], ":", "ADMIS")
        else:
            print(student[0], ":", "AJOURNE")

print(A(students))
C(students)

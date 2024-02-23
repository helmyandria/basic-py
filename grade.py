grade = ""
nilai = int(input("masukkan nilai : "))

if nilai >= 90:
    grade = "A"
elif nilai >=80 and nilai <=89:
    grade = "B"
elif nilai >=60 and nilai <=79:
    grade = "C"
else :
    grade = "D"

print("grade nilaimu adalah " + grade)
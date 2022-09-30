from datetime import date


class personne:
    def __init__(self,nom, prenom, birthyear, birthmonth, birthday, nationalité):
        self.nom=nom
        self.prenom = prenom
        self.birthyear = birthyear
        self.birthmonth = birthmonth
        self.birthday=birthday
        self.nationalité=nationalité

    def calcule_age(self):
        today = date.today()
        age = today.year - self.birthyear -((today.month, today.day) <(self.birthmonth, self.birthday))
        return age

    def update_nationality(self,NewNationality):
        self.nationalité=NewNationality

pers1=personne("Battou","Karim",1991,7,1,"Algérienne")
print(pers1.calcule_age())
print(pers1.nationalité)
pers1.update_nationality("Américanine")
print(pers1.nationalité)

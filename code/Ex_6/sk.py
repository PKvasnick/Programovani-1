

class Zvire:
    """ Tŕída definující zvíře s daným jménoem a zvukem"""
    
    def __init__(self, jmeno, zvuk):
        self.jmeno = jmeno
        self.zvuk = zvuk

    def slysi_na(self, jmeno):
        return self.jmeno == jmeno

    def ozvi_se(self):
        print(f"{self.jmeno} říká {self.zvuk}")
        return

    def __str__(self):
        return f"Zvire jmenem {self.jmeno} vydavajici zvuk {self.zvuk}"

    def __repr__(self):
        return f"Zvire(jmeno = {self.jmeno}, zvuk = {self.zvuk}"
    
    def __eq__(self, jine):
        return (self.jmeno == jine.jmeno) and (self.zvuk == jine.zvuk)

    def __bool__(self):
        return bool(self.jmeno and self.zvuk)


class Kocka(Zvire):

    def __init__(self, jmeno, zvuk):
        Zvire.__init__(self, jmeno, zvuk)
        self.pocet_zivotu = 9

    def slysi_na(self, jmeno):
        return False



    

        

    

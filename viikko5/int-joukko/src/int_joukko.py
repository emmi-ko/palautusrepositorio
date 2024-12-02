KAPASITEETTI = 5
OLETUSKASVATUS = 5

"""Olisin muuttanut myös funktioitten nimiä, mutten sitten olisi pitänyt koskea testeihin, niin jätin rauhaan."""

class IntJoukko:
    
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.tarkista_argumentti(kapasiteetti, "kapasiteetti")
        self.kasvatuskoko = self.tarkista_argumentti(kasvatuskoko, "kasvatuskoko")
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def tarkista_argumentti(self, argumentti, tyyppi):
        if argumentti is None:
            if tyyppi == "kapasiteetti":
                return KAPASITEETTI
            return OLETUSKASVATUS
        elif not isinstance(argumentti, int) or argumentti < 0:
            raise Exception(f"Väärä {tyyppi}")  
        else:
            return argumentti

    def kuuluu(self, n):
        for luku in self.ljono:
            if n == luku:
                return True
        
        return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm += 1

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.korvaa_vanha_lista(self.ljono)
    
    def korvaa_vanha_lista(self, vanhalista):
        uusi_lista = self._luo_lista(len(vanhalista)+self.kasvatuskoko)
        self.kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista

    def poista(self, n):
        poistettava_indeksi = -1

        for indeksi in range(0, self.alkioiden_lkm):
            if n == self.ljono[indeksi]:
                poistettava_indeksi = indeksi   
                self.ljono[indeksi] = 0
                break

        if poistettava_indeksi != -1:
            self.siirra_listaa_vasemmalle(poistettava_indeksi)
            self.alkioiden_lkm -= 1

    def siirra_listaa_vasemmalle(self, poistettava_indeksi):
        for indeksi in range(poistettava_indeksi, self.alkioiden_lkm - 1):
            siirron_lahtoindeksi = self.ljono[indeksi]
            self.ljono[indeksi] = self.ljono[indeksi + 1]
            self.ljono[indeksi + 1] = siirron_lahtoindeksi

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        lista = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            lista.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            lista.lisaa(b_taulu[i])

        return lista

    @staticmethod
    def leikkaus(a, b):
        lista = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    lista.lisaa(b_taulu[j])

        return lista

    @staticmethod
    def erotus(a, b):
        lista = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            lista.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            lista.poista(b_taulu[i])

        return lista

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.ljono[i]) + ", "
            tuotos += str(self.ljono[self.alkioiden_lkm - 1]) + "}"
            return tuotos

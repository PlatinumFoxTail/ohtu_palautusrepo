from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KiviPaperiSakset):
    # toteutetaan metodi pelityypin mukaisesti
    def __init__(self):
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        self.tekoaly.aseta_siirto(ensimmaisen_siirto)

        return tokan_siirto
import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        ### v4t3 ###
        # palautetaan aina arvo 42
        #self.viitegeneraattori_mock.uusi.return_value = 42
        ### v4t3 ###

        ### v4t4 ###
        self.viitegeneraattori_mock.return_value = Mock(wraps=Viitegeneraattori())
        ### v4t4 ###

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 20
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 10)
            if tuote_id == 3:
                return Tuote(3, "leipä", 3)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_data(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("mikko", "11111")

        ### v4t3 ###
        # varmistetaan, että metodia tilisiirto on kutsuttu
        #self.pankki_mock.tilisiirto.assert_called_with('mikko', 42, "11111", '33333-44455', 5)
        ### v4t3 ###

        ### v4t4 ###
        self.pankki_mock.tilisiirto.assert_called_with('mikko', ANY, "11111", '33333-44455', 5)
        ### v4t4 ###

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_data(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("mikko", "11111")

        ### v4t3 ###
        # varmistetaan, että metodia tilisiirto on kutsuttu
        #self.pankki_mock.tilisiirto.assert_called_with('mikko', 42, "11111", '33333-44455', 5)

        ### v4t4 ###
        self.pankki_mock.tilisiirto.assert_called_with('mikko', ANY, "11111", '33333-44455', 5)
        ### v4t4 ###

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_kaksi_eri_tuotetta(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "22222")

        ### v4t3 ###
        # varmistetaan, että metodia tilisiirto on kutsuttu
        #self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, "22222", '33333-44455', 15)
        ### v4t3 ###

        ### v4t4 ###
        self.pankki_mock.tilisiirto.assert_called_with('pekka', ANY, "22222", '33333-44455', 15)
        ### v4t4 ###

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_kaksi_samaa_tuotetta(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("eero", "33333")

        ### v4t3 ###
        # varmistetaan, että metodia tilisiirto on kutsuttu
        #self.pankki_mock.tilisiirto.assert_called_with('eero', 42, "33333", '33333-44455', 10)
        ### v4t3 ###

        ### v4t4 ###
        self.pankki_mock.tilisiirto.assert_called_with('eero', ANY, "33333", '33333-44455', 10)
        ### v4t4 ###

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_kaksi_eri_tuotetta_toinen_tuote_loppu(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("lauri", "44444")

        ### v4t3 ###
        # varmistetaan, että metodia tilisiirto on kutsuttu
        #self.pankki_mock.tilisiirto.assert_called_with('lauri', 42, "44444", '33333-44455', 5)
        ### v4t3 ###

        ### v4t4 ###
        self.pankki_mock.tilisiirto.assert_called_with('lauri', ANY, "44444", '33333-44455', 5)
        ### v4t4 ###

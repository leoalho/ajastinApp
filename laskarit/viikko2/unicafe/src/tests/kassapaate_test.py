import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
  def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

  def test_rahat_ja_myydyt_ateriat_alussa_oikein(self):
    self.assertEqual(self.kassapaate.edulliset, 0)
    self.assertEqual(self.kassapaate.maukkaat, 0)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
  
  def test_kateisosto_edullisesti_lisaa_rahaa_ja_myytyja_lounaita_kun_rahat_riittaa(self):
    self.kassapaate.syo_edullisesti_kateisella(500)

    self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    self.assertEqual(self.kassapaate.edulliset, 1)

  def test_kateisosto_edullisesti_palauttaa_oikean_maaran_kun_rahat_riittaa(self):
    maksu = self.kassapaate.syo_edullisesti_kateisella(500)

    self.assertEqual(maksu, 260)

  def test_kateisosto_edullisesti_ei_lisaa_rahaa_eika_myytyja_lounaita_kun_rahat_ei_riita(self):
    self.kassapaate.syo_edullisesti_kateisella(100)

    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(self.kassapaate.edulliset, 0)

  def test_kateisosto_edullisesti_palauttaa_oikean_maaran_kun_rahat_ei_riita(self):
    maksu = self.kassapaate.syo_edullisesti_kateisella(100)

    self.assertEqual(maksu, 100)

  def test_kateisosto_maukkaasti_lisaa_rahaa_ja_myytyja_lounaita_kun_rahat_riittaa(self):
    self.kassapaate.syo_maukkaasti_kateisella(500)

    self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    self.assertEqual(self.kassapaate.maukkaat, 1)

  def test_kateisosto_maukkaasti_palauttaa_oikean_maaran_kun_rahat_riittaa(self):
    maksu = self.kassapaate.syo_maukkaasti_kateisella(500)

    self.assertEqual(maksu, 100)

  def test_kateisosto_maukkaasti_ei_lisaa_rahaa_eika_myytyja_lounaita_kun_rahat_ei_riita(self):
    self.kassapaate.syo_maukkaasti_kateisella(100)

    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(self.kassapaate.edulliset, 0)

  def test_kateisosto_maukkaasti_palauttaa_oikean_maaran_kun_rahat_ei_riita(self):
    maksu = self.kassapaate.syo_maukkaasti_kateisella(100)

    self.assertEqual(maksu, 100)

  def test_korttiosto_edullisesti_palauttaa_true_vahentaa_rahaa_kortilta_ja_lisaa_myytyja_lounaita_kun_rahat_riittaa(self):
    maksu = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
    self.assertEqual(self.kassapaate.edulliset, 1)
    self.assertEqual(maksu, True)

  def test_korttiosto_edullisesti_palauttaa_false_ei_vahenna_rahaa_kortilta_eika_lisaa__myytyja_lounaita_kun_rahat_ei_riita(self):
    maksukortti = Maksukortti(100)

    maksu = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(str(maksukortti), "Kortilla on rahaa 1.00 euroa")
    self.assertEqual(self.kassapaate.edulliset, 0)
    self.assertEqual(maksu, False)

  def test_korttiosto_maukkaasti_palauttaa_true_vahentaa_rahaa_kortilta_ja_lisaa__myytyja_lounaita_kun_rahat_riittaa(self):
    maksu = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
    self.assertEqual(self.kassapaate.maukkaat, 1)
    self.assertEqual(maksu, True)

  def test_korttiosto_maukkaasti_palauttaa_false_ei_vahenna_rahaa_kortilta_eika_myytyja_lounaita_kun_rahat_ei_riita(self):
    maksukortti = Maksukortti(100)

    maksu = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(str(maksukortti), "Kortilla on rahaa 1.00 euroa")
    self.assertEqual(self.kassapaate.maukkaat, 0)
    self.assertEqual(maksu, False)

  def test_kortille_ladattaessa_rahaa_kassan_rahamaara_ja_kortin_saldo_muuttuvat(self):
    self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)

    self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
    self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

  def test_kortille_ladattaessa_negatiivinen_maara_rahaa_kassan_rahamaara_ja_kortin_saldo_eivat_muutu(self):
    self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)

    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
  
import unittest
def contador(string):
    tupla=("a","e","i","o","u")
    rdo={}
    for letra in string:
        letra = letra.lower()
        if letra in tupla:
            if letra in rdo.keys():
                rdo[letra]+=1 #agrego al diccionario "rdo" la clave "letra"de valor 1 
            else:
                rdo[letra]=1
    return rdo

           

    

class Testervocales (unittest.TestCase):

    def test_1(self):
        string = "tryhgf"
        rdo= contador(string)
        self.assertEqual(rdo, {})
        
    def test_2(self):
        string= "abba"
        rdo=contador(string)
        self.assertEqual(rdo, {'a':2})
        
    def test_3(self):
        string= "AteniOn"
        rdo=contador(string)
        self.assertEqual(rdo, {'a':1, 'o':1, 'i':1, 'e':1})


    def test_4(self):
        string= "maria fue al baño"
        rdo=contador(string)
        self.assertEqual(rdo, {'a':4, 'i':1, 'e':1, 'o':1, 'u':1})

    def test_5(self):
        string= "casamiento"
        rdo=contador(string)
        self.assertEqual(rdo, {'a':2, 'i':1, 'e':1, 'o':1})

    def test_6(self):
        string= "hoy es un gran dia"
        rdo=contador(string)
        self.assertEqual(rdo, {'a':2, 'i':1, 'e':1, 'o':1, 'u':1})
unittest.main()
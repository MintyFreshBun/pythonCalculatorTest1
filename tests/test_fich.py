import unittest
from unittest import mock
import csv
import fich
import pathlib as pl


def criaFichTeste(filename):
    dados =[['257', '+', '38'],
        ['5', 'x', '2'],
        ['85', 'x','927'],
        ['8','tab','5']]
    with open(filename, 'w',newline='') as f:
        novo_fich=csv.writer(f)
        novo_fich.writerows(dados)





class testar_fich(unittest.TestCase):
    def test_lefFich(self):
        fichTeste = r'c:\temp\file2.csv'
        criaFichTeste(fichTeste)
        lista = fich.lerFich(fichTeste)
        self.assertListEqual(lista, [['257', '+', '38'], ['5', 'x', '2'], ['85', 'x','927']])

    def test_apagaFich(self):
        filename = r'c:\temp\file2.csv'
        fich.apagaFich(filename)
        path = pl.Path(filename)
        self.assertFalse(path.is_file)

    #mock.patch('fich.calc.calcula', return_value=(2, '1+2=3', 'um mais dois é igual a três'))
    exp_tab_data = ['8x1 = 8',
                  '8x2 = 16',
                  '8x3 = 24',
                  '8x4 = 32',
                  '8x5 = 40',
                  '8x6 = 48',
                  '8x7 = 56',
                  '8x8 = 64',
                  '8x9 = 72',
                  '8x10 = 80'
                  ]


    mock.patch('fich.calc.calcula.tabuada' ,return_value=(exp_tab_data))
    def test_proFich(self, mock_calculo):
        fichTeste = r'c:\temp\file2.csv'
        criaFichTeste(fichTeste)
        fich.procFich(fichTeste)

        lista = fich.lerFich(r'c:\temp\file2.csv')

        listaPrevista=[]
        for i in range(len(lista)):
            listaPrevista.append(['1+2=3'])

        self.assertListEqual(lista, listaPrevista)





if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python

class main():
    def __init__(self):
        self.fila = [Estados(3, 0, 3, 0, 'esquerda')]
        self.solucao = None

    def verificar_solucao(self):







if __name__ == '__main__':
    main()


class Estados():
    def __init__(self, mis_esq, mis_dir, cani_esq, cani_dir, lado):
        
        self.mis_esq = mis_esq
        self.mis_dir = mis_dir
        self.cani_esq = cani_esq
        self.cani_dir = cani_dir
        self.lado = lado
        self.pai = None
        self.filhos = []

    def verificar_final(self):
        valido_esq = self.mis_esq == self.cani_esq == 0
        valido_dir = self.mis_dir == self.cani_dir == 3

        print(valido_esq and valido_dir)

        return valido_esq and valido_dir


    def gerar_filhos(self):
        retorno_lado = 'dir' if self.lado == 'esq' else 'esq'

        regrasBarco = [
            {'missionarios': 2, 'canibais': 0},
            {'missionarios': 1, 'canibais': 0},
            {'missionarios': 1, 'canibais': 1},
            {'missionarios': 0, 'canibais': 1},
            {'missionarios': 0, 'canibais': 1},
        ]

        for movimento in regrasBarco:
            if self.lado == 'esq':
                if(self.mis_dir < movimento['missionarios']):
                    newMiss_dir = self.mis_dir + movimento['missionarios']
                else:
                    newMiss_dir = self.mis_dir - movimento['missionarios']

                if (self.mis_esq < movimento['missionarios']):
                    newMiss_esq = self.mis_esq + movimento['missionarios']
                else:
                    newMiss_esq = self.mis_dir - movimento['missionarios']

                if (self.cani_dir < movimento['canibais']):
                    newCani_dir = self.cani_dir + movimento['canibais']
                else:
                    newCani_dir = self.cani_dir - movimento['canibais']

                if (self.cani_esq < movimento['canibais']):
                    newCani_esq = self.cani_esq + movimento['canibais']
                else:
                    newCani_esq = self.cani_esq - movimento['canibais']

            else:
                newMiss_dir = self.mis_dir - movimento['missionarios']
                newMiss_esq = self.mis_esq + movimento['missionarios']
                newCani_dir = self.mis_dir - movimento['canibais']
                newCani_esq = self.mis_esq - movimento['canibais']











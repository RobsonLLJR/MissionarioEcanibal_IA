#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cmath import sqrt


class Estados():
    def __init__(self, mis_esq, mis_dir, cani_esq, cani_dir, lado):

        self.mis_esq = mis_esq
        self.mis_dir = mis_dir
        self.cani_esq = cani_esq
        self.cani_dir = cani_dir
        self.lado = lado
        self.pai = None
        self.filhos = []
        self.valor = 6;
        self.posicao = []



    def __str__(self):
        return 'Mis: {}\t| Mis: {}\nCani: {}\t| Cani: {}'\
            .format(self.mis_esq, self.mis_dir, self.cani_esq, self.cani_dir)


    def estado_valido(self):
        if(self.mis_esq < 0) or (self.mis_dir < 0) or (self.cani_dir < 0) or (self.cani_esq < 0):
            return False

        return ((self.mis_esq == 0 or self.mis_esq >= self.cani_esq) and
                (self.mis_dir == 0 or self.mis_dir >= self.cani_dir))



    def verificar_final(self):
        valido_esq = self.mis_esq == self.cani_esq == 0
        valido_dir = self.mis_dir == self.cani_dir == 3

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
                newMiss_dir = self.mis_dir - movimento['missionarios']
                newMiss_esq = self.mis_dir - movimento['missionarios']
                newCani_dir = self.cani_dir - movimento['canibais']
                newCani_esq = self.cani_esq - movimento['canibais']

            else:
                newMiss_dir = self.mis_dir - movimento['missionarios']
                newMiss_esq = self.mis_esq + movimento['missionarios']
                newCani_dir = self.mis_dir - movimento['canibais']
                newCani_esq = self.mis_esq - movimento['canibais']

            filho = Estados(newMiss_esq, newMiss_dir, newCani_esq, newCani_dir, retorno_lado)

            teste = sqrt((newMiss_esq + newCani_esq) * (newMiss_esq + newCani_esq) + (newMiss_dir + newCani_dir) * (newCani_dir + newCani_dir))

            if(self.valor > teste):
                filho.pai = self
                filho.valor = teste

                if filho.estado_valido():
                    self.filhos.append(filho)



class main():
    def __init__(self):
        self.fila = [Estados(3, 0, 3, 0, 'esquerda')]
        self.solucao = None

    def gerar_solucao_valida(self):
        for componente in self.fila():
            if componente.verificar_final():
                self.solucao = [componente]
                while componente.pai:
                    self.solucao.insert(0, componente.pai)
                    elemento = elemento.pai
                break;
            componente.gerar_filhos()
            self.fila.extend(componente.filhos)





if __name__ == '__main__':
    main()

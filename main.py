






class Estados():
    def __init__(self, mis_esq, mis_dir, cani_esq, cani_dir, lado):

        self.mis_esq = mis_esq
        self.mis_dir = mis_dir
        self.cani_esq = cani_esq
        self.cani_dir = cani_dir
        self.lado = lado
        self.pai = None
        self.filhos = []

    def __str__(self):
        return 'Missionarios: {}\t| Missionarios: {}\nCanibais: {}\t| Canibais: {}'.format(
            self.mis_esq, self.mis_dir, self.cani_esq, self.cani_dir)


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

            filho = Estados(newMiss_esq, newMiss_dir, newCani_esq, newCani_dir, retorno_lado)

            filho.pai = self

            if filho.estado_valido():
                for estado in filho:
                    print(estado, '\n----------------')
                self.filhos.append(filho)




class main():
    def __init__(self):
        self.fila = [Estados(3, 0, 3, 0, 'esquerda')]
        self.solucao = None

    def gerar_solucao_valida(self):
        for elemento in self.fila():
            if elemento.verificar_final():
                self.solucao = [elemento]
                while elemento.pai:
                    self.solucao.insert(0, elemento.pai)
                    elemento = elemento.pai
                break;
            elemento.gerar_filhos()
            self.fila.extend(elemento.filhos)





if __name__ == '__main__':
    main()

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


    def verificar_final(self):
        valido_esq = self.mis_esq == self.cani_esq == 0
        valido_dir = self.mis_dir == self.cani_dir == 3

        return valido_esq and valido_dir




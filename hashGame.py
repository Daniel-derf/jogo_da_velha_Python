# jogo da velha em python


class JogoDaVelha:
    def __init__(self):
        self.jogador_um_posicoes = [False] * 9
        self.jogador_dois_posicoes = [False] * 9
        self.tabuleiro_posicoes = [False] * 9
        self.jogador_um = False
        self.jogador_dois = False
        self.jogo_ativo = False

    def iniciar(self):
        self.jogador_um = True
        self.jogo_ativo = True

    def terminar(self):
        self.jogo_ativo = False

    def trocarJogador(self):
        if self.jogador_um:
            self.jogador_um = False
            self.jogador_dois = True
        else:
            self.jogador_um = True
            self.jogador_dois = False

    def get_status(self):
        return self.jogo_ativo
    
    def mostrar_tabuleiro(self):
        print('_' * 2 + '|' + '_' * 2 + '|' + '_' * 2 + '\n' + '_' * 2 + '|' + '_' * 2 + '|' + '_' * 2 + '\n' + ' ' * 2 + '|' + ' ' * 2 + '|' + ' ' * 2)

    def selecionar_jogador(self, numero_do_jogador):
        if numero_do_jogador == 1:
            self.jogador_um = True
        else:
            self.jogador_dois = True

    def verificar_posicao_livre(self, posicao):
        if self.tabuleiro_posicoes[posicao]:
            return False
        else:
            return True

    # REFATORAR
    def selecionar_posicao(self, posicao):
        if self.jogador_um:
            self.jogador_um_posicoes[posicao] = True
        else:
            self.jogador_dois_posicoes[posicao] = True
        self.tabuleiro_posicoes[posicao] = True

    def verificar_uma_possibilidade_de_vitoria(self, posicoes_no_tabuleiro):
        if all(self.jogador_um_posicoes[i] for i in posicoes_no_tabuleiro) or all(self.jogador_dois_posicoes[i] for i in posicoes_no_tabuleiro):
            return True


    # REFATORAR
    def verificar_todas_possibilidades_de_vitoria(self):
        if self.jogador_um:
            #posições horizontais
            if self.verificar_uma_possibilidade_de_vitoria([0,1,2]):
                return True
            if self.verificar_uma_possibilidade_de_vitoria([3,4,5]):
                return True
            if self.verificar_uma_possibilidade_de_vitoria([6,7,8]):
                return True
            #posicoes verticais
            if self.verificar_uma_possibilidade_de_vitoria([0,3,6]):
                return True
            if self.verificar_uma_possibilidade_de_vitoria([1,4,7]):
                return True
            if self.verificar_uma_possibilidade_de_vitoria([2,5,8]):
                return True
            #posicoes diagonais
            if self.verificar_uma_possibilidade_de_vitoria([0,4,8]):
                return True
            if self.verificar_uma_possibilidade_de_vitoria([2,4,6]):
                return True
            return False

    def limpar_tabuleiro(self):
        self.jogador_um_posicoes = [False] * 9
        self.jogador_dois_posicoes = [False] * 9
        self.tabuleiro_posicoes = [False] * 9

    def verificar_velha(self):
        if False in self.tabuleiro_posicoes:
            return False
        else:
            return True

class JogoDaVelhaConcreto(JogoDaVelha):
    def __init__(self):
        super().__init__()
        self.tabuleiro_visual = [
                                 '1','2','3',
                                 '4','5','6',
                                 '7','8','9'
                                 ]
    def exibir_tabuleiro(self):
        print(self.tabuleiro_visual[0:3])
        print(self.tabuleiro_visual[3:6])
        print(self.tabuleiro_visual[6:])

    def marcar_tabuleiro_visual(self, posicao):
        if self.jogador_um:
            self.tabuleiro_visual[posicao] = 'X'
        else:
            self.tabuleiro_visual[posicao] = 'O'

    def ver_se_ganhou(self):
        if self.verificar_todas_possibilidades_de_vitoria():
            if self.jogador_um:
                print('Jogador um ganhou!')
            else:
                print('Jogador dois ganhou!')
            self.limpar_tabuleiro()
            self.terminar()
        else:
            return False

    def ver_se_deu_velha(self):
        if self.verificar_velha():
            print('O jogo deu velha!')
            self.limpar_tabuleiro()
            self.terminar()
            return True

    def escolher_jogada(self):
        self.exibir_tabuleiro()
        if self.jogador_um:
            print('Jogador UM')
        else:
            print('Jogador DOIS')
        try:
            jogada = int(input('Insira a posição a ser preenchida: \n'))
            jogada -= 1
        except:
            print('Jogada inválida! Digite um valor numérico.')
            self.escolher_jogada()

        if (jogada > -1) and (jogada < 10):
            if self.verificar_posicao_livre(jogada):
                self.selecionar_posicao(jogada)
                self.marcar_tabuleiro_visual(jogada)
                self.ver_se_ganhou()
                self.ver_se_deu_velha()
                self.trocarJogador()
            else:
                print('Posição do tabuleiro já selecionada, tente novamente!')
                self.escolher_jogada()
        else:
            print('Jogada Inválida! Selecione uma posição entre 1 e 9.')
            self.escolher_jogada()





    def jogar(self):
        self.iniciar()


def jogoDaVelha():
    primeiro_jogo = JogoDaVelhaConcreto()
    primeiro_jogo.jogar()
    while(primeiro_jogo.get_status()):
        primeiro_jogo.escolher_jogada()

jogoDaVelha()







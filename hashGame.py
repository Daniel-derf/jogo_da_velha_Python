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

    def terminar_jogo(self):
        self.jogo_ativo = False

    def trocar_jogador(self):
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

    def selecionar_posicao(self, posicao):
        if self.jogador_um:
            self.jogador_um_posicoes[posicao] = True
        else:
            self.jogador_dois_posicoes[posicao] = True
        self.tabuleiro_posicoes[posicao] = True

    def verificar_uma_possibilidade_de_vitoria(self, posicoes_no_tabuleiro):
        if all(self.jogador_um_posicoes[i] for i in posicoes_no_tabuleiro) or all(self.jogador_dois_posicoes[i] for i in posicoes_no_tabuleiro):
            return True

    def verificar_todas_possibilidades_de_vitoria(self):
        posicoes_de_vitoria = [
            [0, 1, 2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]
        ]
        for posicao_de_vitoria in posicoes_de_vitoria:
            if self.verificar_uma_possibilidade_de_vitoria(posicao_de_vitoria):
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
        self.jogada = -1
        self.posicao_esta_livre = True

    def jogar(self):
        self.iniciar()

    def continuar_jogo(self):
        if self.nao_esta_na_primeira_jogada():
            self.trocar_jogador()
        self.escolher_jogada()

    def nao_esta_na_primeira_jogada(self):
        if True in self.tabuleiro_posicoes:
            return True
        return False

    def escolher_jogada(self):
        self.exibir_tabuleiro()
        self.exibir_jogador_da_vez()

        jogada_valida = self.pedir_jogada_e_validar()
        if jogada_valida:
            self.selecionar_jogada()
        else:
            self.escolher_jogada()

    def exibir_tabuleiro(self):
        print(self.tabuleiro_visual[0:3])
        print(self.tabuleiro_visual[3:6])
        print(self.tabuleiro_visual[6:])

    def exibir_jogador_da_vez(self):
        if self.jogador_um:
            print('Jogador UM')
        else:
            print('Jogador DOIS')

    def pedir_jogada_e_validar(self):
        try:
            self.jogada = int(input('Insira a posição a ser preenchida: \n'))
            self.jogada -= 1
            self.validar_valor_entre_opcoes_possiveis()
            self.validar_valor_ja_selecionado()
            return True
        except ValueError:
            if self.posicao_esta_livre:
                print('Jogada Inválida! Selecione uma número inteiro entre 1 e 9.')
            else:
                print('Posição do tabuleiro já selecionada, tente novamente!')
            return False

    def validar_valor_entre_opcoes_possiveis(self):
        if self.jogada > -1 and self.jogada < 10:
            return True
        raise ValueError()

    def validar_valor_ja_selecionado(self):
        if self.verificar_posicao_livre(self.jogada):
            return
        self.posicao_esta_livre = False
        raise ValueError()

    def selecionar_jogada(self):
        self.selecionar_posicao(self.jogada)
        self.marcar_tabuleiro_visual(self.jogada)

    def marcar_tabuleiro_visual(self, posicao):
        if self.jogador_um:
            self.tabuleiro_visual[posicao] = 'X'
        else:
            self.tabuleiro_visual[posicao] = 'O'

    def jogo_terminou(self):
        if self.ver_se_ganhou():
            self.terminar_jogo()
        elif self.ver_se_deu_velha():
            self.terminar_jogo()
        return False

    def ver_se_ganhou(self):
        if self.verificar_todas_possibilidades_de_vitoria():
            if self.jogador_um:
                print('Jogador um ganhou!')
            else:
                print('Jogador dois ganhou!')
            return True
        else:
            return False

    def ver_se_deu_velha(self):
        if self.verificar_velha():
            print('O jogo deu velha!')
            return True


def jogoDaVelha():
    primeiro_jogo = JogoDaVelhaConcreto()
    primeiro_jogo.jogar()
    while(primeiro_jogo.get_status()):
        primeiro_jogo.continuar_jogo()
        primeiro_jogo.jogo_terminou()

jogoDaVelha()







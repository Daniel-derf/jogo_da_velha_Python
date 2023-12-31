# jogo da velha em python
import sys
import io


class JogoDaVelha:
    def __init__(self):
        self.jogador_um_posicoes = [False] * 9
        self.jogador_dois_posicoes = [False] * 9
        self.tabuleiro_posicoes = [False] * 9
        self.jogador_X = False
        self.jogador_O = False
        self.jogo_ativo = False

    def iniciar(self):
        self.jogador_X = True
        self.jogo_ativo = True

    def terminar_jogo(self):
        self.jogo_ativo = False

    def trocar_jogador(self):
        if self.jogador_X:
            self.jogador_X = False
            self.jogador_O = True
        else:
            self.jogador_X = True
            self.jogador_O = False

    def get_status(self):
        return self.jogo_ativo

    def mostrar_tabuleiro(self):
        print('_' * 2 + '|' + '_' * 2 + '|' + '_' * 2 + '\n' + '_' * 2 + '|' + '_' * 2 + '|' + '_' * 2 + '\n' + ' ' * 2 + '|' + ' ' * 2 + '|' + ' ' * 2)

    def selecionar_jogador(self, numero_do_jogador):
        if numero_do_jogador == 1:
            self.jogador_X = True
        else:
            self.jogador_O = True

    def verificar_posicao_livre(self, posicao):
        return self.tabuleiro_posicoes[posicao] is False

    def selecionar_posicao(self, posicao):
        if self.jogador_X:
            self.jogador_um_posicoes[posicao] = True
        else:
            self.jogador_dois_posicoes[posicao] = True
        self.tabuleiro_posicoes[posicao] = True

    def verificar_uma_possibilidade_de_vitoria(self, posicoes_no_tabuleiro_para_vitoria):
        return all(self.jogador_um_posicoes[posicao] for posicao in posicoes_no_tabuleiro_para_vitoria) \
               or all(self.jogador_dois_posicoes[posicao] for posicao in posicoes_no_tabuleiro_para_vitoria)

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

    def verificar_se_deu_velha(self):
        return not False in self.tabuleiro_posicoes

    def nao_esta_na_primeira_jogada(self):
        return True in self.tabuleiro_posicoes

class JogoDaVelhaTerminal(JogoDaVelha):
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
        while self.get_status():
            self.continuar_jogo()
            self.jogo_terminou()

    def continuar_jogo(self):
        if self.nao_esta_na_primeira_jogada():
            self.trocar_jogador()
        self.escolher_jogada()

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
        if self.jogador_X:
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
            return True
        self.posicao_esta_livre = False
        raise ValueError()

    def selecionar_jogada(self):
        self.selecionar_posicao(self.jogada)
        self.marcar_tabuleiro_visual(self.jogada)

    def marcar_tabuleiro_visual(self, posicao):
        if self.jogador_X:
            self.tabuleiro_visual[posicao] = 'X'
        else:
            self.tabuleiro_visual[posicao] = 'O'

    def jogo_terminou(self):
        if self.ver_se_ganhou() or self.ver_se_deu_velha():
            self.terminar_jogo()
            return True

    def ver_se_ganhou(self):
        if self.verificar_todas_possibilidades_de_vitoria():
            if self.jogador_X:
                print('Jogador um ganhou!')
            else:
                print('Jogador dois ganhou!')
            return True
        else:
            return False

    def ver_se_deu_velha(self):
        if self.verificar_se_deu_velha():
            print('O jogo deu velha!')
            return True


def jogoDaVelha():
    primeiro_jogo = JogoDaVelhaTerminal()
    primeiro_jogo.jogar()















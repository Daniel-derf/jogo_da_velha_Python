import unittest
import hashGame
from unittest.mock import patch


class SupportMethods():
    def __init__(self):
        self.jogoDaVelhaTerminal = hashGame.JogoDaVelhaTerminal()

    def fazerDarVelha(self):
        self.jogoDaVelhaTerminal.iniciar()
        for i in [0, 2, 5, 6, 7]:
            self.jogoDaVelhaTerminal.selecionar_posicao(i)
        self.jogoDaVelhaTerminal.trocar_jogador()
        for i in [1, 3, 4, 8]:
            self.jogoDaVelhaTerminal.selecionar_posicao(i)

    def fazerJogadorXGanhar(self):
        self.jogoDaVelhaTerminal.iniciar()
        for i in [0,1,2]:
            self.jogoDaVelhaTerminal.selecionar_posicao(i)

    def fazerJogadorOGanhar(self):
        for i in [0,1,2]:
            self.jogoDaVelhaTerminal.selecionar_posicao(i)

class TestJogoDaVelhaTerminal(unittest.TestCase, SupportMethods):
    def setUp(self):
        self.jogoDaVelhaTerminal = hashGame.JogoDaVelhaTerminal()

    def test_ver_se_deu_velha(self):
        self.fazerDarVelha()
        self.assertTrue(self.jogoDaVelhaTerminal.ver_se_deu_velha())
        self.jogoDaVelhaTerminal.limpar_tabuleiro()
        self.assertFalse(self.jogoDaVelhaTerminal.ver_se_deu_velha())

    def test_ver_se_ganhou(self):
        self.fazerJogadorXGanhar()
        self.assertTrue(self.jogoDaVelhaTerminal.ver_se_ganhou())
        self.jogoDaVelhaTerminal.limpar_tabuleiro()
        self.assertFalse(self.jogoDaVelhaTerminal.ver_se_ganhou())
        self.fazerJogadorOGanhar()
        self.assertTrue(self.jogoDaVelhaTerminal.ver_se_ganhou())

    def test_jogo_terminou(self):
        self.fazerDarVelha()
        self.assertTrue(self.jogoDaVelhaTerminal.jogo_terminou())
        self.jogoDaVelhaTerminal.limpar_tabuleiro()
        self.assertFalse(self.jogoDaVelhaTerminal.jogo_terminou())
        self.fazerJogadorXGanhar()
        self.assertTrue(self.jogoDaVelhaTerminal.jogo_terminou())

    def test_marcar_tabuleiro_visual(self):
        self.jogoDaVelhaTerminal.iniciar()
        self.jogoDaVelhaTerminal.marcar_tabuleiro_visual(0)
        self.assertTrue(self.jogoDaVelhaTerminal.tabuleiro_visual[0] == 'X')
        self.jogoDaVelhaTerminal.trocar_jogador()
        self.jogoDaVelhaTerminal.marcar_tabuleiro_visual(1)
        self.assertTrue(self.jogoDaVelhaTerminal.tabuleiro_visual[1] == 'O')

    def test_validar_valor_ja_selecionado(self):
        self.jogoDaVelhaTerminal.jogada = 0
        self.assertTrue(self.jogoDaVelhaTerminal.validar_valor_ja_selecionado())
        self.jogoDaVelhaTerminal.selecionar_jogada()
        with self.assertRaises(ValueError):
            self.jogoDaVelhaTerminal.validar_valor_ja_selecionado()

    def test_validar_valor_entre_opcoes_possiveis(self):
        self.jogoDaVelhaTerminal.jogada = 0
        self.assertTrue(self.jogoDaVelhaTerminal.validar_valor_entre_opcoes_possiveis())
        self.jogoDaVelhaTerminal.jogada = 10
        with self.assertRaises(ValueError):
            self.jogoDaVelhaTerminal.validar_valor_entre_opcoes_possiveis()

    def test_exibir_jogador_da_vez(self):
        self.jogoDaVelhaTerminal.iniciar()

        with patch('builtins.print') as mock_print:
            self.jogoDaVelhaTerminal.exibir_jogador_da_vez()
            mock_print.assert_called_with("Jogador UM")
        self.jogoDaVelhaTerminal.trocar_jogador()

        with patch('builtins.print') as mock_print:
            self.jogoDaVelhaTerminal.exibir_jogador_da_vez()
            mock_print.assert_called_with("Jogador DOIS")

    @patch('builtins.input', side_effect=['5'])
    def test_pedir_jogada_e_validar(self):
        self.assertTrue(self.jogoDaVelhaTerminal.pedir_jogada_e_validar())



if __name__ == '__main__':
    unittest.main()

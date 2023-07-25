import unittest
import hashGame

class TestJogoDaVelha(unittest.TestCase):
    def setUp(self):
        self.jogoDaVelha = hashGame.JogoDaVelha()

    def test_iniciar(self):
        self.jogoDaVelha.iniciar()
        self.assertTrue(self.jogoDaVelha.jogador_X)
        self.assertTrue(self.jogoDaVelha.jogo_ativo)

    def test_terminar_jogo(self):
        self.jogoDaVelha.terminar_jogo()
        self.assertFalse(self.jogoDaVelha.jogo_ativo)

    def test_trocar_jogador(self):
        self.jogoDaVelha.iniciar()
        self.jogoDaVelha.trocar_jogador()
        self.assertFalse(self.jogoDaVelha.jogador_X)
        self.assertTrue(self.jogoDaVelha.jogador_O)

    def test_get_status(self):
        self.assertEqual(self.jogoDaVelha.get_status(), self.jogoDaVelha.jogo_ativo)

    def test_selecionar_jogador_X(self):
        self.jogoDaVelha.selecionar_jogador(1)
        self.assertTrue(self.jogoDaVelha.jogador_X)
        self.assertFalse(self.jogoDaVelha.jogador_O)

    def test_selecionar_jogador_O(self):
        self.jogoDaVelha.selecionar_jogador(2)
        self.assertFalse(self.jogoDaVelha.jogador_X)
        self.assertTrue(self.jogoDaVelha.jogador_O)

    def test_verificar_posicao_livre(self):
        self.jogoDaVelha.tabuleiro_posicoes[0] = True
        self.assertFalse(self.jogoDaVelha.verificar_posicao_livre(0))
        self.assertTrue(self.jogoDaVelha.verificar_posicao_livre(1))

    def test_selecionar_posicao(self):
        self.jogoDaVelha.iniciar()
        self.jogoDaVelha.selecionar_posicao(1)
        self.assertTrue(self.jogoDaVelha.tabuleiro_posicoes[1])
        self.assertTrue(self.jogoDaVelha.jogador_um_posicoes[1])
        self.assertFalse(self.jogoDaVelha.jogador_dois_posicoes[1])

    def test_verificar_uma_possibilidade_de_vitoria(self):
        self.jogoDaVelha.iniciar()
        self.jogoDaVelha.selecionar_posicao(0)
        self.jogoDaVelha.selecionar_posicao(1)
        self.jogoDaVelha.selecionar_posicao(2)
        self.assertTrue(self.jogoDaVelha.verificar_uma_possibilidade_de_vitoria([0,1,2]))

    def test_verificar_todas_possibilidades_de_vitoria(self):
        self.jogoDaVelha.iniciar()
        self.jogoDaVelha.selecionar_posicao(6)
        self.jogoDaVelha.selecionar_posicao(7)
        self.jogoDaVelha.selecionar_posicao(8)
        self.assertTrue(self.jogoDaVelha.verificar_todas_possibilidades_de_vitoria())
        self.jogoDaVelha.limpar_tabuleiro()
        self.jogoDaVelha.selecionar_posicao(2)
        self.jogoDaVelha.selecionar_posicao(5)
        self.jogoDaVelha.selecionar_posicao(1)
        self.assertFalse(self.jogoDaVelha.verificar_todas_possibilidades_de_vitoria())

    def test_limpar_tabuleiro(self):
        self.jogoDaVelha.selecionar_posicao(1)
        self.jogoDaVelha.limpar_tabuleiro()
        self.assertFalse(self.jogoDaVelha.tabuleiro_posicoes[1])

    def test_verificar_se_deu_velha(self):
        for i in range(9):
            self.jogoDaVelha.selecionar_posicao(i)
        self.assertTrue(self.jogoDaVelha.verificar_se_deu_velha())
        self.jogoDaVelha.limpar_tabuleiro()
        self.assertFalse(self.jogoDaVelha.verificar_se_deu_velha())

    def test_nao_esta_na_primeira_jogada(self):
        self.jogoDaVelha.selecionar_posicao(1)
        self.assertTrue(self.jogoDaVelha.nao_esta_na_primeira_jogada())
        self.jogoDaVelha.limpar_tabuleiro()
        self.assertFalse(self.jogoDaVelha.nao_esta_na_primeira_jogada())



if __name__ == '__main__':
    unittest.main()

class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, remetente, assunto, corpo):
        for user in self.sessao.listar():
            self.enviador.enviar(
                remetente,
                user.email,
                assunto,
                corpo
            )

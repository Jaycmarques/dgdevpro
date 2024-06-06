class Enviador:
    def __init__(self):
        self.qde_email_enviados = 0

    def enviar(self, remetente, enviador, assunto, corpo):
        if '@' not in remetente:
            raise EmailNotValid(f'Receiver e-mail not valid: {remetente}')
        self.qde_email_enviados += 1
        return remetente


class EmailNotValid(Exception):
    pass

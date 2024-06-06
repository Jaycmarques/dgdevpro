class Enviador:
    def enviar(self, remetente, enviador, assunto, corpo):
        if '@' not in remetente:
            raise EmailNotValid(f'Receiver e-mail not valid: {remetente}')
        return remetente


class EmailNotValid(Exception):
    pass

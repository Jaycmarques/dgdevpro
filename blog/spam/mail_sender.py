class Sender:
    def send(self, receiver, sender, subject, body):
        if '@' not in receiver:
            raise EmailNotValid(f'Receiver e-mail not valid: {receiver}')
        return receiver


class EmailNotValid(Exception):
    pass

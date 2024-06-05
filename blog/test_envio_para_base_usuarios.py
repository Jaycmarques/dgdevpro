from blog.spam.mail_sender import Sender
from blog.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Sender())
    enviador_de_spam.enviar_emails('julio@gmail.com', 'Assunto', 'corpo')

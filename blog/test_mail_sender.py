from blog.spam.mail_sender import Sender


def test_send_mail():
    sender = Sender()
    assert sender is not None

def test_receiver():
    sender = Sender()
    sender.send('julio.jcmarques@gmail.com', 'julionihongo@gmail.com', 'criação enviar email', 'aprendendo a criar testes de spam')



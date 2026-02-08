#importação.
from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email, password, secret_key
from datetime import date


#contrução.
app = Flask(__name__)
app.secret_key = secret_key

#controle de e-mail.
mail_settings = {
    "MAIL_SERVER": "smtp-mail.outlook.com", 
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": password
}

app.config.update(mail_settings)
mail = Mail(app)

#class contato estrutura de envio.
class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem


#construção html.
@app.route("/")
def index():
    nascimento = date(2000, 1, 16)
    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return render_template('index.html', idade=idade)


#guia host/port or email.
@app.route('/send', methods=["GET", "POST"])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message(
            subject= f'{formContato.nome} te enviou uma mensagem no Portifólio',
            sender= app.config.get("MAIL_USERNAME"),
            recipients= ['danyelsan.silva@outlook.com', app.config.get("MAIL_USERNAME")],
            body= f'''

            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:

            {formContato.mensagem}
            
            '''
        )
        mail.send(msg)
        flash('Mensagem enviada com sucesso.')
    return redirect("/")

#execução.
if __name__ == '__main__':
    app.run(debug=True)
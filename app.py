#importação.
from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email, password


#contrução.
app = Flask(__name__)
app.secret_key = 'danielsilva'

#controle de e-mail.
mail_settings = {
    "MAIL_SERVER": "smtp.gmail.com", 
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
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
    return render_template('index.html')


#guia host/port or email.
@app.route('/send', methods=["GET", "POST'"])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message(
            subject= f'{formContato.nome} te enviou uma mensagem no Portifólio',
            sender= app.config.get("MAIL_USERMANE"),
            recipients= ['danyelsan.silva@gmail.com', app.config.get("MAIL_USERMANE")],
            body= f'''

            {formContato.nome} com o e-mail {formContato.email}, te enivou a seguinte mensagem:

            {formContato.mensagem}
            
            '''
        )
        mail.send(msg)
        flash('Mensagem enviada com sucesso.')
    return redirect("/")

#execução.
if __name__ == '__main__':
    app.run(debug=True)
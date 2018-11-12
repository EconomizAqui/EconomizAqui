Data | Versão | Descrição | Responsáveis
-- | -- | -- | --
31/10/2018 | 1.0 | Adição de seção de Introdução e seção sobre GOF Observer | Amanda Bezerra

# GOF

## Introdução
<p align="justify">
Padrões de projeto são descrições ou modelos de como resolver um problema que podem ser usados em diversas situações.
</p>

<p align="justify">
Os padrões GOF (<i>Gang of Four</i>) são soluções reutilizáveis de software orientado a objetos que são divididos em três categorias: de Criação, Estrutural e Comportamental.
</p>

<p align="justify">
Este documento detalha os padrões GOF utilizados no projeto EconomizAqui.
</p>

## Observer
<p align="justify">
É um padrão GOF comportamental que tem como objetivo definir um mecanismo eficiente para reagir às alterações realizadas em certos objetos, permitindo que objetos interessados possam ser avisados sobre a mudança de estado ou um evento, para que possam ser atualizados.
</p>

### Estrutura genérica
![](https://sourcemaking.com/files/v2/content/patterns/Observer.png)

### Utilização no projeto EconomizAqui
<p align="justify">
O projeto utiliza um módulo que notifica um usuário por e-mail sempre que um login em sua conta for detectado.
</p>

<p align="justify">
Para que o módulo de envio de e-mail seja notificado de forma eficiente quando um login em uma conta de usuário for realizado, optou-se pela utilização do padrão <i>Observer</i>. Dada as peculiaridades da linguaguem Python, bem como certas limitações em relação à utilização do framework Django e sua arquitetura MTV, algumas adaptações na solução proposta pelo Observer tiveram que ser feitas.
</p>

#### Modelagem
![](https://lh3.googleusercontent.com/vEbxYknJcjulku7HAtu3LmBRQCcYLl84ydewwNfo2vh2Bv2tArY-P-vvUZwMQHmDm244sroYMciqKNeCNUBokMC3zHksJt7X81MnAfUol8P6avdUYTFRoNj9cAgGvogFv57V3b5f)

#### Implementação

Um manipulador de evento é adicionado a um <i>user</i>.
```Python
def attach(self, event_handler):
    if event_handler not in self.event_handlers:
        self.event_handlers.append(event_handler)
```

O recurso de [sinais do Django](https://docs.djangoproject.com/en/2.1/topics/signals/) captura a ação de logar de um usuário e então permite que o <i>user</i> notifique esse evento para os manipuladores interessados.
```Python
user_logged_in.connect(notify)
```
O <i>user</i> notifica seus interessados e repassa seu estado para que os manipuladores possam ser atualizados.
```python
def notify(user, **kwarg):
    event_handler = NotificationEmailSender()
    user.attach(event_handler)

    for event_handler in user.event_handlers:
        event_handler.update(user)
```

O módulo de envio de e-mail é atualizado e dispara um e-mail para o usuário referente ao <i>user</i> que o alertou.
```Python
class NotificationEmailSender():
    def update(self, user):
        email = user.email

        sent = send_mail(
            'Alerta de login',
            'Registramos um novo login em sua conta no EconomizAqui. '
            + 'Caso não tenha sido você, favor redefinir sua senha.',
            'economizaqui@email.com',
            [email],
        )
```

Para mais detalhes da implementação, acesse o [código](https://github.com/EconomizAqui/EconomizAqui/commit/a7747e8d00846bc6f546dbb48973961871bed460) no repositório.

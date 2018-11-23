Data | Versão | Descrição | Responsáveis
-- | -- | -- | --
31/10/2018 | 1.0 | Adição de seção de Introdução e seção sobre GOF Observer | Amanda Bezerra
19/11/2018 | 2.0 | Adição de seção de seção Referências e seção sobre GOF Strategy  | Amanda Bezerra
21/11/2018 | 2.1 | Implementação do mecanismo de envio de email para o Observer | Eduardo, Mateus de Oliveira e Matheus Roberto
23/11/2018 | 2.2 | Implementação do Padrão State | Eduardo, Mateus de Oliveira, Matheus Roberto e Vinicius Cantuária
23/11/2018 | 2.3 | Adição do Padrão Factory | Eduardo, Mateus de Oliveira e Matheus Roberto
23/11/2018 | 2.4 | Adição do Padrão Facade | Eduardo, Mateus de Oliveira, Matheus Roberto e Vinícius Cantuária


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
class EventHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, user):
        pass

class NotificationEmailSender(EventHandler):
    def update(self, user):
        email = user.email 
        msg = 'Alerta de login.Registramos um novo login em sua conta no EconomizAqui. Caso não tenha sido você, favor redefinir sua senha!'
        self.notify(msg, email)

    def notify(self, texto, email):
        email_to = ['noreplayfiscae@gmail.com']
        subject = 'Login detectado'
        mensagem = MIMEText(texto)
        mensagem.set_charset('utf-8')
        mensagem['Subject'] = subject
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('noreplayfiscae@gmail.com', 'fiscaeunb')
        mail.sendmail('noreplayfiscae@gmail.com', email, mensagem.as_string())
```

Para mais detalhes da implementação, acesse o [código](https://github.com/EconomizAqui/EconomizAqui/commit/a7747e8d00846bc6f546dbb48973961871bed460) no repositório.

## Strategy
<p align="justify">
É um padrão GOF comportamental que tem como objetivo definir uma família de algoritmos que podem variar de forma independente. Este padrão melhora a manutenção do código e ajuda a gerenciar toda complexidade exigida pelas lógicas condicionais.
</p>

### Estrutura genérica
![](https://sourcemaking.com/files/v2/content/patterns/Strategy1.png)

### Utilização no projeto EconomizAqui
<p align="justify">
O projeto possui uma lista de mercados cadastrados que podem ser ordenadas de acordo com alguns critérios, sendo eles: por ordem alfabética (de "A a Z" e de "Z a A") e por avaliação (melhores avaliados e piores avaliados). 
</p>
<p align="justify">
Para ordenar esta lista de mercados podem ser utilizados vários algoritmos, assim, encontrou-se uma oportunidade para aplicar o padrão <i>Strategy</i>, visto que uma família de algoritmos seria definida.
</p>
<p align="justify">
Dada as peculiaridades da linguaguem Python, bem como certas limitações em relação à utilização do framework Django e sua arquitetura MTV, algumas adaptações na solução proposta pelo <i>Strategy</i> tiveram que ser feitas.
</p>

#### Implementação

<p align="justify">Na maioria das linguagens de programação, o padrão Strategy é implementado através da criação de uma interface ou classe abstrata base e a partir desta subclasses são criadas implementações concretas das Strategys, porém, a linguagem Python suporta funções de ordem superior que podem ser utilizadas para simplificar a implementação deste padrão.</p>

<p align="justify">Em Python, funções são tratadas como objetos de primeira classe, permitindo que, por exemplo, uma função possa ter uma ou mais funções como argumentos, permitindo assim que o padrão Strategy seja implementado de modo que uma única classe seja criada e sejam injetadas funções em suas instâncias.</p>

Uma classe contém as implementações das variações de algoritmos como funções:
```Python
class MarketSorter:  
    def __init__(self, func=None):
        self.queryset = list(Market.objects.all())
        if func is not None:
            self.sort = types.MethodType(func, self)
    def sort(self):
        return self.queryset
    def sort_by_name_ascending(self):
        return Market.objects.order_by('name')
    # ...
    def sort_by_rating_descending(self):
        return Market.objects.filter(ratings__isnull=False).order_by('ratings__average')
```

<p align="justify">Um <i>form</i> do Django é responsável por capturar a opção desejada pelo usuário, que representa o critério a partir do qual ele quer que a lista de mercados seja ordenada. De acordo com a opção, um dos algoritmos da classe <i>MarketSorter</i> é escolhido e então a função <i>sort()</i> é chamada para ordenar a lista de acordo com o algoritmo escolhido.</p>

```Python
if form.is_valid():
    choice = form.cleaned_data['choice']
    if choice == 'nomeAz':
        sorter = MarketSorter(MarketSorter.sort_by_name_ascending)
    elif choice == 'nomeZa':
        sorter = MarketSorter(MarketSorter.sort_by_name_descending)
    elif choice == 'avaliacaoMelhores':
        sorter = MarketSorter(MarketSorter.sort_by_rating_ascending)
    elif choice == 'avaliacaoPiores':
        sorter = MarketSorter(MarketSorter.sort_by_rating_descending)
    markets = sorter.sort()
```

Para mais detalhes da implementação, acesse o [código](https://github.com/EconomizAqui/EconomizAqui/commit/284dadc78abfcebefbc5413efc870fb3d5721a28) no repositório.

## State
<p align="justify">
É um padrão GOF comportamental que permite um objeto modificar seu comportamento quando seu estado interno vária.</p>

### Estrutura genérica
![](https://sourcemaking.com/files/v2/content/patterns/State1.png)

### Utilização no projeto EconomizAqui
<p align="justify">
O projeto possui diversos produtos nos quais usuários podem informar o preço, para garantir que o preço realmente é válido, os usuários tem a opção de confirmar o preço ou declara-lo incorreto, o preço possui um atributo de pontos de confiabilidade, que aumenta ou diminui de acordo com esta opção do usuário. 
</p>
<p align="justify">Para garantir esta confiabilidade, encontrou-se uma oportunidade para aplicar o padrão <i>State</i>, No qual o produto receberia um selo de verificado caso este atributo de pontos estivesse em uma determinada categoria.
</p>

#### Implementação

<p align="justify">Na classe Historic foi adicionado um campo para guardar seus pontos</p>

```Python
class Historic (models.Model):
    price = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    commerce = models.ForeignKey('markets.Market', models.DO_NOTHING)
    points = models.IntegerField(default=0)
    def _self_(self):
        return self.price
```

<p align="justify">A classe <i>View</i> de Produtos é responsável pela realização das operações, que no caso seria o pegar os pontos e adicionar ou subtrair do banco de dados, para assim realizar as decisões posteriores.</p>

```Python
def view(request, id):
    product = Product.objects.get(id=id)
    historic_price = []
    historic_commerce = []
    if request.POST:
        historic = product.historic.last()
        historic.points += int(request.POST['points'])
        historic.save()

    point = False
    for historic in product.historic.all():
        price = json.dumps(historic.price)
        historic_price.append(price)
        historic_commerce.append(historic.commerce.name)

    historic_price = json.dumps(historic_price)
    historic_commerce = json.dumps(historic_commerce)

    return render(request, 'product.html', {"product": product, "historic_price": historic_price, "historic_commerce": historic_commerce})
```

<p align="justify">No Template de Produtos o método é chamado através do JS, para assim ser utilizado no HTML após o usuário realizar uma ação de clique no botão, para somar ou subtrair. No HTML também é realizado a decisão se o selo de verificado irá aparecer ou não dependendo da quantidade de pontos daquele determinado produto.</p>

```JS
function AumentaPontos(valor){
  var opt= document.getElementById('option_points');
  opt.value = valor
  document.getElementById("pointForm").submit();
}
HTML
{% if product.historic.last.points > 9 %}
    <span class="fa-stack fa-2x">
      <i class="fa fa-certificate fa-stack-2x" style="color:blue"></i>
      <i class="fa fa-check fa-stack-1x" style="color:#247BA0"></i>
    </span>
    {% endif %}
```

Para mais detalhes da implementação, acesse o [código](https://github.com/EconomizAqui/EconomizAqui/commit/7516a9c0010144edb065b5311b2cb764a98042e4) no repositório.

## Factory
<p align="justify">
É um padrão GOF criacional que define uma interface para criar um objeto, mas deixa que as subclasses decidam quais classes instanciar.</p>

### Estrutura genérica
![](https://sourcemaking.com/files/v2/content/patterns/Factory_Method.png)

### Utilização no projeto EconomizAqui
<p align="justify">
O projeto é desenvolvido utilizando o <i>Framework</i> Django da linguagem Python, e o mesmo possui um módulo de Forms no qual é responsável por definir os campos necessários para que seja construido um objeto
</p>

#### Implementação

<p align="justify">O modulo <i>Forms</i> de Produtos é responsável por definir os campos de entrada de dado de um usuário, ou seja os atributo necessários para a instanciação de um determinado objeto</p>

```Python
class HistoricForm (forms.ModelForm):
    price = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o preço do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Preço',
            }
        )
    )
    cod_commerce = forms.ChoiceField()
```

<p align="justify">A classe meta define qual a model que sera utilizada na construção do formulario, e os fields definem os campos necessários para a construção de um objeto deste tipo.</p>

```Python
    class Meta:
        model = Historic
        fields = ('price', 'cod_commerce')
```}
```

Para mais detalhes da implementação, acesse o [código](https://github.com/EconomizAqui/EconomizAqui/blob/development/products/forms.py) no repositório.

## Facade
Prover uma interface simplificada para a utilização de várias interfaces de um subsistema.

### Estrutura genérica
![](https://sourcemaking.com/files/v2/content/patterns/Facade1.png)

### Utilização no projeto EconomizAqui
Essa estrutura já é implementada no django com o arquivo urls.py, onde é feito todo o gerenciamento de rotas da aplicação. No django existem vários apps, no qual cada um tem a sua própria url, e o arquivo urls.py nada mais é do que uma fachada que gerencia outras fachadas.

#### Implementação

```
#economizaqui urls.py

"""economizaqui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('', include('users.urls')),
    path('', include('django.contrib.auth.urls')),
    path('markets/', include('markets.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]


#product urls.py
from django.urls import path
from django.urls import include
from products import views
urlpatterns = [
    path('', views.list_products ,name='listProducts'),
    path('new', views.create_product ,name='createProduct'),
    path('view/<int:id>/', views.view ,name='viewProduct'),
    path('update/<int:id>/', views.update_product ,name='updateProduct'),
    path('delete/<int:id>/', views.delete_product ,name='deleteProduct'),
    path('addPrice/<int:id>/', views.new_price ,name='newPrice'),
]

#market urls.py
from django.urls import path

from markets import views

urlpatterns = [
    path('', views.market_list, name='market_list'),
    path('view/<int:pk>', views.market_view, name='market_view'),
    path('new', views.market_create, name='market_new'),
    path('edit/<int:pk>', views.market_update, name='market_edit'),
    path('delete/<int:pk>', views.market_delete, name='market_delete'),
]
```


## Referências
+ [Observer Design Pattern](https://sourcemaking.com/design_patterns/observer)
+ [Abstract Base Classes in Python](http://blog.thedigitalcatonline.com/blog/2016/04/03/abstract-base-classes-in-python/)
+ [Strategy Design Pattern](https://sourcemaking.com/design_patterns/strategy)
+ [Strategy Design Pattern](https://sourcemaking.com/design_patterns/state)
+ [Python Higher Order Functions](https://www.hackerearth.com/pt-br/practice/python/functional-programming/higher-order-functions-and-decorators/tutorial/)
+ [Python Patterns](https://github.com/faif/python-patterns)
Para mais detalhes da implementação, acesse o [código](https://github.com/EconomizAqui/EconomizAqui/blob/development/users/services.py) no repositório.

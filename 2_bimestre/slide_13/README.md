# Exercício
Identifique no Projeto do Grupo situações onde os princípios SOLID poderiam ser (ou foram) aplicados.

# Projeto
O Projeto do grupo se encontra no link "https://github.com/EricToshio/Rede_Portal".
O objetivo do projeto é a criação de um site para o H8, ele foi realizado utilizando a framework  Django.

# Princípios SOLID

## Single responsability
Todos os models do projeto estão de acordo com o princípio "single responsability". Isso porque cada um dele tem uma clara e única função, que é descrever uma table específica para o banco de dados.

Abaixo segue o model que descreve a table de reserva da sala: 
```python
class ReservationRede(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=5)
    details = models.CharField(max_length=200)
    reservation_date = models.DateTimeField()
    status = models.CharField(default="pendente", max_length=20)
```

## Open Closed Design
Várias classes do projeto seguem o princípio "open closed design". Por exemplo tem-se a classe IssueForm, o qual descreve as características do formulário de reclamação de problemas no H8. Esse classe é facilmente utilizada para a criação de forms nas views, porém difícil de modifica-lo.
```python
class IssueForm(forms.Form):
    name = forms.CharField(label='Seu nome', initial='',max_length=50)
    localization = forms.CharField(label='AP/vaga (ex.: 315/F)', initial='', max_length=5)
    iniciativa = forms.ChoiceField(label='iniciativa (ex.: RedeCasd)', choices= (('RedeCasd','RedeCasd'),('DOO','DOO'),('Casd','Casd')))
    description = forms.CharField(label='Descrição do problema', initial='',max_length=200)
```
    
## Liskov Substitution
Como a framework Django tem como objetivo o desenvolvimento rápido de aplicações, ela tenta facilitar ao máximo o trabalho do programador. Uma das principais fazer isso é por meio de várias super classes, o qual devem ter posterior adição de funcionalidades. 
No caso do exemplo abaixo, a subclasse "Migration" recebe a superclasse "migrations.Migration" aonde foram adicionadas novas funcionalidades por meio da adição da lista "operations".
```python
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('iniciativa_name', models.CharField(max_length=100)),
            ],
        ),
    ]
```

## Interface Segregation
Como já dito anteriormente, um dos objetivos da framework Django é o desenvolvimento rápido de aplicações. E uma das formas de fazer isso é reduzir ao máximo o desenvolvimento das interfaces e suas relações. Por isso, não houve quase nenhuma implementação direta de toda uma interface.
No entanto, o princípio de "interface segregation" poderia ser utilizado numa classe "Server_Helper", a qual ajudaria obter dados da situação da internet no H8. Nessa classe poderia ter sido utilizado a interfaces de leitura e obtenção de dados específicos do "json" gerado no servidor. 
```python
def redecasd_status():
    with open('redecasd_info.json') as f:
        data = json.load(f)
    return data
```  

## Dependency Injection
Este princípio tem como base a ideia de que detalhes devem ser implementados sobre abstrações. No exemplo abaixo a classe News (detalhe) é implementado sobre a classe abstrata (models.Model). 
```python
class News(models.Model):
    title = models.TextField(validators=[MaxLengthValidator(30)], default = 'Title')
    sub_title = models.TextField(validators=[MaxLengthValidator(50)], default = 'Sub-titulo')
    iniciativa_name = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', default = timezone.now())
    pic = models.ImageField(upload_to = get_image_path, default = 'home/static/home/images/casd.png')
    
    def pic_url(self):
        return self.pic.url[4:]
```
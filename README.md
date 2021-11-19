# e-diary-hack
Скрипт для исправления оценок, удаления замечаний и создания похвал в базе данных школьного сайта при наличи доступа к серверу. Данный проект является учебным и создан в рамках курса Devman.

# Подготовка к использованию
Для начала вам необходимо получить доступ к серверу школьного сайта.
<details>
  <summary>А если я хочу протестировать скрипт в своих целях или доработать его?</summary>
Разверните локальную копию сайта школы по инструкции в <a href=https://github.com/devmanorg/e-diary/tree/master>репозитории</a>.

Не забудьте наполнить пустую базу данных - для корректной работы понадобятся данные.
</details>
<details>
  <summary>У меня есть доступ к школьному серверу, но меня встречает недружелюбная черная консоль</summary>
  Вам понадобится базовое знание команд Linux, можете поискать любой гайд или использовать, например, <a href="https://selectel.ru/blog/basic-linux-commands/">этот</a>.
</details>

После того как вы убедились, что у вас есть доступ к серверу, то скачайте скрипт. Наиболее удобный способ это сделать - использовать git.

Чтобы скачать скрипт с помощью git, в любом удобном месте (но, желательно, не в папке с сайтом) на сервере исполните:
```bash
$ git clone https://github.com/valeriy131100/e-diary-hack
```

После этого в текущей директории будет создана папка e-diary-hack. Скопируйте из нее файл scripts.py и поместите в папку школьного сайта, рядом с файлом manage.py.

# Использование
После того, как вы успешно скачали скрипт и поместили его в папку школьного сайта, вам понадобится открыть Django-shell. 

Для этого, находясь в папке школьного сайта исполните:
```bash
$ bin/python manage.py shell
```

Если вы все сделаете верно, то последней строчкой в терминале будет:
```text
(InteractiveConsole)
```

Теперь осталось лишь запустить скрипт:
```python
import scripts
```

Далее вас встретит дружелюбный интерфейс, который спросит ваше имя и название урока, для которого необходимо создать похвалу. Скрипт сообщит об ошибках ввода и попросит их исправить. В случае успешного исполнения скрипта вы увидите нечто подобное:
```text
Оценки Фролов Иван Григорьевич 6А исправлены
Замечания Фролов Иван Григорьевич 6А удалены
Создана похвала по предмету Биология 6А
```

Не забудьте избавиться от следов своего присутствия на сервере - удалить папку со скриптом, а также его копию в папке сайта.
1. Ajout de ``admin.site.register(Choice)`` dans admin 
2. .
3. .
    - Non
    - Non
    - Non
    - Non
4. Classes rajoutés dans admin
5. Impossible de se connecter
6. Connection possible
7. Connexion impossible


# Exo shell
1. ``>>[print(x,x.__dict__) for x in Question.objects.filter()]    
What's up? {'_state': <django.db.models.base.ModelState object at 0x00000237D5614DA0>, 'id': 1, 'question_text': "What's up?", 'pub_date': datetime.datetime(2024, 10, 7, 12, 27, 32, 87107, tzinfo=datetime.timezone.utc)}
A {'_state': <django.db.models.base.ModelState object at 0x00000237D5614E30>, 'id': 2, 'question_text': 'A', 'pub_date': datetime.datetime(2024, 10, 8, 8, 37, 19, tzinfo=datetime.timezone.utc)}
B {'_state': <django.db.models.base.ModelState object at 0x00000237D56150D0>, 'id': 3, 'question_text': 'B', 'pub_date': datetime.datetime(2024, 10, 9, 8, 37, 31, tzinfo=datetime.timezone.utc)}
C {'_state': <django.db.models.base.ModelState object at 0x00000237D5614E60>, 'id': 4, 'question_text': 'C', 'pub_date': datetime.datetime(2024, 10, 15, 8, 38, 9, tzinfo=datetime.timezone.utc)}
E {'_state': <django.db.models.base.ModelState object at 0x00000237D5614EF0>, 'id': 5, 'question_text': 'E', 'pub_date': datetime.datetime(2024, 10, 8, 8, 38, 18, tzinfo=datetime.timezone.utc)}
F {'_state': <django.db.models.base.ModelState object at 0x00000237D5614500>, 'id': 6, 'question_text': 'F', 'pub_date': datetime.datetime(2024, 10, 1, 8, 38, 26, tzinfo=datetime.timezone.utc)}
[None, None, None, None, None, None]
``
2. ``>>> [print(x,x.__dict__) for x in Question.objects.filter(pub_date__day=15)]  
C {'_state': <django.db.models.base.ModelState object at 0x00000237D5614C80>, 'id': 4, 'question_text': 'C', 'pub_date': datetime.datetime(2024, 10, 15, 8, 38, 9, tzinfo=datetime.timezone.utc)}
[None]
``
3. 
```
>>> [print(x,x.__dict__) for x in Question.objects.filter(pub_date__day=15)] 
C {'_state': <django.db.models.base.ModelState object at 0x00000237D56148F0>, 'id': 4, 'question_text': 'C', 'pub_date': datetime.datetime(2024, 10, 15, 8, 38, 9, tzinfo=datetime.timezone.utc)} [None]
>>> [print(x,x.__dict__) for x in Choice.objects.filter(question_id=2)]       
A1 {'_state': <django.db.models.base.ModelState object at 0x00000237D56150D0>, 'id': 4, 'question_id': 2, 'choice_text': 'A1', 'votes': 0}
A2 {'_state': <django.db.models.base.ModelState object at 0x00000237D56150A0>, 'id': 5, 'question_id': 2, 'choice_text': 'A2', 'votes': 0}
A3 {'_state': <django.db.models.base.ModelState object at 0x00000237D56151F0>, 'id': 6, 'question_id': 2, 'choice_text': 'A3', 'votes': 0}
[None, None, None]
```
4. 
```
>>> for i in Question.objects.filter():                                
...     print(i,i.__dict__)                                                                                                      
...     [print("",v) for v in Choice.objects.filter(question_id=i.id)]
...
What's up? {'_state': <django.db.models.base.ModelState object at 0x00000237D56151F0>, 'id': 1, 'question_text': "What's up?", 'pub_date': datetime.datetime(2024, 10, 7, 12, 27, 32, 87107, tzinfo=datetime.timezone.utc)}
 Not much
 The sky
[None, None]
A {'_state': <django.db.models.base.ModelState object at 0x00000237D56152B0>, 'id': 2, 'question_text': 'A', 'pub_date': datetime.datetime(2024, 10, 8, 8, 37, 19, tzinfo=datetime.timezone.utc)}
 A1
 A2
 A3
[None, None, None]
B {'_state': <django.db.models.base.ModelState object at 0x00000237D56153A0>, 'id': 3, 'question_text': 'B', 'pub_date': datetime.datetime(2024, 10, 9, 8, 37, 31, tzinfo=datetime.timezone.utc)}
 B1
 B2
 B2
[None, None, None]
C {'_state': <django.db.models.base.ModelState object at 0x00000237D5614FE0>, 'id': 4, 'question_text': 'C', 'pub_date': datetime.datetime(2024, 10, 15, 8, 38, 9, tzinfo=datetime.timezone.utc)}
 C1
 C3
[None, None]
E {'_state': <django.db.models.base.ModelState object at 0x00000237D56150D0>, 'id': 5, 'question_text': 'E', 'pub_date': datetime.datetime(2024, 10, 8, 8, 38, 18, tzinfo=datetime.timezone.utc)}
 E1
 E2
 E3
[None, None, None]
F {'_state': <django.db.models.base.ModelState object at 0x00000237D56156D0>, 'id': 6, 'question_text': 'F', 'pub_date': datetime.datetime(2024, 10, 1, 8, 38, 26, tzinfo=datetime.timezone.utc)}
 F1
 F2
 F3
[None, None, None]

```
5. 
```
>>> [print(v,Choice.objects.filter(question_id=v.id).count()) for v in Question.objects.filter()]                                
What's up? 2
A 3
B 3
C 2
E 3
F 3
```
6. .
7. 
```
Question.objects.filter().order_by("-pub_date")
```
8. .
9. ```Question("Question","2024-10-23").save()```
10. ```
    Choice(None,11,"Bleu",0).save() 
    Choice(None,11,"Violet",0).save() 
    Choice(None,11,"Jaune",0).save() 
    ```
11. 
```
>>> Question.objects.filter(pub_date__gt="2024-10-11")
C:\Users\aupetit-gautierm\PycharmProjects\app_django\.venv\Lib\site-packages\django\db\models\fields\__init__.py:1595: RuntimeWarning: DateTimeField Question.pub_date received a naive datetime (2024-10-11 00:00:00) while time zone support is active.
  warnings.warn(
<QuerySet [<Question: C>, <Question: Question>]>
```
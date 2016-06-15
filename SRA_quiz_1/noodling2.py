>>> from SRA_quiz_1.models import Onemodel
>>> Onemodel.objects.all()
[]
>>> u = Onemodel.objects.all()
>>> u = Onemodel(email="test@email.com", status=0, q1_answer="testq1answer", q2_answer="testq2answer", q3_answer="")
>>> Onemodel.objects.all()
[]
>>> u.save()
>>> Onemodel.objects.all()
[<Onemodel: Onemodel object>]
>>> u = Onemodel(email="second@email.com", status=0, q1_answer="secondone", q2_answer="secondone", q3_answer="")
>>> u.save()
>>> u = Onemodel(email="third@email.com", status=0, q1_answer="thirdone", q2_answer="thirdone", q3_answer="thirdone")
>>> u.save()
>>> Onemodel.objects.all()
[<Onemodel: Onemodel object>, <Onemodel: Onemodel object>, <Onemodel: Onemodel object>]

>>> u = Onemodel.objects.all()
>>> for thing in u:
...     print thing
...
Onemodel object
Onemodel object
Onemodel object
>>> for thing in u:
...     print thing.email
...
test@email.com
second@email.com
third@email.com

>>> for thing in u:
...     if thing.email=="third@email.com":
...             print thing.q3_answer
...
thirdone
>>>
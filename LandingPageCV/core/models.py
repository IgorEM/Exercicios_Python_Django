from django.db import models

# Create your models here.
class Skills(models.Model):
        #validators=[ MaxValueValidator(100), MinValueValidator(1) ]
        nome_skill = models.CharField(
            max_length= 100,
            null= False,
            blank= False,
            default=""
        )
        porcentagem = models.PositiveIntegerField(
            default=100
            #verbose_name= "Porcentagem"
        )

        def __str__(self):
            return f"{self.nome_skill} - {self.porcentagem}%"

        #makemigrations gera as migraçoes e o migrate aplica as migrações no banco de dados

        """
        class Meta:
            table_name = "table_skills"
        """

        """
        None - Nada, null
        blank - ''
        """

        # core_skills
        """
        CREATE TABLE(...)
        """

        """
        
        python manage.py shell
        
        from core.models import Skills
        
        In [5]: python = Skills(nome_skill="Python" , porcentagem=100)
        
        In [6]: python
        Out[6]: <Skills: Skills object (None)>
        
        In [7]: python.save()
        
        In [8]: python
        Out[8]: <Skills: Skills object (1)>
        
        In [9]: Skills.objects.count()
        Out[9]: 1
        
        In [10]: javascript = Skills.objects.create(nome_skill="JavaScript", porcentagem=80)
        
        In [11]: javascript
        Out[11]: <Skills: Skills object (2)>
        
        In [4]: todos = Skills.objects.all()

        In [5]: todos
        Out[5]: <QuerySet [<Skills: Python - 100%>, <Skills: JavaScript - 80%>, <Skills: HTML - 60%>, <Skills: CSS - 60%>]>


        """
from django.db import models

# Create your models here.



class Paciente(models.Model):
  nome = question_text = models.CharField('Nome do Paciente',max_length=200)
  codigo_TMO = question_text = models.CharField('Cod. Ficha Hemocentro',max_length=200,unique=True,blank=False,null=False)
  pre_tmo_list = models.ManyToManyField('PreTMO')
  pos_tmo_list = models.ManyToManyField('PosTMO')
  research_form_list = models.ManyToManyField('ResearchIssue')
  #Dados do Paciente

class PreTMO(models.Model):
  data = models.DateTimeField('Data da Coleta dos Dados',null=False,blank=False)
  pass

class PosTMO(models.Model):
  data = models.DateTimeField('Data da Coleta dos Dados',null=False,blank=False)
  pass

class ResearchIssue(models.Model):
  data = models.DateTimeField('Data da Coleta dos Dados',null=False,blank=False)
  pass

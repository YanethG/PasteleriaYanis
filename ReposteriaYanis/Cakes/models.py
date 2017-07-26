from django.db import models
 #create your models here.
 class cakes(models.Model)
      """Almacena las publicaciones realizadas por el equipo
        administrativo """
        title = models.CharField(max_lenght=50,held_text= 'Ingrese el titulo de la pagina web')
        name= models.CharField(max_lenght=50,held_text='Ingrese el nombre del producto')
        models.DateTimeFimeFiald(auto_now=True )

        class comens(models, Model)


    

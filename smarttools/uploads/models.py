from django.db import models

from contests.models import Contest
# from smarttools.contests.models import Contest

'''
Desde el Home del Concurso, el usuario debe poder subir un nuevo video, para ello el  usuario  debe  ingresar:  
los  nombres,  los  apellidos,  el  email,  el  video  y  un  mensaje asociado al video.El usuario puede subir 
un video (o varios realizando envíos individuales) en  cualquier  formato  (ej.  AVI,WMV,  FLV,  MP4,  etc.).  
El  usuario  envía  el  video  y  en  ese momento el video queda en estado “En proceso” y aún NO deberá 
aparecer el video en el listadodel  Home  del  Concurso.  El  video  original  quedará  almacenado  en  un  
sistema dearchivos. 
'''


class Video(models.Model):
    title = models.CharField(max_length=100, default='Non-Title')
    description = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=150, default='Non-Name')
    sureName = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=254, null=True)
    video = models.FileField(upload_to='videos')
    created_At = models.DateTimeField(auto_now_add=False)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, null=False, blank=False, default=1)

    def __str__(self):
        return self.name + self.title

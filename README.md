# web-foromid-repo
Foro para compartir propuestas del MID

Este proyecto parte de la misma estructura de código que StudyBud.

Referencia:

[Video de YouTube](https://www.youtube.com/watch?v=PtQiiknWUcI&t=10322s)

[Repositorio GitHub](https://github.com/divanov11/StudyBud/)

El repositorio fue transformado para ser del MID y estar en español y adaptado para funcionar en una página de fly.io, conectado a una base de datos PG de fly y a un Google Storage en Google Cloud.

También tiene varios parches para su correcto funcionamiento, como un backend de autentificación, un sistema de usuarios, estáticos en whitenoise, corrección de errores, mejoras, entre otras.
Las imágenes de los avatares están conectados a Google Storage para que no se pierdan al reiniciarse en servidor.

Este repositorio no incluye las credenciales de google y fly-pg.

El resultado final puede verse en funcionamiento en la web en: [Foro MID](https://foromid.fly.dev/)

![El foro del MID](https://github.com/pacokrapo/web-foromid-repo/blob/main/media/ForoMID.png)

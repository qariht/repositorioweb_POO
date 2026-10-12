# Publicar el avance en GitHub

El repositorio Git local ya fue inicializado. Antes de publicar, completen los nombres del equipo en el `README.md` y revisen que no existan archivos personales que no deban compartirse.

## 1. Crear el repositorio remoto

En GitHub, creen un repositorio nuevo con un nombre como `repositorio-web-academico-unsch`.

- Seleccionen la visibilidad solicitada por el docente.
- No agreguen README, `.gitignore` ni licencia desde GitHub, porque ya existen localmente.

## 2. Registrar el primer avance

En una terminal abierta en la carpeta del proyecto, ejecuten:

```bash
git add .
git commit -m "feat: avance inicial del modelo POO"
```

## 3. Conectar y subir

Copien la URL del repositorio recién creado y reemplacen `URL_DEL_REPOSITORIO`:

```bash
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

## 4. Verificación final

En GitHub deben verse el README, las carpetas `src`, `tests` y `docs`. En la pestaña de archivos, el avance se podrá ejecutar con `python3 main.py` y comprobar con `python3 -m unittest discover -s tests -v`.

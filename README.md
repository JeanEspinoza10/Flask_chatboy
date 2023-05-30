
### Migraciones

- Iniciar las migraciones (Ejecuta una sola vez)

```sh
flask db init
```

- Crear una migración (Cuando se crea un modelo nuevo o se modifica uno anterior)

```sh
flask db migrate -m "Comentario"
```

- Subir los cambios a nuestra BD

```sh
flask db upgrade
```
# Login-and-Register

Aplicación GUI de registro y login en Python.

---

## 📋 Descripción

Este proyecto implementa una interfaz gráfica (GUI) para **registrar** y **loguear** usuarios. Los datos de los usuarios se almacenan en un archivo JSON (`Usuarios.json`). Está construido con Python, y los scripts principales son:

* `login.py`: Pantalla de inicio de sesión.
* `Registro.py`: Pantalla para registrar nuevos usuarios.
* `Usuarios.json`: Archivo para almacenar la información de usuario.

---

## 🛠️ Tecnologías usadas

* Python
* PyQt (o alguna librería gráfica que uses para la GUI)
* JSON (para persistencia sencilla de usuarios)

---

## ▶️ Cómo usar

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Ramerlinj/Login-and-Register.git
   cd Login-and-Register
   ```

2. (Opcional pero recomendado) Crea un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

   > Si no existe `requirements.txt`, instala manualmente lo que necesites (por ejemplo, PyQt).

4. Ejecuta la aplicación:

   ```bash
   python login.py
   # o
   python Registro.py
   ```

---

## 🔐 Cómo funciona

* Al registrar un usuario, los datos se guardan en `Usuarios.json`.
* Al hacer login, el programa verifica las credenciales contra ese archivo.
* Si las credenciales coinciden, se puede mostrar un mensaje de éxito o abrir otra ventana (según implementación).

---

## 🧪 Pruebas y uso

* Prueba primero registrando un nuevo usuario con `Registro.py`.
* Luego cierra esa ventana y abre `login.py` para iniciar sesión.
* Verifica que los datos se guarden correctamente en `Usuarios.json`.

---

## ⚙️ Mejoras posibles

Algunas ideas para expandir el proyecto:

* Encriptar las contraseñas antes de guardarlas (por ejemplo, usando `bcrypt` o `hashlib`).
* Añadir validaciones más robustas (correo, longitud de contraseña, caracteres especiales).
* Guardar los usuarios en una base de datos (SQLite, PostgreSQL, etc.) en lugar de JSON.
* Crear una interfaz más sofisticada con PyQt (pantalla principal después del login, perfiles de usuario, etc.).

---

## 👨‍💻 Contribuciones

Las contribuciones son bienvenidas. Si quieres aportar:

1. Haz un fork del repositorio.
2. Crea una rama con tu feature: `git checkout -b mi-feature`.
3. Haz commit de tus cambios: `git commit -m "Mi nueva funcionalidad"`.
4. Empuja la rama: `git push origin mi-feature`.
5. Abre un Pull Request.

---

## 📄 Licencia

Este proyecto no tiene una licencia explícita (por ahora), así que usa con responsabilidad. Si quieres agregar una licencia abierta, puedes considerar MIT, Apache o GPL.


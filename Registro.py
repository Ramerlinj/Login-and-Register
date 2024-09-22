from PyQt6.QtWidgets import (QDialog,QLabel,QPushButton,QLineEdit,QMessageBox)
from PyQt6.QtGui import QFont
import os 
import json

Archivo_usuarios = 'Usuarios.json'
import os 
import json

Archivo_usuarios = 'Usuarios.json'

class RegistroDeUsuario(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.formulario_segundo()
        
    def formulario_segundo(self):
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("Registro")
        
        usuario_label = QLabel(self)
        usuario_label.setText("Nombre")
        usuario_label.setFont(QFont("Comic Sans MS",11))
        usuario_label.move(55,54) 
        
        self.usuario_input = QLineEdit(self)
        self.usuario_input.resize(270,35)
        self.usuario_input.move(50,80)
        self.usuario_input.setFont(QFont("Comic Sans MS",11))
        self.usuario_input.setPlaceholderText("Ingrese un Nombre de usuario")
        
        password1_label = QLabel(self)
        password1_label.setText("Ingrese una contraseña")
        password1_label.setFont(QFont("Comic Sans MS",11))
        password1_label.move(55,125) 
        
        self.password1_input = QLineEdit(self)
        self.password1_input.resize(270,35)
        self.password1_input.move(50,150)
        self.password1_input.setFont(QFont("Comic Sans MS",11))
        self.password1_input.setPlaceholderText("Ingrese una contraseña")
        self.password1_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        
        password2_label = QLabel(self)
        password2_label.setText("Confirmar contraseña")
        password2_label.setFont(QFont("Comic Sans MS",11))
        password2_label.move(55,197) 
        
        self.password2_input = QLineEdit(self)
        self.password2_input.resize(270,35)
        self.password2_input.move(50,220)
        self.password2_input.setFont(QFont("Comic Sans MS",11))
        self.password2_input.setPlaceholderText("Confirmar Contraseña")
        self.password2_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        
        crear_btn = QPushButton(self)
        crear_btn.setText("Registrarse")
        crear_btn.resize(150,40)
        crear_btn.move(110,270)
        crear_btn.setFont(QFont("Segoe UI",11))
        crear_btn.clicked.connect(self.Registrarse)
        crear_btn.setStyleSheet("""
            QPushButton {
                background-color: #3c3c3c;    
                border-radius: 15px;          
                color: white;                 
                font-size: 16px;              
                padding:5px;     
                border-bottom: 0.5px solid #727272;  
            
            }
            QPushButton:hover {
                background-color: #424242;   
            }
            QPushButton:pressed {
                background-color: #4E4E4E; 
                color: #979696;   
            }
        """)
        
        btn_atras = QPushButton(self)
        btn_atras.setText("<-") #!Poner Icono mas adelante 21-9-24
        btn_atras.resize(50,35)
        btn_atras.move(10,2)
        btn_atras.setFont(QFont("Comic Sans MS",30))
        btn_atras.setStyleSheet("background-color: transparent; border: none;")
        btn_atras.clicked.connect(self.Volver_atras)
        
    def Volver_atras(self):
        self.close()
        
        
    def Registrarse(self):
        User = self.usuario_input.text()
        User = self.usuario_input.text()
        Password1 = self.password1_input.text()
        Password2 = self.password2_input.text()
        
        if User == "" or Password1 == "" or Password2 == "":
        if User == "" or Password1 == "" or Password2 == "":
            QMessageBox.warning(self,"Error","Los campos no pueden estar vacios",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        elif not User.isalnum():
        elif not User.isalnum():
            QMessageBox.warning(self,"Error","El nombre no puede contener ningun caracter especial",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        elif Password1 != Password2:
            QMessageBox.warning(self,"Error","Las contraseñas no coinciden",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        elif Password1 == Password2:
            if os.path.exists(Archivo_usuarios):
                with open(Archivo_usuarios,'r') as archivos:
                    Usuario = json.load(archivos)
            else:
                Usuario = {}
            if User in Usuario:
                QMessageBox.information(self,"Completado","El usuario ya esta en uso",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            else:
                Usuario[User] = Password1
                with open(Archivo_usuarios, 'w') as archivo:
                    json.dump(Usuario, archivo, indent=4)
                QMessageBox.information(self,"Completado","Se registro correctamente!",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
                self.close()
       
        elif Password1 == Password2:
            if os.path.exists(Archivo_usuarios):
                with open(Archivo_usuarios,'r') as archivos:
                    Usuario = json.load(archivos)
            else:
                Usuario = {}
            if User in Usuario:
                QMessageBox.information(self,"Completado","El usuario ya esta en uso",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            else:
                Usuario[User] = Password1
                with open(Archivo_usuarios, 'w') as archivo:
                    json.dump(Usuario, archivo, indent=4)
                QMessageBox.information(self,"Completado","Se registro correctamente!",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
                self.close()
       
                

                    
            
                
                
        
        
        

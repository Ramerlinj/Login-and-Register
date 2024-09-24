import sys,os,json
from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QMessageBox
from PyQt6.QtGui import QFont, QPixmap
from Registro import RegistroDeUsuario


Archivo_usuarios = 'Usuarios.json'


class Login(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializadorUI()
        
    def inicializadorUI(self):
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("Login")
        self.generarFormulario()
        self.show()
        
    def generarFormulario(self):
        self.is_logged = False #si estalogeado accede a todo los metodos de la app.
        
        user_label = QLabel(self)
        user_label.setText("Usuario")
        user_label.setFont(QFont("Comic Sans MS",11))
        user_label.move(55,54)
        
        self.user_input = QLineEdit(self)
        self.user_input.resize(300,35)
        self.user_input.move(50,80)
        self.user_input.setPlaceholderText("Ingrese su usuario")
        self.user_input.setFont(QFont("Comic Sans MS",11))#Segoe UI
        
        password_label = QLabel(self)
        password_label.setText("Password")
        password_label.setFont(QFont("Comic Sans MS",11))
        password_label.move(55,135)
        
        self.password_input = QLineEdit(self)
        self.password_input.resize(300,35)
        self.password_input.move(50,160)
        self.password_input.setEchoMode(
             QLineEdit.EchoMode.Password
         )
        self.password_input.setPlaceholderText("Ingrese su contraseña")
        self.password_input.setFont(QFont("Comic Sans MS",11))
        
        login_button = QPushButton(self)
        login_button.setText("Login")
        login_button.resize(100,40)
        login_button.move(80,220)
        login_button.setFont(QFont("Segoe UI",11))
        login_button.clicked.connect(self.Login)
        login_button.setStyleSheet("""
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
        
        
        register_button = QPushButton(self)
        register_button.setText("Registrate")
        register_button.resize(100,40)
        register_button.move(210,220)
        register_button.setFont(QFont("Segoe UI",11))
        register_button.clicked.connect(self.registrar_usuario)
        register_button.setStyleSheet("""
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
    
    def Login(self):
        user = self.user_input.text()
        contrasena = self.password_input.text()
        if os.path.exists(Archivo_usuarios):
            with open(Archivo_usuarios, 'r') as archivo:
                usuarios = json.load(archivo)
                
            if user in usuarios and usuarios[user] == contrasena:
                QMessageBox.information(self,"Compleado", "Se inicio sesion correctamente",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
                self.is_logged = True
            else:
                QMessageBox.warning(self,"Error", "El usuario o contraseña son incorrectas",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                
    def registrar_usuario(self):
        self.new_user_form = RegistroDeUsuario()
        self.new_user_form.show()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Login()
    sys.exit(app.exec())
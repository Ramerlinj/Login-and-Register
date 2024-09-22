import sys,os,json
import sys,os,json
from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QMessageBox,QCheckBox
from PyQt6.QtGui import QFont, QPixmap
from Registro import RegistroDeUsuario


Archivo_usuarios = 'Usuarios.json'

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
        self.is_logged = False
        
        user_label = QLabel(self)
        user_label.setText("Usuario")
        user_label.setFont(QFont("Comic Sans MS",11))
        user_label.move(20,59)
        
        self.user_input = QLineEdit(self)
        self.user_input.resize(250,35)
        self.user_input.move(90,50)
        self.user_input.setPlaceholderText("Ingrese su usuario")
        self.user_input.setFont(QFont("Comic Sans MS",11))#Segoe UI
        
        password_label = QLabel(self)
        password_label.setText("Password")
        password_label.setFont(QFont("Comic Sans MS",11))
        password_label.move(15,122)
        
        self.password_input = QLineEdit(self)
        self.password_input.resize(250,35)
        self.password_input.move(90,115)
        self.password_input.setEchoMode(
             QLineEdit.EchoMode.Password
         )
        self.password_input.setPlaceholderText("Ingrese su contraseña")
        self.password_input.setFont(QFont("Comic Sans MS",11))
        
        #self.check_vista_password = QCheckBox(self)
        #self.check_vista_password.setText("Ver Contraseña")
        #self.check_vista_password.move(95,155)
       # self.check_vista_password.toggled.connect(self.mostrar_contraseña_check)
        
         
        login_button = QPushButton(self)
        login_button.setText("Login")
        login_button.resize(100,40)
        login_button.move(90,190)
        login_button.setFont(QFont("Segoe UI",11))
        login_button.clicked.connect(self.iniciar_mainview)
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
        register_button.move(220,190)
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
    
    
    #def mostrar_contraseña_check(self,cliked):
        #if cliked:
            #self.password_input.setEchoMode(
                #QLineEdit.EchoMode.Normal
            #)
        #else:
             #self.password_input.setEchoMode(
                #QLineEdit.EchoMode.Password
             #)
    
    def iniciar_mainview(self):
        user = self.user_input.text()
        contrasena = self.password_input.text()
        if os.path.exists(Archivo_usuarios):
            with open(Archivo_usuarios, 'r') as archivo:
                usuarios = json.load(archivo)
                
            if user in usuarios and usuarios[user] == contrasena:
                QMessageBox.information(self,"Compleado", "Se inicio sesion correctamente",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.warning(self,"Error", "El usuario o contraseña son incorrectas",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

                

        user = self.user_input.text()
        contrasena = self.password_input.text()
        if os.path.exists(Archivo_usuarios):
            with open(Archivo_usuarios, 'r') as archivo:
                usuarios = json.load(archivo)
                
            if user in usuarios and usuarios[user] == contrasena:
                QMessageBox.information(self,"Compleado", "Se inicio sesion correctamente",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.warning(self,"Error", "El usuario o contraseña son incorrectas",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

                

    
    def registrar_usuario(self):
        self.new_user_form = RegistroDeUsuario()
        self.new_user_form.show()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Login()
    sys.exit(app.exec())
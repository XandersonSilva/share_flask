from app import db


class User(db.Model):
    __tablename__ = 'users'

    user_id  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name     = db.Column(db.String)
    usrname  = db.Column(db.String, unique=True) 
    email    = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, username, password, name, email):
        self.usrname  = username
        self.password = password
        self.name     = name
        self.email    = email

    def __repr__(self):
        return "<User %r>" % self.usrname
    
class Upload(db.Model):
    __tablename__ = "uploads"

    upload_id    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name         = db.Column(db.Text)
    user_id      = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    upload_data  = db.Column(db.DateTime, index=True)
    type_Up      = db.Column(db.Integer)
    category     = db.Column(db.Text)
    content      = db.Column(db.Text)

    def  __init__(self,name,user_id,uploud_data,type_Up,category,content):
        self.name         = name
        self.user_id      = user_id
        self.uploud_data  = uploud_data
        self.type_Up      = type_Up
        self.category     = category
        self.content      = content

class ConversationPeople(db.Model):
    __tablename__ = "conversation_people"
    
    conv_people_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_snd = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user_rcv = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __init__(self, user_snd, user_rcv):
        self.user_snd = user_snd
        self.user_rcv = user_rcv
    
class Conversation(db.Model):
    __tablename__ = "conversations"
    
    conv_id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Corrigir a chave estrangeira para referenciar corretamente conv_people_id
    conversation =  db.Column(db.Integer, db.ForeignKey("conversation_people.conv_people_id"))

    # Adicionar o relacionamento entre Conversation e ConversationPeople
    conv_people = db.relationship('ConversationPeople', backref='conversation', lazy=True)

    name =  db.Column(db.Text)

    def __init__(self, conversation, name):
        self.conversation = conversation
        self.name = name

class Mensage(db.Model):
    __tablename__ = "mensages"

    mensage_id    =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    conv_id       =  db.Column(db.Integer, db.ForeignKey('conversations.conv_id'), nullable=False)
    snd_id        =  db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    content       =  db.Column(db.Text)
    time_send     =  db.Column(db.DateTime)
    msg_state     =  db.Column(db.SmallInteger, default=0) # 0: enviado, 1: leido

    def __init__(self, conv_id,snd_id,content,time_send,msg_state):
        self.conv_id      = conv_id
        self.snd_id       = snd_id
        self.content      = content
        self.time_send    = time_send
        self.msg_state    = msg_state
            



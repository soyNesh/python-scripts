from datetime import datetime
import locale
import emoji

locale.setlocale(locale.LC_ALL, 'es-MX') 

class Gabriel:

    def __init__(self):
        self.author = 'Alejandro Huerta Campos a.k.a N3sh'
        self.city = 'Querétaro'
        self.date_object = datetime(2021, 8, 2)
        self.name = 'Gabe'
        self.full_name = 'Gabriel López'
        self.town = 'Querétaro'
        self.meme = 'Primero que nada, buenos días'
        self.jose_jose = 'Qué triste fue decirnos adiós, cuando nos adorábamos más...'
        self.app = '9gag'

    def say_goodbye(self):
        str = f"""
                                                    {self.city}, {self.town} a {self.date_object.strftime('%d de %B del %Y')}

            ¡{self.name}! {self.meme} {emoji.emojize(':grinning_squinting_face:')}

            Recuerdo el momento en que Vale me platicó que un tal {self.full_name} 
            iba con ella en su salón de la carrera y que había sido la primera persona
            con la que había hablado el primer día de clases, todo gracias a {self.app}. Le dije 
            que le preguntara si había estado en el Colegio Washington en la primaria, a 
            lo que respondió afirmativamente. Con gran alegría yo le platiqué que también 
            lo conocía y que había sido un gran amigo en aquella época.

            Algunos días después llegó el momento de conocer y convivir con los nuevos amigos de
            Vale y fue ahí cuando volví a ver, luego de muchos años, al buen {self.name}. Fue muy
            grato platicar y recordar eventos y personajes del contexto histórico que alguna vez
            compartimos.

            {self.name}, quiero decirte que me dio mucho gusto revivir nuestra amistad y que hayamos
            podido coincidir de nuevo. Tengo muchas grandes anécdotas en la memoria de nuestra etapa
            universitaria.

            Espero que esta nueva aventura que ahora emprendes esté llena de éxito y que todos tus planes
            y objetivos se cumplan, lo mereces.

            Quiero que sepas que aquí tienes a un amigo y ojalá que nos podamos seguir viendo. Ya tendremos 
            Vale y yo un gran motivo para irnos de paseo a Canadá jeje

            Te mando un gran abrazo.
        
            Saludos.

            Atentamente,
            {self.author}

            "{self.jose_jose} {emoji.emojize(':speak-no-evil_monkey:')}"
        """
        print(str)

g = Gabriel()

g.say_goodbye()

from mycroft import MycroftSkill, intent_file_handler


class GrupoDeRisco(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('risco.de.grupo.intent')
    def handle_risco_de_grupo(self, message):
        self.speak_dialog('risco.de.grupo')


def create_skill():
    return GrupoDeRisco()


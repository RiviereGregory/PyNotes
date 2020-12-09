from uuid import uuid4

class Note:
    def __init__(self, title="", content="", uuid=None):
        self.uuid = str(uuid4())
        self.title = title
        self.content = content


if __name__ == '__main__':
    n = Note(title="Ceci est une note", content="ceci est un contenu")
    print(n.uuid)

import uuid

class UsuarioCRUD:
   def __init__(self, session):
      self.session = session

   def criar_usuario(self, nome, email):
      user_id = uuid.uuid4()
      self.session.execute(
            "INSERT INTO usuarios (id, nome, email) VALUES (%s, %s, %s)",
            (user_id, nome, email)
      )
      return user_id

   def ler_usuario(self, user_id):
      result = self.session.execute(
            "SELECT * FROM usuarios WHERE id = %s", (user_id,)
      )
      return result.one()

   def atualizar_usuario(self, user_id, nome, email):
      self.session.execute(
            "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s",
            (nome, email, user_id)
      )

   def deletar_usuario(self, user_id):
      self.session.execute(
            "DELETE FROM usuarios WHERE id = %s", (user_id,)
      )

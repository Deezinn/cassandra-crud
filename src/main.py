from db.connect_db import get_session
from crud.crud import UsuarioCRUD

def main():
   session = get_session('meu_keyspace')
   crud = UsuarioCRUD(session)

   user_id = crud.criar_usuario("Andrezinho Lindo", "andrezinho@email.com")
   print(f"Usuário criado com ID: {user_id}")

   user = crud.ler_usuario(user_id)
   print("Usuário lido:", user)

   crud.atualizar_usuario(user_id, "André Luiz", "andrelsn@email.com")
   print("Usuário atualizado.")

   user = crud.ler_usuario(user_id)
   print("Usuário atualizado:", user)

   crud.deletar_usuario(user_id)
   print("Usuário deletado.")

if __name__ == "__main__":
   main()

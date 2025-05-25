from cassandra.cluster import Cluster # type: ignore

def get_session(keyspace):
   cluster = Cluster(['127.0.0.1'])
   session = cluster.connect()
   session.execute(f"""
      CREATE KEYSPACE IF NOT EXISTS {keyspace}
      WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}}
   """)
   session.set_keyspace(keyspace)
   session.execute("""
      CREATE TABLE IF NOT EXISTS usuarios (
            id UUID PRIMARY KEY,
            nome TEXT,
            email TEXT
      )
   """)
   return session

# print(get_session('meu_keyspace'))

from sqlalchemy import create_engine, text
import os


db_connection_string = os.environ['DB_CONECTION_STRING']




engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
 )

  
def full_db(koncentracja):
  with engine.connect() as conn:
    query = text("INSERT INTO koncentracja (plec, wiek, godzina, miejsce, samopoczucie, koncentracja, problemy, pora_dnia,miejsce_koncentracja ) VALUES (:plec, :wiek, :godzina, :miejsce, :samopoczucie, :koncentracja, :problemy, :pora_dnia,:miejsce_koncentracja)")
    
    conn.execute(query, 
                 {'wiek': koncentracja['plec'], 
                  'plec': koncentracja['wiek'],
                  'godzina': koncentracja['godzina'],
                  'miesce': koncentracja['miesce'],
                  'koncentracja': koncentracja['koncentracja'],
                  'problemy': koncentracja['problemy'],
                  'pora_dnia': koncentracja['pora_dnia'],
                  'miejsce_koncentracja': koncentracja['miejsce_koncentracja'],
                 })
import psycopg2


class Sql:
    def __init__(self, database, user, password):
        self.database = database
        self.user = user
        self.password = password

    def create_table(self):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE Clients
                (
                    client_id SERIAL PRIMARY KEY,
                    Name VARCHAR(30) NOT NULL,
                    Last_name VARCHAR(30) NOT NULL,
                    Email VARCHAR(60)
                );
    
                CREATE TABLE Phone_numbers
                (
                    phone_id SERIAL PRIMARY KEY,
                    client_id INT REFERENCES Clients(client_id),
                    Phone_number VARCHAR(15)
                );
            ''')
        conn.commit()
        conn.close()

    def new_client(self, name, last_name, email):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute(f'''
                INSERT INTO Clients (Name, Last_name, Email) VALUES
                ('{name}', '{last_name}', '{email}');
            ''')
        conn.commit()
        conn.close()

    def add_phone_number(self, client_id, phone_number):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute(f'''
                INSERT INTO Phone_numbers (client_id, Phone_number) VALUES
                ({client_id}, '{phone_number}');
            ''')
        conn.commit()
        conn.close()

    def update_client_data(self, client_id):
        name = input('Введите имя для замены (Enter = пропустить): ')
        last_name = input('Введите фамилию для замены (Enter = пропустить): ')
        email = input('Введите email для замены (Enter = пропустить): ')
        phone = input('Введите телефон для замены (Enter = пропустить): ')
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            if len(name) != 0:
                cur.execute(f'''
                    UPDATE Clients
                    SET Name = '{name}'
                    WHERE client_id = {client_id};
                ''')
            if len(last_name) != 0:
                cur.execute(f'''
                    UPDATE Clients
                    SET Last_name = '{last_name}'
                    WHERE client_id = {client_id};
                ''')
            if len(email) != 0:
                cur.execute(f'''
                    UPDATE Clients
                    SET Email = '{email}'
                    WHERE client_id = {client_id};
                ''')
            if len(phone) != 0:
                phone_id = input('Введите id номера который нужно заменить: ')
                cur.execute(f'''
                    UPDATE Phone_numbers
                    SET Phone_number = '{phone}'
                    WHERE phone_id = {phone_id} AND client_id = {client_id};
                ''')
        conn.commit()
        conn.close()

    def delete_phone_number(self, phone_id):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute(f'''
                DELETE FROM Phone_numbers
                WHERE phone_id = {phone_id};     
            ''')
        conn.commit()
        conn.close()

    def delete_client(self, client_id):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute(f'''
                DELETE FROM Clients
                WHERE client_id = {client_id};     
            ''')
        conn.commit()
        conn.close()

    def find_client(self):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            name = input('Введите имя для поиска (Enter = пропустить): ')
            if len(name) != 0:
                cur.execute(f'''
                    SELECT clients.client_id FROM Clients
                    WHERE Name = '{name}';
                ''')
                return cur.fetchone()[0]
            else:
                last_name = input('Введите фамилию для поиска (Enter = пропустить): ')

            if len(last_name) != 0:
                cur.execute(f'''
                    SELECT clients.client_id FROM Clients
                    WHERE Last_name = '{last_name}';       
                ''')
                return cur.fetchone()[0]
            else:
                email = input('Введите email для поиска (Enter = пропустить): ')

            if len(email) != 0:
                cur.execute(f'''
                    SELECT clients.client_id FROM Clients
                    WHERE Email = '{email}';        
                ''')
                return cur.fetchone()[0]
            else:
                phone = input('Введите телефон для поиска (Enter = пропустить): ')

            if len(phone) != 0:
                cur.execute(f'''
                    SELECT phone_numbers.client_id FROM Phone_numbers
                    WHERE Phone_number = '{phone}';            
                ''')
                return cur.fetchone()[0]
        conn.commit()
        conn.close()


user1 = Sql(database='Your database', user='postgres', password='Your password')
#user1.create_table()
#user1.new_client('Анатолий', 'Карпов', 'anatioliykarpov.mail.ru')
#user1.add_phone_number(1, '+7**********')
#user1.update_client_data(1)
#print(user1.find_client())
#user1.delete_phone_number(1)
#user1.delete_client(1)

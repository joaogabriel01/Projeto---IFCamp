import MySQLdb
print('COnectando...')
conn = MySQLdb.connect(user='root', passwd='', host='127.0.0.1', port=3306, charset='utf8')

# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP DATABASE `db_Camp`;")
conn.commit()

#Descomente para criar o banco e suas tabelas
criar_tabelas = '''
    CREATE DATABASE db_Camp DEFAULT CHARSET=utf8;
    USE `db_Camp`;
    CREATE TABLE `tb_jogos` ( 
        `idJogos` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `Nome` VARCHAR(45) NULL);
    CREATE TABLE `tb_campeonatos` ( 
        `idCampeonato` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        `Nome` VARCHAR(45) NOT NULL, `Premio` VARCHAR(45) NOT NULL, 
        `Data_Criacao` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
        `Data_Camp` DATETIME, 
        `idJogos` INT NOT NULL, 
        FOREIGN KEY(`idJogos`) REFERENCES `tb_jogos`(`idJogos`) );
    CREATE TABLE `tb_usuarios` ( 

        `usuario` VARCHAR(45) NOT NULL PRIMARY KEY, 
        `senha` VARCHAR(45) NOT NULL,
        `tipo_usuario` INT NOT NULL);
    CREATE TABLE `tb_times` ( 
        `idTime` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        `nome` VARCHAR(45) NULL);
    CREATE TABLE `tb_usuarios_times` ( 
        `usuario` VARCHAR(45) NOT NULL , 
        `idTime` INT NOT NULL, 
        FOREIGN KEY(`usuario`) REFERENCES tb_usuarios(usuario), 
        FOREIGN KEY(`idTime`) REFERENCES tb_times(idTime));
    CREATE TABLE `tb_campeonatos_times` ( 
        `idCampeonato` INT NOT NULL, `idTime` INT NOT NULL, 
        FOREIGN KEY(`idCampeonato`) REFERENCES tb_campeonatos(idCampeonato), 
        FOREIGN KEY(`idTime`) REFERENCES tb_times(idTime));
'''




# #inserindo usuarios
cursor = conn.cursor()
cursor.execute(criar_tabelas)

cursor.executemany(
      'INSERT INTO db_Camp.tb_usuarios (usuario, senha, tipo_usuario) VALUES (%s, %s, %s)',
      [
            ('joao', 'root', 1),
            ('nico', 'Nico', 2)

      ])

cursor.execute('select * from db_Camp.tb_usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# # cursor.executemany
conn.commit()
cursor.close()
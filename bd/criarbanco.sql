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
        `idUsuario` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `usuario` VARCHAR(45) NOT NULL,
        `senha` VARCHAR(45) NOT NULL,
        `tipo_usuario` INT NOT NULL);
    CREATE TABLE `tb_times` (
        `idTime` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `nome` VARCHAR(45) NULL);
    CREATE TABLE `tb_usuarios_times` (
        `idUsuario` INT NOT NULL,
        `idTime` INT NOT NULL,
        FOREIGN KEY(`idUsuario`) REFERENCES tb_usuarios(idUsuario),
        FOREIGN KEY(`idTime`) REFERENCES tb_times(idTime));
    CREATE TABLE `tb_campeonatos_times` (
        `idCampeonato` INT NOT NULL, `idTime` INT NOT NULL,
        FOREIGN KEY(`idCampeonato`) REFERENCES tb_campeonatos(idCampeonato),
        FOREIGN KEY(`idTime`) REFERENCES tb_times(idTime));
-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 30-Set-2022 às 19:41
-- Versão do servidor: 5.7.36
-- versão do PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `botdiscord`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `commands`
--

DROP TABLE IF EXISTS `commands`;
CREATE TABLE IF NOT EXISTS `commands` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `commandName` varchar(45) NOT NULL,
  `answer` varchar(9999) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `commands`
--

INSERT INTO `commands` (`ID`, `commandName`, `answer`) VALUES
(1, '$hello', 'Olá, seja bem-vindo Autor!'),
(11, '$github', 'Coloque o nome de um usuário no github e veja suas curiosidades!'),
(5, '$rules', 'Autor vou explicar as regras do servidor para que você não tenha nenhum problema:\r\n\r\n1 - Respeitar os colegas\r\n\r\n2 - Não enviar spam\r\n\r\n3 - Seja amigável com os outros que eles serão amigáveis com você!\r\n\r\nDivirta-se!\r\n                                     '),
(6, '$commands', 'Autor - Comandos do BotTester:\r\n1 - $hello - Eu digo olá para você!\r\n\r\n2 - $rules - Digo as regras do servidor para você!\r\n\r\n3 - $github{Usuário} - Mostra alguns dados curiosos sobre o desenvolvedor escolhido!\r\n'),
(10, '$github', 'Coloque o nome de um usuário no github e veja suas curiosidades!');

-- --------------------------------------------------------

--
-- Estrutura da tabela `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(40) NOT NULL,
  `id_user` bigint(20) NOT NULL,
  `points` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `user`
--

INSERT INTO `user` (`ID`, `Name`, `id_user`, `points`) VALUES
(1, 'Japuneis', 1024341823533109270, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

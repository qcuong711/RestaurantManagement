-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: projecttt
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `drinks`
--

DROP TABLE IF EXISTS `drinks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drinks` (
  `d_id` varchar(20) NOT NULL,
  `d_name` varchar(20) NOT NULL,
  `d_price` float NOT NULL,
  PRIMARY KEY (`d_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drinks`
--

LOCK TABLES `drinks` WRITE;
/*!40000 ALTER TABLE `drinks` DISABLE KEYS */;
INSERT INTO `drinks` VALUES ('D1','CA PHE',50000),('D2','NUOC NGOT',40000),('D3','NUOC EP CAM',60000),('D4','NUOC DUA',50000),('D5','SODA CHANH',50000),('D6','SODA SUA HOT GA',60000),('D7','NUOC EP DUA HAU',50000);
/*!40000 ALTER TABLE `drinks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `e_id` varchar(20) NOT NULL,
  `e_name` varchar(50) NOT NULL,
  `m_id` varchar(20) NOT NULL,
  `hire_date` date NOT NULL,
  `job` varchar(20) NOT NULL,
  `salary` float NOT NULL,
  PRIMARY KEY (`e_id`),
  KEY `m_id` (`m_id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`m_id`) REFERENCES `manager` (`m_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('E1','VAN LAM','M1','2017-11-17','BAO VE',6500000),('E10','DUC HUY','M3','2018-04-22','BOI BAN',6500000),('E11','DUY MANH','M3','2019-03-25','BOI BAN',5600000),('E12','ANH DUC','M3','2019-05-12','BOI BAN',5400000),('E13','DINH TRONG','M3','2019-01-30','BOI BAN',5200000),('E14','HONG DUY','M3','2018-12-23','BOI BAN',5750000),('E15','QUANG HAI','M3','2018-01-11','BOI BAN',5900000),('E16','TRONG HOANG','M3','2019-03-02','BOI BAN',5000000),('E17','MINH VUONG','M3','2018-04-07','BOI BAN',5300000),('E18','TUAN MANH','M3','2018-02-04','BOI BAN',5400000),('E19','XUAN MANH','M3','2018-05-07','BOI BAN',5800000),('E2','NGUYEN MANH','M1','2018-03-05','BAO VE',5800000),('E9','XUAN TRUONG','M3','2018-07-11','BOI BAN',5900000);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `foods`
--

DROP TABLE IF EXISTS `foods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `foods` (
  `f_id` varchar(20) NOT NULL,
  `f_name` varchar(20) NOT NULL,
  `f_price` float NOT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `foods`
--

LOCK TABLES `foods` WRITE;
/*!40000 ALTER TABLE `foods` DISABLE KEYS */;
INSERT INTO `foods` VALUES ('F1','GOI CUON',170000),('F10','SUP NAM ROM CUA',160000),('F11','SUP BAP CUA',160000),('F12','BANH MI TOM CHIEN',150000),('F2','CHA GIO',160000),('F3','SUP BAP GA',140000),('F4','XA XIU GA',200000),('F5','RAU CAI XAO DAU',190000),('F6','GA SATE LUI',180000),('F7','TOM LAC BOT',170000),('F8','MI THAP CAM',230000),('F9','COM CHIEN',160000);
/*!40000 ALTER TABLE `foods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager` (
  `m_id` varchar(20) NOT NULL,
  `m_name` varchar(50) NOT NULL,
  `salary` float NOT NULL,
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager`
--

LOCK TABLES `manager` WRITE;
/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
INSERT INTO `manager` VALUES ('M1','VAN THANH',17000000),('M2','HUY HUNG',22500000),('M3','TIEN LINH',21800000);
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'projecttt'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-27 22:16:12

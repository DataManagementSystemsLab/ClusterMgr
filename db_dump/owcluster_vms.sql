-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: owcluster
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vms`
--

DROP TABLE IF EXISTS `vms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vms` (
  `id` int NOT NULL AUTO_INCREMENT,
  `indx` int DEFAULT NULL,
  `ipaddr` varchar(15) DEFAULT NULL,
  `memory` int DEFAULT NULL,
  `vcpu` int DEFAULT NULL,
  `vmtype` varchar(10) DEFAULT NULL,
  `macaddr` varchar(30) DEFAULT NULL,
  `hostname` varchar(30) DEFAULT NULL,
  `disk_image` varchar(40) DEFAULT NULL,
  `location` varchar(10) DEFAULT NULL,
  `managed` tinyint(1) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ipaddr` (`ipaddr`),
  UNIQUE KEY `macaddr` (`macaddr`),
  UNIQUE KEY `hostname` (`hostname`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vms`
--

LOCK TABLES `vms` WRITE;
/*!40000 ALTER TABLE `vms` DISABLE KEYS */;
INSERT INTO `vms` VALUES (1,0,'10.100.04.00',4,2,NULL,'ae:52:00:00:00:00','khalefam',NULL,'owhpc-00',NULL,NULL),(2,1,'10.100.04.01',4,2,NULL,'ae:52:00:00:00:01','noutsosc',NULL,'owhpc-00',NULL,NULL),(3,2,'10.100.04.02',4,2,NULL,'ae:52:00:00:00:02','balyanr',NULL,'owhpc-00',NULL,NULL),(4,3,'10.100.04.03',4,2,NULL,'ae:52:00:00:00:03','rayanas',NULL,'owhpc-00',NULL,NULL),(5,10,'10.100.3.10',10,5,NULL,'ae:52:03:00:04:0a','db',NULL,'owhpc-01',1,NULL),(6,11,'10.100.4.56',4,2,NULL,'ae:52:00:00:04:0b','net0',NULL,'owhpc-00',1,NULL),(7,12,'10.100.4.57',4,2,NULL,'ae:52:00:00:04:0c','net1',NULL,'owhpc-01',1,NULL),(8,13,'10.100.4.58',4,2,NULL,'ae:52:00:00:04:0d','vm1',NULL,'owhpc-05',1,NULL),(9,20,'10.100.6.50',4,2,NULL,'ae:52:06:00:00:50','pchau1',NULL,'owhpc-01',1,NULL),(10,21,'10.100.6.51',4,2,NULL,'ae:52:06:00:00:51','emastroc',NULL,'owhpc-01',1,NULL),(11,22,'10.100.6.52',4,2,NULL,'ae:52:06:00:00:52','vyashaev',NULL,'owhpc-01',1,NULL),(12,23,'10.100.6.53',4,2,NULL,'ae:52:06:00:00:53','kthomp39',NULL,'owhpc-01',1,NULL),(13,24,'10.100.6.54',4,2,NULL,'ae:52:06:00:00:54','jcozzoli',NULL,'owhpc-01',1,NULL),(14,25,'10.100.6.55',4,2,NULL,'ae:52:06:00:00:55','cpeter16',NULL,'owhpc-01',1,NULL);
/*!40000 ALTER TABLE `vms` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-21 18:28:02

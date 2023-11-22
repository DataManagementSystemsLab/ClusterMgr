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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(15) DEFAULT NULL,
  `lastname` varchar(40) DEFAULT NULL,
  `firstname` varchar(40) DEFAULT NULL,
  `passwd` varchar(40) DEFAULT NULL,
  `hashpasswd` varchar(40) DEFAULT NULL,
  `secret_key` char(40) DEFAULT NULL,
  `grp` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `sent` tinyint(1) DEFAULT NULL,
  `created` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (64,'kmertz1','Mertz','Kevin D.',NULL,'263a840ba5225c07836a83fd19241ad1bb2b9310','RFGW4WG6UJEEFFVKADBJZ3NGN4YFD7OQ','GP_Students','kmertz1@oldwestbury.edu',1,1),(65,'rshahid','Shahid','Rahma',NULL,'d977f11c86242c3aab9fe916f058bfdf9318a8b6','6GG7UX3EO2QVUOS4SESBASOZAUCCBSMG','GP_Students','rshahid@oldwestbury.edu',1,1),(66,'tverma','Verma','Taruna',NULL,'20f93c7a331143ec27439fdd417b4c80817c6709','CC3FZO7EVDPE7E6M7FTUOPWUMHO4U2E3','GP_Students','tverma@oldwestbury.edu',1,1),(68,'pchau1','Chau','Philip',NULL,'6733193a5c4990454ac40c6dd602723fdca623d6','MA4XTG2HY5FFRJZGIG2QG2PXZANYXJK7','GP_Students','pchau1@oldwestbury.edu',1,1),(69,'emastroc','Mastrocola','Emily',NULL,'057d670447cc8a6b2fbdd92f295c04ce98ee7672','6PEYK2D2B6QE6CDHYB2S7IZAWBJUZPS3','GP_Students','emastroc@oldwestbury.edu',1,1),(70,'vyashaev','Yashaev','Vladislav',NULL,'baa1f699d32e83ca108e8b5597b764f114c451d2','56II5KYGBL227W5YTWZRZKE7VLODV3ZA','GP_Students','vyashaev@oldwestbury.edu',1,1),(71,'kthomp39','Thompson','Kayla',NULL,'0f98bb736882701a41b6d3526b3db8d967a00b47','TFIFBB24MWZVT62ABMAVSU7SCMWKQ2R5','GP_Students','kthomp39@oldwestbury.edu',1,1),(72,'noutsosc','Christos','Noutsos',NULL,'98dcf76bc245ad36972f1f811e62c72f5d4a9fb1','VLN26RL5OD3CLBLLQIHHU7BEWTLS2RG7','GP_Students','noutsosc@oldwestbury.edu',1,1),(74,'cpeter16','Petersen','Christian J.',NULL,'e43bd8ca3d883ec677bbcd4d45248321efe0d158','V44ASOAJKRFW66FRIFXYUA5BJHXIHPP3','GP_Students','cpeter16@oldwestbury.edu',1,1),(75,'balyanr','Balyan','Renu',NULL,'03073aa28f38d5ba9312cb6a871a517f9e946ea8','6TK374JLSBET6M56RGNWPWFL2WX7U7FB','GP_Students','balyanr@oldwestbury.edu',1,1),(76,'khalefam','khalefa','Mohamed',NULL,'46888b397ef0799b23790b7fb46bd1c2e35fc318','FNA7O7IGBRTZAXLQRRNO7FAYZ2EXN63J','GP_Students','khalefam@oldwesbury.edu',1,1),(77,'willkoman','William','Krasnov',NULL,'36ade69380c4d1a1975c6cf25f4ac126f3e4de63','HRD2773XYLW6GUIBSBH52O4KTHJWGIVW','GP_Students','willkoman@gmail.com',1,1),(78,'rfelix3','Raymundo','Felix',NULL,'61d7d00bb9df94f101006a2684158783547b7d05','MY35V4OSOAT34M2N5FFOTDRHKUZ5IBJA','GP_Students','Rfelix3@oldwestbury.edu',1,1),(79,'cgrimad1','Christine','Grimadeau',NULL,'d05b5e7cf24553927b992da710c00a3a33e06455','JA3Z5PPFD54KEPLU5RJA4XBSILODO2JU','GP_Students','cgrimad1@oldwwstbury.edu',1,1),(80,'syaw1','Syrai','yaw',NULL,'8cb40e21520589995728d6f30c208fe54c4b88c9','5JYV6W5Z4PTOPRP3Q4UAIGZZ4WRESDES','GP_Students','Syaw1@oldwestbury.edu',1,1),(81,'afrett','Andrew','Frett',NULL,'d3482ae1461c90de04fa87d4138d937296b871e8','SJPHLKP4G5CK26Z7ES2OEGHYVYFNAWYS','GP_Students','AFrett@oldwestbury.edu',1,1),(82,'gsingh23','Gagandeep','Singh',NULL,'12e32fbebfaf4546a8ba01379e458954054b4a40','T74ZVPTIN2NLCTIID4CKQ7ZG755OPNCA','GP_Students','gsingh23@oldwestbury.edu',1,1),(83,'mvalles','Michael','Valles',NULL,'8771e718fb1a09e84f680cf4db829f3eefce9933','XDYMZ7QTGZNKEDXNFQ2X6ZXQXCMEA3IL','GP_Students','mvalles@oldwestbury.edu',1,1),(84,'snaqvi3','Sami','Naqvi',NULL,'2c5ae05e710e8537487623a7b1eb3045b194a122','7BH6EUKMSXBGVG7OIVLNS7E2UXWK5X2G','GP_Students','snaqvi3@oldwestbury.edu',1,1),(85,'llehr','Larry','Lehr',NULL,'4ec47f44e49350fdce2cba31a0c23bdfd8d984b3','BMYWHSHVAFCTEO5JZ2A5BACUI5UL3K3K','GP_Students','llehr@oldwestbury.edu',1,1),(87,'gramchar','Ganesh','Ramcharan',NULL,'16ecc62207bfda9c20b88c691588931dbc480235','HTMCBOGMBJ6VNKPHZUDWE74MDTX2REBU','GP_Students','gramchar@oldwestbury.edu',1,1),(88,'ecomrie','Evan','Comrie',NULL,'62ddebfc77b17f13959ff4d3d85372899b75ee46','55FGYPFICJIROXMOR3LU6CZ5SZYBM7J4','GP_Students','ecomrie@oldwestbury.edu',1,1),(89,'mrondell','Audrey','Rondello',NULL,'4d7913c60e73a536fc01869d0ba8b15c1d3aaa3b','OYPNACKMMY5I33IPNX4WNT7HRDZ3BZMV','GP_Students','mrondell@oldwesbury.edu',1,1),(90,'njust','Nicole','Just',NULL,'e3408600c3f09c1b9b54c9596d2dc39728f6f952','UNSWDBYICDZWHFDZAIVZY3EJOHSIS57J','GP_Students','njust@oldwestbury.edu',1,1),(91,'jramir64','Jair','Ramirez',NULL,'7ea9bf6e937b245a36fab6c42ab4a35d0d411e18','VGKE3UN4FQX5OXHWTQXH67OVHCJVJFO7','GP_Students','jramir64@oldwestbury.edu',1,1),(92,'tsingh17','tadhbir','singh',NULL,'d2fd2fa16dd039e1bf3787e0691d78600d093e1a','WA3BBBCUVS5JJRS6TYDB5CCD2HQ5M7M4','GP_Students','tsingh17@gmail.com',1,1),(93,'nsarwar1','Nawal','Sarwar',NULL,'cc272eca956af31f0089a42294d334342328b22b','QMA6UCXETGKJ4PWONRWQCIHTI66RMAL5','GP_Students','nsarwar1@oldwestbury.edu',1,1),(94,'jacksonbeach339','Jackson','Beach',NULL,'38213d9770fed4406010ef32bc3165687d6e6bc3','U7C7DQ4Y5HJXVCBXAMZFBTKQEVQDKX6A','GP_Students','jacksonbeach339@gmail.com',1,1),(95,'fzahid1','Faizan','Zahid',NULL,'20ce7722c22acc27f6e735ce675eea80e9266893','L44RXS64BDXQJ4YAIZRX4SU6HATAEPNX','GP_Students','fzahid1@sunyoldwestbury.edu',1,1),(96,'sbhatta1','Sajal','bhattarai',NULL,'5243195e13c859c4387a94ddcd98e6ab516723f1','Y7R5ZEF3DWS37IXOWR6FHCZFHTMWL5NP','GP_Students','sbhatta1@oldwestbury.edu',1,1),(97,'mhochste','Matthew','Hochstein',NULL,'d18c604d7e3be10bf54e563af19117aaa7fe58fc','4N7IVKKIJBZE7MLLU4MVMWYWTDCJJGR2','GP_Students','mhochste@oldwestbury.edu',1,1),(98,'aniqabidaa','Aniq','Abid',NULL,'4e58ad83dd3726aaa9dcae56ffd8195e99eb7212','P2P6URBLDIK2YFNHHR7RNVEL2H77DRUQ','GP_Students','aniqabidaa@hotmail.com',1,1),(99,'dpatel18','Darshan','Patel',NULL,'0b183de3966cc5a20f1e302953d3831efecae036','HC76SARDLEOZB2HB5FZHC6BRXFY7RT5Q','GP_Students','dpatel18@oldwestbury.edu',1,1),(100,'rayanas','rayana','shebuti',NULL,'b32829e96e8d1949dae3156e5e356be6d726f31a','LZ2XNZMOGSZ5QEO4U6P2MAS2ILRMAPIK','GP_Students','rayanas@oldwestbury.edu',1,1),(123,'demo',NULL,NULL,NULL,'61b72afce907fc9a074e29b612623040dc226f58','M24SUHWE3CSKD3V53Q75X2YEVERL2GDK','GP_Students','owcluster@gmail.com',NULL,NULL),(124,'jcozzoli','Cozzolino','John',NULL,NULL,NULL,NULL,'jcozzoli@oldwestbury.edu',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
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

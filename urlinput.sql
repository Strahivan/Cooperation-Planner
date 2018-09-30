--
-- Table structure for table `url`
--
USE urlinput;
DROP TABLE IF EXISTS `url`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `url` (
  `index` bigint(20) AUTO_INCREMENT PRIMARY KEY,
  `url` text,
  `statuscode` bigint(20) DEFAULT NULL,
  `tld` text,
  `status` text,
  `inLink` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `url`
--

LOCK TABLES `url` WRITE;
/*!40000 ALTER TABLE `url` DISABLE KEYS */;
INSERT INTO `url` VALUES (0,'xing.rs',200,'.rs','okay',0),(1,'steveiva.com',400,'.com','okay',0);
/*!40000 ALTER TABLE `url` ENABLE KEYS */;
UNLOCK TABLES;
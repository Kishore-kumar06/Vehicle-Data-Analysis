CREATE DATABASE  IF NOT EXISTS `vehicle_expense_analytics` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `vehicle_expense_analytics`;
-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: vehicle_expense_analytics
-- ------------------------------------------------------
-- Server version	8.0.43

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
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_id` int NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `category` varchar(50) DEFAULT NULL,
  `is_fuel` bit(1) DEFAULT NULL,
  `is_service` bit(1) DEFAULT NULL,
  `modified_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Petrol','Fuel',_binary '',_binary '\0','2026-03-13 19:41:30'),(2,'Helmet','Safety Gear',_binary '\0',_binary '\0','2026-03-13 19:41:30'),(3,'Puncher','Service',_binary '\0',_binary '','2026-03-13 19:41:30'),(4,'General Service','Service',_binary '\0',_binary '','2026-03-13 19:41:30'),(5,'Icici Insurance','Motor Insurance',_binary '\0',_binary '\0','2026-03-13 19:41:30'),(6,'Polish','Maintenance',_binary '\0',_binary '\0','2026-03-13 19:41:30'),(7,'Water Wash','Maintenance',_binary '\0',_binary '','2026-03-13 19:41:30'),(8,'Air Filter','Accessories',_binary '\0',_binary '\0','2026-03-13 19:41:30'),(9,'Sparkplug','Accessories',_binary '\0',_binary '\0','2026-03-13 19:41:30'),(10,'Tyres','Accessories',_binary '\0',_binary '\0','2026-03-13 19:41:30'),(11,'Clutch Repair','Service',_binary '\0',_binary '','2026-03-13 19:41:30'),(12,'Helmet Cap','Accessories',_binary '\0',_binary '\0','2026-03-13 19:41:30'),(13,'Battery','Accessories',_binary '\0',_binary '\0','2026-03-13 19:41:30'),(14,'Battery Recharge','Service',_binary '\0',_binary '','2026-03-13 19:41:30'),(15,'One Way Bolt','Accessories',_binary '\0',_binary '\0','2026-03-13 19:41:30'),(16,'Break Pads','Accessories',_binary '\0',_binary '\0','2026-03-13 19:41:30');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-13 20:11:06

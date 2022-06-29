CREATE DATABASE  IF NOT EXISTS `libmanager` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `libmanager`;
-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: libmanager
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `loaisach`
--

DROP TABLE IF EXISTS `loaisach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loaisach` (
  `id_loaisach` int(11) NOT NULL AUTO_INCREMENT,
  `Ten_loai` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_loaisach`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaisach`
--

LOCK TABLES `loaisach` WRITE;
/*!40000 ALTER TABLE `loaisach` DISABLE KEYS */;
INSERT INTO `loaisach` VALUES (1,'Lập trình'),(2,'Truyện tranh'),(3,'Toán học'),(4,'Lịch sử'),(5,'Địa lý');
/*!40000 ALTER TABLE `loaisach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nhanvien`
--

DROP TABLE IF EXISTS `nhanvien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nhanvien` (
  `id_nhanvien` int(11) NOT NULL AUTO_INCREMENT,
  `Ho_va_ten` varchar(255) DEFAULT NULL,
  `taikhoan` varchar(255) DEFAULT NULL,
  `matkhau` varchar(255) DEFAULT NULL,
  `Role` varchar(255) DEFAULT 'Nhân viên',
  PRIMARY KEY (`id_nhanvien`),
  UNIQUE KEY `taikhoan` (`taikhoan`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhanvien`
--

LOCK TABLES `nhanvien` WRITE;
/*!40000 ALTER TABLE `nhanvien` DISABLE KEYS */;
INSERT INTO `nhanvien` VALUES (1,'NamQuanLy','admin','46f94c8de14fb36680850768ff1b7f2a','Quản lý'),(2,'Phương Nam','namshen','46f94c8de14fb36680850768ff1b7f2a','Nhân viên'),(3,'Nguyễn Phương Nam','phuongnam','46f94c8de14fb36680850768ff1b7f2a','Nhân viên');
/*!40000 ALTER TABLE `nhanvien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id_phieumuon` int(11) DEFAULT NULL,
  `id_sach` int(11) DEFAULT NULL,
  `id_orders` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_orders`),
  KEY `fk_orders_phieumuon` (`id_phieumuon`),
  KEY `fk_orders_sach` (`id_sach`),
  CONSTRAINT `fk_orders_phieumuon` FOREIGN KEY (`id_phieumuon`) REFERENCES `phieumuon` (`id_phieumuon`),
  CONSTRAINT `fk_orders_sach` FOREIGN KEY (`id_sach`) REFERENCES `sach` (`id_sach`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (22,1,1),(23,1,2),(23,2,3),(23,4,4),(23,3,5),(24,2,6),(24,1,7),(27,1,8),(27,3,9),(30,4,10),(30,3,11),(31,7,12),(32,1,13),(32,2,14),(32,3,15),(32,5,16),(33,6,17),(33,1,18),(34,1,19),(34,2,20),(34,3,21),(35,1,22),(35,3,23),(35,2,24);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieumuon`
--

DROP TABLE IF EXISTS `phieumuon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phieumuon` (
  `id_phieumuon` int(11) NOT NULL AUTO_INCREMENT,
  `id_thanhvien` int(11) DEFAULT NULL,
  `NgayMuon` date DEFAULT current_timestamp(),
  `TinhTrang` varchar(255) DEFAULT NULL,
  `id_nhanvien` int(11) DEFAULT NULL,
  `HanChot` date DEFAULT NULL,
  `TienCoc` int(11) DEFAULT NULL,
  `NgayTra` date DEFAULT NULL,
  `SoNgayQuaHan` int(11) DEFAULT NULL,
  `TienPhat` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_phieumuon`),
  KEY `fk_phieumuon_nhanvien` (`id_nhanvien`),
  KEY `fk_phieumuon_thanhvien` (`id_thanhvien`),
  CONSTRAINT `fk_phieumuon_nhanvien` FOREIGN KEY (`id_nhanvien`) REFERENCES `nhanvien` (`id_nhanvien`),
  CONSTRAINT `fk_phieumuon_thanhvien` FOREIGN KEY (`id_thanhvien`) REFERENCES `thanhvien` (`id_thanhvien`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieumuon`
--

LOCK TABLES `phieumuon` WRITE;
/*!40000 ALTER TABLE `phieumuon` DISABLE KEYS */;
INSERT INTO `phieumuon` VALUES (22,1,'2022-06-26','DM',1,'2022-09-24',30000,NULL,NULL,NULL),(23,3,'2022-06-26','DT',1,'2022-09-24',0,'2022-06-27',NULL,NULL),(24,4,'2022-06-26','DT',1,'2022-09-24',0,'2022-06-27',NULL,NULL),(27,4,'2022-06-26','DT',1,'2022-09-24',0,'2022-06-26',NULL,NULL),(30,1,'2022-06-26','DM',1,'2022-09-24',33000,NULL,NULL,NULL),(31,3,'2022-06-26','QH',1,'2022-01-01',0,'2022-06-27',177,88500),(32,7,'2022-06-27','DM',1,'2022-09-25',155000,NULL,NULL,NULL),(33,4,'2022-06-27','DM',2,'2022-09-25',130000,NULL,NULL,NULL),(34,4,'2022-06-27','DT',1,'2022-09-25',0,'2022-06-27',NULL,NULL),(35,4,'2022-06-27','DM',1,'2022-09-25',85000,NULL,NULL,NULL);
/*!40000 ALTER TABLE `phieumuon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sach`
--

DROP TABLE IF EXISTS `sach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sach` (
  `id_sach` int(11) NOT NULL AUTO_INCREMENT,
  `Ten_sach` varchar(255) DEFAULT NULL,
  `giatri` int(11) DEFAULT NULL,
  `id_loaisach` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_sach`),
  KEY `fk_SachLoaisach` (`id_loaisach`),
  CONSTRAINT `fk_SachLoaisach` FOREIGN KEY (`id_loaisach`) REFERENCES `loaisach` (`id_loaisach`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sach`
--

LOCK TABLES `sach` WRITE;
/*!40000 ALTER TABLE `sach` DISABLE KEYS */;
INSERT INTO `sach` VALUES (1,'Giải tích',30000,3),(2,'Đại số',40000,3),(3,'Doraemon',15000,2),(4,'Shin cậu bé bút chì',18000,2),(5,'Lập trình Python',70000,1),(6,'Lịch sử dân tộc Việt Nam',100000,4),(7,'Atlas',10000,5),(8,'Anh hùng bàn phím',50000,1),(10,'Lập trình cho trẻ em',50000,1);
/*!40000 ALTER TABLE `sach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thanhvien`
--

DROP TABLE IF EXISTS `thanhvien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `thanhvien` (
  `id_thanhvien` int(11) NOT NULL AUTO_INCREMENT,
  `Ho_va_ten` varchar(255) DEFAULT NULL,
  `Namsinh` date DEFAULT NULL,
  `Phone` varchar(255) DEFAULT NULL,
  `Dia_chi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_thanhvien`),
  UNIQUE KEY `Phone` (`Phone`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thanhvien`
--

LOCK TABLES `thanhvien` WRITE;
/*!40000 ALTER TABLE `thanhvien` DISABLE KEYS */;
INSERT INTO `thanhvien` VALUES (1,'Lương Minh Hoàng','1999-10-30','0123456789','Hà Nội'),(3,'Tiến Nổ',NULL,'0123123123','Hà Nội'),(4,'Hoàng Văn Quốc Thịnh',NULL,'0456456456','Hà Nội'),(5,'Dương Văn Quang',NULL,'0789789789','Hà Nội'),(6,'Nguyễn Văn A','1999-01-01','0912345612','Mỹ Tho'),(7,'Nguyễn Văn B','2000-01-01','0123321123','Hà Tây'),(8,'Nguyễn Văn C','2001-01-01','0111222333','Phú Quốc'),(9,'test','2000-02-03','0999','VN'),(10,'abc','1999-01-01','123123123','');
/*!40000 ALTER TABLE `thanhvien` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-29 20:06:37

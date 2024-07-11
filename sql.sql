/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - gym_management
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`gym_management` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `gym_management`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=97 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add batches',7,'add_batches'),
(26,'Can change batches',7,'change_batches'),
(27,'Can delete batches',7,'delete_batches'),
(28,'Can view batches',7,'view_batches'),
(29,'Can add equipment',8,'add_equipment'),
(30,'Can change equipment',8,'change_equipment'),
(31,'Can delete equipment',8,'delete_equipment'),
(32,'Can view equipment',8,'view_equipment'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add physician',10,'add_physician'),
(38,'Can change physician',10,'change_physician'),
(39,'Can delete physician',10,'delete_physician'),
(40,'Can view physician',10,'view_physician'),
(41,'Can add product',11,'add_product'),
(42,'Can change product',11,'change_product'),
(43,'Can delete product',11,'delete_product'),
(44,'Can view product',11,'view_product'),
(45,'Can add users',12,'add_users'),
(46,'Can change users',12,'change_users'),
(47,'Can delete users',12,'delete_users'),
(48,'Can view users',12,'view_users'),
(49,'Can add workout',13,'add_workout'),
(50,'Can change workout',13,'change_workout'),
(51,'Can delete workout',13,'delete_workout'),
(52,'Can view workout',13,'view_workout'),
(53,'Can add user_workouts',14,'add_user_workouts'),
(54,'Can change user_workouts',14,'change_user_workouts'),
(55,'Can delete user_workouts',14,'delete_user_workouts'),
(56,'Can view user_workouts',14,'view_user_workouts'),
(57,'Can add user_diets',15,'add_user_diets'),
(58,'Can change user_diets',15,'change_user_diets'),
(59,'Can delete user_diets',15,'delete_user_diets'),
(60,'Can view user_diets',15,'view_user_diets'),
(61,'Can add subscription',16,'add_subscription'),
(62,'Can change subscription',16,'change_subscription'),
(63,'Can delete subscription',16,'delete_subscription'),
(64,'Can view subscription',16,'view_subscription'),
(65,'Can add shop',17,'add_shop'),
(66,'Can change shop',17,'change_shop'),
(67,'Can delete shop',17,'delete_shop'),
(68,'Can view shop',17,'view_shop'),
(69,'Can add productbooking',18,'add_productbooking'),
(70,'Can change productbooking',18,'change_productbooking'),
(71,'Can delete productbooking',18,'delete_productbooking'),
(72,'Can view productbooking',18,'view_productbooking'),
(73,'Can add message',19,'add_message'),
(74,'Can change message',19,'change_message'),
(75,'Can delete message',19,'delete_message'),
(76,'Can view message',19,'view_message'),
(77,'Can add gym_instructor',20,'add_gym_instructor'),
(78,'Can change gym_instructor',20,'change_gym_instructor'),
(79,'Can delete gym_instructor',20,'delete_gym_instructor'),
(80,'Can view gym_instructor',20,'view_gym_instructor'),
(81,'Can add feedback',21,'add_feedback'),
(82,'Can change feedback',21,'change_feedback'),
(83,'Can delete feedback',21,'delete_feedback'),
(84,'Can view feedback',21,'view_feedback'),
(85,'Can add complaints',22,'add_complaints'),
(86,'Can change complaints',22,'change_complaints'),
(87,'Can delete complaints',22,'delete_complaints'),
(88,'Can view complaints',22,'view_complaints'),
(89,'Can add attendances',23,'add_attendances'),
(90,'Can change attendances',23,'change_attendances'),
(91,'Can delete attendances',23,'delete_attendances'),
(92,'Can view attendances',23,'view_attendances'),
(93,'Can add payments',24,'add_payments'),
(94,'Can change payments',24,'change_payments'),
(95,'Can delete payments',24,'delete_payments'),
(96,'Can view payments',24,'view_payments');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'gym','batches'),
(8,'gym','equipment'),
(9,'gym','login'),
(10,'gym','physician'),
(11,'gym','product'),
(12,'gym','users'),
(13,'gym','workout'),
(14,'gym','user_workouts'),
(15,'gym','user_diets'),
(16,'gym','subscription'),
(17,'gym','shop'),
(18,'gym','productbooking'),
(19,'gym','message'),
(20,'gym','gym_instructor'),
(21,'gym','feedback'),
(22,'gym','complaints'),
(23,'gym','attendances'),
(24,'gym','payments');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-06-26 10:20:34.794460'),
(2,'auth','0001_initial','2023-06-26 10:20:35.248227'),
(3,'admin','0001_initial','2023-06-26 10:20:35.375885'),
(4,'admin','0002_logentry_remove_auto_add','2023-06-26 10:20:35.385858'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-06-26 10:20:35.393838'),
(6,'contenttypes','0002_remove_content_type_name','2023-06-26 10:20:35.457666'),
(7,'auth','0002_alter_permission_name_max_length','2023-06-26 10:20:35.492574'),
(8,'auth','0003_alter_user_email_max_length','2023-06-26 10:20:35.526483'),
(9,'auth','0004_alter_user_username_opts','2023-06-26 10:20:35.536455'),
(10,'auth','0005_alter_user_last_login_null','2023-06-26 10:20:35.569373'),
(11,'auth','0006_require_contenttypes_0002','2023-06-26 10:20:35.572360'),
(12,'auth','0007_alter_validators_add_error_messages','2023-06-26 10:20:35.581338'),
(13,'auth','0008_alter_user_username_max_length','2023-06-26 10:20:35.616242'),
(14,'auth','0009_alter_user_last_name_max_length','2023-06-26 10:20:35.647160'),
(15,'auth','0010_alter_group_name_max_length','2023-06-26 10:20:35.683063'),
(16,'auth','0011_update_proxy_permissions','2023-06-26 10:20:35.693036'),
(17,'auth','0012_alter_user_first_name_max_length','2023-06-26 10:20:35.724952'),
(18,'gym','0001_initial','2023-06-26 10:20:36.876869'),
(19,'sessions','0001_initial','2023-06-26 10:20:36.928732'),
(20,'gym','0002_payments','2023-06-27 03:02:53.889499'),
(21,'gym','0003_remove_batches_first_name','2023-06-27 03:07:16.149462'),
(22,'gym','0004_alter_workout_equipment','2023-06-27 05:32:23.177987');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('7460a6fg5mbpcwqg4sezwkf7q9z3z6gt','eyJsaWQiOjQsInVpZCI6MX0:1qE15k:RmFnKM-6xisav6iVHtPnvsHckLeDQlXIGTw08zEDq74','2023-07-11 05:18:16.485304'),
('5fkv3v7d5f8kkvneujjnin4doh025s5y','eyJsaWQiOjl9:1qKALm:TZPU2Ma9tMgUY0ivRmA2Ah6gHEuRGh6BPwKezp0T7I0','2023-07-28 04:24:14.243277'),
('hv1bix9j0bwp7q3f94zwbl15wvdjygt3','eyJsaWQiOjExLCJ1aWQiOjF9:1qMNDi:HH4QwqKDMMByfMo8OMNcjMxGKe8MiahxbNgaBeNCFhY','2023-08-03 06:33:02.923177');

/*Table structure for table `gym_attendances` */

DROP TABLE IF EXISTS `gym_attendances`;

CREATE TABLE `gym_attendances` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` varchar(225) NOT NULL,
  `payment_for` varchar(225) NOT NULL,
  `payment_date` varchar(225) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`attendance_id`),
  KEY `gym_attendances_user_id_a1447307` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `gym_attendances` */

/*Table structure for table `gym_batches` */

DROP TABLE IF EXISTS `gym_batches`;

CREATE TABLE `gym_batches` (
  `batch_id` int(11) NOT NULL AUTO_INCREMENT,
  `batch_name` varchar(225) NOT NULL,
  `start_time` varchar(225) NOT NULL,
  `end_time` varchar(225) NOT NULL,
  `instructor_id` int(11) NOT NULL,
  PRIMARY KEY (`batch_id`),
  KEY `gym_batches_instructor_id_063da072` (`instructor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `gym_batches` */

insert  into `gym_batches`(`batch_id`,`batch_name`,`start_time`,`end_time`,`instructor_id`) values 
(1,'drfvrsdffv','22:22','22',1),
(2,'sdvsdgbvdfsgb','2323e2','32e3e',1);

/*Table structure for table `gym_complaints` */

DROP TABLE IF EXISTS `gym_complaints`;

CREATE TABLE `gym_complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(225) NOT NULL,
  `reply` varchar(225) NOT NULL,
  `complaint_date` varchar(225) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`complaint_id`),
  KEY `gym_complaints_user_id_9afb480e` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `gym_complaints` */

/*Table structure for table `gym_equipment` */

DROP TABLE IF EXISTS `gym_equipment`;

CREATE TABLE `gym_equipment` (
  `equipment_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(225) NOT NULL,
  `description` varchar(225) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`equipment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `gym_equipment` */

insert  into `gym_equipment`(`equipment_id`,`name`,`description`,`image`) values 
(1,'dcvdxc','xdwsxdwsx','WIN_20221228_13_27_47_Pro.jpg'),
(2,'sxdasxc','saxdAXC','R.jpg');

/*Table structure for table `gym_feedback` */

DROP TABLE IF EXISTS `gym_feedback`;

CREATE TABLE `gym_feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback_desc` varchar(225) NOT NULL,
  `feedback_reply` varchar(225) NOT NULL,
  `feedback_date` varchar(225) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`feedback_id`),
  KEY `gym_feedback_user_id_ce106695` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `gym_feedback` */

insert  into `gym_feedback`(`feedback_id`,`feedback_desc`,`feedback_reply`,`feedback_date`,`user_id`) values 
(1,'kjdshncjknsdjkcnksdn','pending','2023-07-20 07:21:49.393667+00:00',1);

/*Table structure for table `gym_gym_instructor` */

DROP TABLE IF EXISTS `gym_gym_instructor`;

CREATE TABLE `gym_gym_instructor` (
  `instructor_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `age` varchar(225) NOT NULL,
  `gender` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `login_id` int(11) NOT NULL,
  PRIMARY KEY (`instructor_id`),
  KEY `gym_gym_instructor_login_id_10b4c637` (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `gym_gym_instructor` */

insert  into `gym_gym_instructor`(`instructor_id`,`first_name`,`last_name`,`age`,`gender`,`phone`,`email`,`login_id`) values 
(1,'adaaaa','ad','11','male','06464654455','shijo96john@gmail.com',4);

/*Table structure for table `gym_login` */

DROP TABLE IF EXISTS `gym_login`;

CREATE TABLE `gym_login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `usertype` varchar(225) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `gym_login` */

insert  into `gym_login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','12345678','admin'),
(2,'asda','111133333','employee'),
(3,'www','11111111','employee'),
(4,'da','22222222','employee'),
(5,'sdvsdvsdvsdvs','4444444444444444','employee'),
(6,'3w3e3ed','1111111222','physician'),
(7,'1qaqa','11111111111111','physician'),
(8,'user','user','user'),
(9,'user','12345678','user'),
(10,'xsaxc','111111111','user'),
(11,'xsx','scxscscscscs','user');

/*Table structure for table `gym_message` */

DROP TABLE IF EXISTS `gym_message`;

CREATE TABLE `gym_message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `message_description` varchar(225) NOT NULL,
  `message_reply` varchar(225) NOT NULL,
  `message_date` varchar(225) NOT NULL,
  `physician_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`message_id`),
  KEY `gym_message_physician_id_de1a20db` (`physician_id`),
  KEY `gym_message_user_id_39b890ae` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `gym_message` */

insert  into `gym_message`(`message_id`,`message_description`,`message_reply`,`message_date`,`physician_id`,`user_id`) values 
(1,'cdsacsdac','pending','2023-07-20 07:10:06.184307+00:00',2,1),
(2,'ecfedc','pending','2023-07-20 07:11:06.280629+00:00',2,1),
(3,'swdcsc','pending','2023-07-20 07:11:44.241887+00:00',2,1),
(4,'edfvedvfsv','pending','2023-07-20 07:11:51.248155+00:00',2,1),
(5,'edfvedvfsv','pending','2023-07-20 07:11:55.598522+00:00',2,1);

/*Table structure for table `gym_payments` */

DROP TABLE IF EXISTS `gym_payments`;

CREATE TABLE `gym_payments` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` varchar(225) NOT NULL,
  `payment_for` varchar(225) NOT NULL,
  `payment_date` varchar(225) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `gym_payments_user_id_671313d3` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `gym_payments` */

insert  into `gym_payments`(`payment_id`,`amount`,`payment_for`,`payment_date`,`user_id`) values 
(1,'5000/-','subscription','2023-07-20 06:52:39.460165+00:00',1);

/*Table structure for table `gym_physician` */

DROP TABLE IF EXISTS `gym_physician`;

CREATE TABLE `gym_physician` (
  `physician_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `qualification` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `login_id` int(11) NOT NULL,
  PRIMARY KEY (`physician_id`),
  KEY `gym_physician_login_id_2f683b3c` (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `gym_physician` */

insert  into `gym_physician`(`physician_id`,`first_name`,`last_name`,`qualification`,`phone`,`email`,`login_id`) values 
(2,'dsfs','sdfvdsfv','dsf','edfvsgvf','vsdv',4);

/*Table structure for table `gym_product` */

DROP TABLE IF EXISTS `gym_product`;

CREATE TABLE `gym_product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(225) NOT NULL,
  `amount` varchar(225) NOT NULL,
  `shop_id` int(11) NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `gym_product_shop_id_abcb3e52` (`shop_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `gym_product` */

/*Table structure for table `gym_productbooking` */

DROP TABLE IF EXISTS `gym_productbooking`;

CREATE TABLE `gym_productbooking` (
  `productbooking_id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`productbooking_id`),
  KEY `gym_productbooking_product_id_60dd9f27` (`product_id`),
  KEY `gym_productbooking_user_id_6143eff9` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `gym_productbooking` */

/*Table structure for table `gym_shop` */

DROP TABLE IF EXISTS `gym_shop`;

CREATE TABLE `gym_shop` (
  `shop_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `login_id` int(11) NOT NULL,
  PRIMARY KEY (`shop_id`),
  KEY `gym_shop_login_id_a5b0990e` (`login_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `gym_shop` */

/*Table structure for table `gym_subscription` */

DROP TABLE IF EXISTS `gym_subscription`;

CREATE TABLE `gym_subscription` (
  `subscription_id` int(11) NOT NULL AUTO_INCREMENT,
  `physician_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`subscription_id`),
  KEY `gym_subscription_physician_id_92a8bb97` (`physician_id`),
  KEY `gym_subscription_user_id_ff7f5717` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `gym_subscription` */

insert  into `gym_subscription`(`subscription_id`,`physician_id`,`user_id`) values 
(1,2,1);

/*Table structure for table `gym_user_diets` */

DROP TABLE IF EXISTS `gym_user_diets`;

CREATE TABLE `gym_user_diets` (
  `user_diets_id` int(11) NOT NULL AUTO_INCREMENT,
  `diet_details` varchar(225) NOT NULL,
  `diet_date` varchar(225) NOT NULL,
  `physician_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`user_diets_id`),
  KEY `gym_user_diets_physician_id_51a741e0` (`physician_id`),
  KEY `gym_user_diets_user_id_490c43ef` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `gym_user_diets` */

insert  into `gym_user_diets`(`user_diets_id`,`diet_details`,`diet_date`,`physician_id`,`user_id`) values 
(1,'sacsacs','ascasc',2,1);

/*Table structure for table `gym_user_workouts` */

DROP TABLE IF EXISTS `gym_user_workouts`;

CREATE TABLE `gym_user_workouts` (
  `user_workout_id` int(11) NOT NULL AUTO_INCREMENT,
  `day` varchar(225) NOT NULL,
  `duration` varchar(225) NOT NULL,
  `user_id` int(11) NOT NULL,
  `workout_id` int(11) NOT NULL,
  PRIMARY KEY (`user_workout_id`),
  KEY `gym_user_workouts_user_id_5e5c6b2a` (`user_id`),
  KEY `gym_user_workouts_workout_id_d2c3b055` (`workout_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `gym_user_workouts` */

/*Table structure for table `gym_users` */

DROP TABLE IF EXISTS `gym_users`;

CREATE TABLE `gym_users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `age` varchar(225) NOT NULL,
  `gender` varchar(225) NOT NULL,
  `weight` varchar(225) NOT NULL,
  `height` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `payment_status` varchar(225) NOT NULL,
  `batch_id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `gym_users_batch_id_55a1fb0b` (`batch_id`),
  KEY `gym_users_login_id_0b98e788` (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `gym_users` */

insert  into `gym_users`(`user_id`,`first_name`,`last_name`,`age`,`gender`,`weight`,`height`,`phone`,`email`,`payment_status`,`batch_id`,`login_id`) values 
(1,'ronald','jose','11','male','80','6.5','07356456811','rono@gmail.com','pending',2,11);

/*Table structure for table `gym_workout` */

DROP TABLE IF EXISTS `gym_workout`;

CREATE TABLE `gym_workout` (
  `workout_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(225) NOT NULL,
  `description` varchar(225) NOT NULL,
  `benefits` varchar(225) NOT NULL,
  `equipment_id` int(11) NOT NULL,
  PRIMARY KEY (`workout_id`),
  KEY `gym_workout_equipment_id_4082a8be` (`equipment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `gym_workout` */

insert  into `gym_workout`(`workout_id`,`title`,`description`,`benefits`,`equipment_id`) values 
(1,'awdsadfcsaedsaecdsdc','awdcwadcfawdfawdfaedc','axasx',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

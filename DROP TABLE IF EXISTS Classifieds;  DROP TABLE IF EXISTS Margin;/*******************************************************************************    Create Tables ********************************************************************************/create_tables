DROP TABLE IF EXISTS Classifieds;

DROP TABLE IF EXISTS Margin;


/*******************************************************************************
   Create Tables
********************************************************************************/

CREATE TABLE `Classifieds` (
  `id` varchar(255) NOT NULL,
  `customer_id` varchar(255) NOT NULL,
  `created_at` varchar(255) NOT NULL,
  `text` varchar(255) NOT NULL,
  `ad_type` varchar(10) NOT NULL,
  `price` float DEFAULT NULL,
  `currency` varchar(20) DEFAULT NULL,
  `payment_type` varchar(10) DEFAULT NULL,
  `payment_cost` float DEFAULT NULL,
  `offset` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Margin` (
  `id` bigint(100) NOT NULL AUTO_INCREMENT,
  `ad_type` varchar(20) NOT NULL,
  `payment_type` varchar(20) DEFAULT NULL,
  `margin` float DEFAULT NULL,
  `date_calculated` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=911 DEFAULT CHARSET=latin1;


CREATE TABLE `amon` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `peer` varchar(10) COLLATE utf8_bin NOT NULL,
  `state` tinyint(1) NOT NULL,
  `ping` int(11) NOT NULL,
  `ip` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_bin


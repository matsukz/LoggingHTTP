CREATE TABLE `XserverVPS` (
    `id` bigint unsigned NOT NULL AUTO_INCREMENT,
    `date` datetime NOT NULL DEFAULT '1000-01-01 00:00:00',
    `response_code` int NOT NULL DEFAULT 0,
    `response_time` double NOT NULL DEFAULT 0,
    PRIMARY KEY (`id`) 
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;
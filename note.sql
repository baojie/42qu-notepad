DROP DATABASE IF EXISTS `work_notepad`;
CREATE DATABASE IF NOT EXISTS `work_notepad`;
DROP TABLE IF EXISTS `work_notepad`.`account`;
CREATE TABLE  `work_notepad`.`account` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) COLLATE utf8_bin NOT NULL,
  `email` varchar(128) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
DROP TABLE IF EXISTS `work_notepad`.`user_note`;
CREATE TABLE  `work_notepad`.`user_note` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `url_id` bigint(20) unsigned NOT NULL,
  `view_time` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id-url_id` (`user_id`,`url_id`),
  UNIQUE KEY `url_id` (`url_id`),
  KEY `user_id-view_time` (`user_id`,`view_time`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
DROP TABLE IF EXISTS `work_notepad`.`url`;
CREATE TABLE  `work_notepad`.`url` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `url` varbinary(512) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
DROP TABLE IF EXISTS `work_notepad`.`txt_log`;
CREATE TABLE  `work_notepad`.`txt_log` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `url_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  `time` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `url_id-time` (`url_id`,`time`)
  KEY `user_id-time` (`user_id`,`time`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

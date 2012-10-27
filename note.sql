DROP DATABASE IF EXISTS `work_notepad`;
CREATE DATABASE work_notepad;
DROP TABLE IF EXISTS `work_notepad`.`notepad`;
CREATE TABLE  `work_notepad`.`notepad` (
  `url` char(9) COLLATE utf8_bin NOT NULL,
  `txt` mediumtext COLLATE utf8_bin NOT NULL,
  `time` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`url`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

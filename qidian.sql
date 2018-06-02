USE qidian;
-- auto-generated definition
CREATE TABLE novel_info
(
  id                   INT AUTO_INCREMENT
    PRIMARY KEY,
  novel_id             INT         NOT NULL,
  novel_name           VARCHAR(20) NULL,
  novel_author         VARCHAR(20) NULL,
  novel_author_id      INT         NOT NULL,
  novel_link           VARCHAR(50) NULL,
  novel_score          FLOAT       NULL,
  novel_intro          TEXT        NULL,
  novel_big_category   VARCHAR(10) NULL,
  novel_small_category VARCHAR(10) NULL,
  novel_status         VARCHAR(10) NULL,
  novel_read_link      TEXT        NOT NULL,
  novel_total_chapter  INT         NULL,
  CONSTRAINT novel_info_id_uindex
  UNIQUE (id),
  CONSTRAINT novel_info_novel_id_uindex
  UNIQUE (novel_id)
);



-- auto-generated definition
CREATE TABLE chapter_info
(
  id                 INT(30) AUTO_INCREMENT
    PRIMARY KEY,
  novel_id           INT(30)     NOT NULL,
  chapter_volumeId   INT(30)     NULL,
  chapter_ccid       TEXT        NULL,
  chapter_id         INT(30)     NOT NULL,
  chapter_name       VARCHAR(50) NULL,
  chapter_content    LONGTEXT    NULL,
  chapter_wordsCount INT         NULL,
  chapter_freeStatus INT         NULL,
  chapter_vipStatus  INT         NULL,
  chapter_pubdate    VARCHAR(20) NOT NULL,
  CONSTRAINT chapter_info_id_uindex
  UNIQUE (id),
  CONSTRAINT chapter_info_chapter_id_uindex
  UNIQUE (chapter_id)
);


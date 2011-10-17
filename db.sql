DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
    `id` int auto_increment,
    `l_name` varchar(100),
    `f_name` varchar(100),
    `s_name` varchar(100),
    PRIMARY KEY(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `labs`;
CREATE TABLE `labs` (
    `id` int auto_increment,
    `name` varchar(255),
    `pos` int,
    PRIMARY KEY(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `mark`;
CREATE TABLE `mark` (
    `id` int auto_increment,
    `mark` int,
    `mark_date` date,
    `id_lab` int,
    `id_stud` int,
    PRIMARY KEY(`id`),
    CONSTRAINT `stud`
        FOREIGN KEY (`id_stud`)
        REFERENCES `students` (`id`)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,
    CONSTRAINT `lab`
        FOREIGN KEY (`id_lab`)
        REFERENCES `labs` (`id`)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `students` VALUES
(null, 'Безручкин', 'Евгений', 'Геннадьевич'),
(null, 'Букин', 'Максим', 'Николаевич'),
(null, 'Верещагина', 'Александра', 'Владимировна'),
(null, 'Демидова', 'Анастасия', 'Александровна'),
(null, 'Егоров', 'Константин', 'Сергеевич');

INSERT INTO `labs` VALUES
(null, 'ЛР1. Создание и удаление таблиц и БД', 1),
(null, 'ЛР2. Редактирование данных в таблице', 2),
(null, 'ЛР3. Выбор и сортировка данных', 3),
(null, 'ЛР4. Извлечение данных из нескольких таблиц', 4),
(null, 'ЛР5. Извлечение данных из нескольких таблиц 2.', 5),
(null, 'ЛР6. Группировка и агрегирование данных', 6),
(null, 'ЛР7. Использование подзапросов', 7),
(null, 'ЛР8. Изменение структуры таблицы', 8);


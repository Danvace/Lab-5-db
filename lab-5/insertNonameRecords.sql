# вставка 10 елементів noname в таблицю review
DELIMITER //

CREATE PROCEDURE InsertNonameRecords(IN product_id1 int)
BEGIN
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 10
        DO
            INSERT INTO review (product_id, response) VALUES (product_id1, CONCAT('Noname', counter));
            SET counter = counter + 1;
        END WHILE;
END //

DELIMITER ;
call InsertNonameRecords(5);
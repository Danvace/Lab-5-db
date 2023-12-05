DELIMITER //
CREATE PROCEDURE ProcCurso()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE responseT VARCHAR(500);
    DECLARE cur CURSOR FOR SELECT response FROM review;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN cur;
    read_loop:
    LOOP
        FETCH cur INTO responseT;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET @query = CONCAT('CREATE DATABASE ', responseT);
        PREPARE myquery FROM @query;
        EXECUTE myquery;
        DEALLOCATE PREPARE myquery;
    END LOOP;
    CLOSE cur;
END //
DELIMITER ;

CALL ProcCurso();
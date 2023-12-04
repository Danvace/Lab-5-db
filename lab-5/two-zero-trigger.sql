DELIMITER //
CREATE TRIGGER check_value_trigger
    BEFORE INSERT
    ON review
    FOR EACH ROW
BEGIN
    DECLARE value_suffix VARCHAR(2);

    SET value_suffix = RIGHT(NEW.response, 2);

    IF value_suffix = '00' THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Значення стовпця не може закінчуватися двома нулями';
    END IF;
END;
//
DELIMITER ;

INSERT INTO review (product_id, response)
VALUES (4, '100s');



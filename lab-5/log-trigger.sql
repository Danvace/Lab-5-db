CREATE TABLE IF NOT EXISTS deleted_logs
(
    id           INT AUTO_INCREMENT PRIMARY KEY,
    deleted_data VARCHAR(1000),
    deleted_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //
CREATE TRIGGER deleteLogTrigger
    BEFORE DELETE
    ON review
    FOR EACH ROW
BEGIN
    INSERT INTO deleted_logs (deleted_data)
    VALUES (CONCAT('response:', OLD.response,', product_id:', OLD.product_id));
END;
//
DELIMITER ;

DELETE FROM review WHERE id = 2;


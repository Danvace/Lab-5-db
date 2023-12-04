create table if not exists Review (
    id int primary key auto_increment,
    response varchar(255),
    product_id int
);

CREATE TRIGGER trg_insert_review
BEFORE INSERT ON Review
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT id FROM Product WHERE Product.id = NEW.product_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Невірний батьківський запис в review';
    END IF;
END;

CREATE TRIGGER trg_update_review
BEFORE UPDATE ON Review
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT id FROM Product WHERE Product.id = NEW.product_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Невірний батьківський запис в review';
    END IF;
END;

CREATE TRIGGER trg_delete_review
BEFORE DELETE ON Product
    FOR EACH ROW
    BEGIN
        DELETE FROM Review where product_id = OLD.id;
    END;

insert into Review (response, product_id) values ('good', 4);


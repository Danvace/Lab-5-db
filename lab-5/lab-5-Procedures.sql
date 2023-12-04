DElIMITER //
create procedure review_insert(
    IN p_product_id int,
    IN p_response varchar(255)
)
begin
    insert into Review (response, product_id)
    values (p_response, p_product_id);
end //

DELIMITER ;

call review_insert(5, 'This is a review');


CREATE PROCEDURE InsertOrderProductMapping(IN order_id1 INT, IN product_id1 INT)
BEGIN
    INSERT INTO order_has_product (order_id, product_id) VALUES (order_id1, product_id1);
END;

CALL InsertOrderProductMapping(3, 1);




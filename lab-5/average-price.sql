# середнє значення ціни
DELIMITER //
CREATE FUNCTION averagePrice()
    RETURNS DECIMAL(10, 2)
    DETERMINISTIC
    NO SQL
BEGIN
    DECLARE average DECIMAL(10, 2);
    SELECT AVG(price) INTO average FROM product;
    RETURN average;
END;
//

DELIMITER ;

create procedure showAveragePrice()
begin
    select averagePrice();
end;

call showAveragePrice();
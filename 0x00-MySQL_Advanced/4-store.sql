-- triger that reduces the number of items when a new order is added
DELIMITER $$ ;
CREATE
TRIGGER item_order_trigger AFTER INSERT
ON orders
FOR EACH ROW BEGIN
	UPDATE items SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name
END$$
DELIMITER ; $$

-- triger that reduces the number of items when a new order is adde
CREATE TRIGGER item_order_trigger AFTER INSERT
ON orders
FOR EACH ROW
	UPDATE items SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;

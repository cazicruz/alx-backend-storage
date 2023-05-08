-- checks if new email == old email if not resets the attr of valid email to 0
CREATE TRIGGER EMAIL_VALIDATION BEFORE UPDATE
ON users 
FOR EACH ROW 
	IF NEW.email <> old.email
		SET new.valid_email = 0;

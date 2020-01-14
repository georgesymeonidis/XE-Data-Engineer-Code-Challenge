CREATE EVENT hourly_margin_calculation
	ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
	DO
	CALL `gsdataengineer`.`calculate_margin_hourly_procedure`();

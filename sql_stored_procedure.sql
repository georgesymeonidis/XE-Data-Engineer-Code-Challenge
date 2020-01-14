CREATE DEFINER=`root`@`%` PROCEDURE `calculate_margin_hourly_procedure`()
BEGIN
	INSERT INTO Margin
	   (ad_type, payment_type, margin, date_calculated)
	  SELECT ad_type, payment_type, (CASE WHEN ad_type = 'Platinum' || ad_type = "Premium" THEN
		SUM(price - payment_cost)
		ELSE 
		NULL END
		) as margin,
        DATE_FORMAT(NOW(), '%Y-%m-%d %h:00:00') as date_calculated
	  FROM   gsdataengineer.Classifieds GROUP BY 1,2,4;
END

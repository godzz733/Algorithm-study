SELECT * FROM FOOD_PRODUCT AS F WHERE F.PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT); 
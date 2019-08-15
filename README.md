EndPoints information:

## For the PURCHASES layout:

1. Add new `record` on purchases layout
To add a new product and at the same time to add the quantity of the purchase use 
The same EndPoint:
```md
	Method: POST
	/purchases/add
```
2. Remove `record` on purchases layout
To add a new product and at the same time to add the quantity of the purchase use 
The same EndPoint:
```md	
	Method: DELETE
	/purchases/remove/purchases:id
```
3. Create a `product` / Add `product` quantity
To add a new product and at the same time to add the quantity of the purchase use 
The same EndPoint:
```md
	Method: POST
	/products/purchases/add
```
4. Remove `product` quantity
To remove a product of the sale table use The EndPoint:
```md	
	Method: DELETE
	/products/purchases/remove/remove:id
```
## For the SALES layout:

6. Add new `record` on sales layout
To add a new product and at the same time to add the quantity of the sale use 
The same EndPoint:
```md	
	Method: POST
	/sales/add
```
7. Remove `record` on sales layout
To add a new product and at the same time to add the quantity of the sale use 
The same EndPoint:
```md	
	Method: DELETE
	/sales/remove/remove:id
```
8. Make a SALE
To add a new `product` and at the same time to add the quantity of the sale use 
This EndPoint:
```md
	Method: POST
	/products/sales/add
```
9. Remove `product` quantity
To remove a product of the sale table use The same EndPoint:
```md	
	Method: DELETE
	/products/sale/remove/remove:id
```

## For the INVENTORY layout:

10. To get all the `products`
To remove a product of the sale table use The same EndPoint:
```md	
	Method: GET
	/products/all
```

## For the DELIVERY layout:

11. To get all the `warehouses` (motorcycles)
To remove a product of the sale table use The same EndPoint:
```md	
	Method: GET
	/warehouses/all
```
12. To get a particular `warehouse`
To remove a product of the sale table use The same EndPoint:
```md	
	Method: GET
	/warehouses/warehouse:id
```
## For the CUSTOMER layout:

11. To get the `user` and it's related order:
```md	
	Method: GET
	/user/user:id
```
12. To get the `map`: 
```md	
	Method: GET
	/warehouses/warehouse:id/map
```

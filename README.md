# EndPoints:

```md
	•	/transactions/new
	•	/purchases/all
	•	/products/all
	•	/sales/all
```

## INVENTORY `PRODUCTS` TABLE:

### TO `ADD` A NEW RECORD FOR "PRODUCTS"

```md	
	Method: POST
	/products/all
```
- Body must contain the following:

```md	
	 {
  	 "item":"chocolate",
	 "description":"food",
	 "quantity":"7"
         }
```
- First Item Name, description
- Second you must put an initial quantity

### TO `GET ALL` RECORDS OF "TRANSACTIONS"

```md	
	Method: GET
	/transactions/new
```
- Retrieves all records on this table


## INVENTORY `IN` TABLE:

### TO `ADD` A NEW RECORD FOR "IN"

```md	
	Method: POST
	/purchases/all
```
- Adds a record with `id` and `Creation Date`
- To create a `Transaction IN` you must add a new record for IN


### TO `GET ALL` RECORDS OF "IN"

```md	
	Method: GET
	/purchases/all
```
- Retrieves all records on this table, including the related product


## INVENTORY `OUT` TABLE:

### TO `ADD` A NEW RECORD FOR "OUT"

```md	
	Method: POST
	/sales/all
```
- Adds a record with `id` and `Creation Date`
- To create a `Transaction OUT` you must add a new record for OUT


### TO `GET ALL` RECORDS OF "OUT"

```md	
	Method: GET
	/sales/all
```
- Retrieves all records on this table, including the related product


## INVENTORY `TRANSACTIONS` TABLE:

### TO `ADD` A NEW RECORD FOR "TRANSACTIONS" (CAN BE IN OR OUT)

```md	
	Method: POST
	/transactions/new
```
- Body must contain the following:

```md	
	{
	"products_id":3,
	"quantity":5,
	"sales_id":1,
	"purchases_id": null
	}
```
- First you should have a product with an initial quantity
- Second you must create a "IN" or "OUT" record
- If its IN you should set OUT to null, and viceversa

### TO `GET ALL` RECORDS OF "TRANSACTIONS"

```md	
	Method: GET
	/transactions/new
```
- Retrieves all records on this table




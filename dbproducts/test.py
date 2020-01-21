SELECT product_id, COUNT(product_id) AS results
FROM dbproducts_product_categories
INNER JOIN dbproducts_product
ON dbproducts_product_categories.product_id =
dbproducts_product.id
INNER JOIN dbproducts_category
ON dbproducts_product_categories.category_id =
dbproducts_category.id
WHERE dbproducts_product_categories.category_id IN (
SELECT dbproducts_product_categories.category_id FROM
dbproducts_product_categories WHERE
dbproducts_product_categories.product_id = 3095757370015)
AND dbproducts_product_categories.product_id != 3095757370015
GROUP BY dbproducts_product_categories.product_id
HAVING results >=1
ORDER BY results DESC;

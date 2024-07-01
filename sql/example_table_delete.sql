-- name: insert_example
DELETE FROM
	public.example_table
	WHERE int_field in :tuple:deleted_field_values
;

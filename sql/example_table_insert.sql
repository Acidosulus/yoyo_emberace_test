-- name: insert_example
INSERT INTO 
		public.example_table
			(    	int_field,
				    date_field,
				    string_field)
	 VALUES :tuple*:inserted_row
;

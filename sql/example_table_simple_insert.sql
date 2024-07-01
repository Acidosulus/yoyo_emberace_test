-- :resultset
INSERT INTO public.example_table(int_field,date_field,string_field) VALUES (:int_value,:date_value,:string_value);
commit;
CREATE OR REPLACE FUNCTION get_airport_info(airport_code_param bpchar)
RETURNS TABLE (
  airport_code bpchar,
  airport_name text,
  city text,
  longitude float8,
  latitude float8,
  timezone text
) AS $$
BEGIN
  RETURN QUERY
  SELECT
    a.airport_code,
    a.airport_name,
    a.city,
    a.longitude,
    a.latitude,
    a.timezone
  FROM
    bookings.airports a
  WHERE
    a.airport_code = airport_code_param;
END;
$$ LANGUAGE plpgsql;

GRANT EXECUTE ON FUNCTION bookings.get_airport_info(bpchar) TO web_anon;
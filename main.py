from dataclasses import dataclass
from datetime import datetime
import embrace
from embrace import mapobject
import psycopg2
from rich import print



@dataclass
class Aircraft:
    aircraft_code: str
    model: str
    range: int

@dataclass
class Flight:
	flight_id: int
	flight_no: str
	scheduled_departure: datetime
	scheduled_arrival: datetime
	departure_airport: str
	arrival_airport: str
	status: str
	aircraft_code: str
	actual_departure: datetime
	actual_arrival: datetime


conn = psycopg2.connect(
    dbname="demo",
    user="postgres",
    password="321",
    host="192.168.0.112"
)
queries = embrace.module("sql")



# -------------Маппинг в dataclass------------------------------------------------------------------------------
query = queries.query(
                    """
                      SELECT aircraft_code, model,"range" FROM bookings.aircrafts;
                    """).returning(Aircraft)
print([aircraft for aircraft in query.many(conn)])



# -------------Маппинг в несколько dataclass-ов результата джойна------------------------------------------------
query = queries.query(
    """
        SELECT aircrafts.*, flights.* 
            FROM bookings.flights as flights
            left join bookings.aircrafts as aircrafts on aircrafts.aircraft_code = flights.aircraft_code
            where aircrafts.aircraft_code = 'CN1'
            order by flight_id
            limit 5 offset 5
        ;
    """
)

#------------------попытка прикинуть время маппинга/фетчинга, чтобы оценить нужно удалить лимит в запросе--------
print('mapping')
map = query.returning(  (mapobject(Aircraft, split="aircraft_code"),
               mapobject(Flight,   split="flight_id")) )
print('fetching')
result = [(aircraft, flight) for aircraft, flight in map.many(conn)]
print('before print')
print(result)


#------------Вставка удаление одиночных записей------------------------------------------------------------------

queries.example_table_simple_insert(
                                    conn = conn,
                                    int_value = 1,
                                    date_value = datetime.now(),
                                    string_value = 'example string 1'
                                    )

query = queries.example_table_select(conn)
print('simle: after insert: ', [row for row in query.many()])

queries.example_table_simple_delete(
                                    conn = conn,
                                    int_value = 1
                                    )

query = queries.example_table_select(conn)
print('simple: after delete:', [row for row in query.many()])



#-----------Вставка удаление множества записей одной командой---------------------------------------
queries.example_table_insert(
                        conn = conn,
                        inserted_row = (
                                        (1, datetime.now(), 'example string 1'),
                                        (2, datetime.now(), 'example string 2'),
                                        (3, datetime.now(), 'example string 3')
                                        )
                        )


query = queries.example_table_select(conn)
print('many: after insert: ', [row for row in query.many()])

queries.example_table_delete(
                            conn = conn,
                            deleted_field_values = (1,2,3)
                            )

query = queries.example_table_select(conn)
print('many after delete:', [row for row in query.many()])


conn.close()




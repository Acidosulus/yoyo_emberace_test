import re

def convert_copy_to_insert(dump_file, output_file):
    with open(dump_file, 'r') as infile, open(output_file, 'w') as outfile:
        copy_mode = False
        table_name = ""
        columns = []

        for line in infile:
            if line.startswith("COPY"):
                copy_mode = True
                match = re.match(r'COPY (\w+) \(([^)]+)\) FROM stdin;', line)
                if match:
                    table_name = match.group(1)
                    columns = match.group(2).split(", ")
                continue
            
            if line.startswith("\\.") and copy_mode:
                copy_mode = False
                continue

            if copy_mode:
                values = line.strip().split("\t")
                values_escaped = ["'" + v.replace("'", "''") + "'" for v in values]
                insert_statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values_escaped)});\n"
                outfile.write(insert_statement)
            else:
                outfile.write(line)

convert_copy_to_insert(r'C:\Users\kazakovtsev_nm\Desktop\Experiment\migrations\20240628_01_92MO3-fill-data.sql',
                       r'C:\Users\kazakovtsev_nm\Desktop\Experiment\migrations\20240628_01_92MO3-fill-data.sqloutput_dump.sql')
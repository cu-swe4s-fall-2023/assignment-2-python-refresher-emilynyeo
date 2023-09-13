# get_column("Agrofood_co2_emission.csv",0,"South Africa",1)

def get_column(file_name, query_column, query_value, result_column):
    result_array = []
    
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            
            line_array = line.split(",") # Split the line into an array

            # Check if query_column value matches query_value
            if line_array[query_column] == query_value:
                result_array.append(line_array[result_column])
    
    return result_array


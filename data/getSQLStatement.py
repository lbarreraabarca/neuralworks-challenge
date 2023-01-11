import logging

def readFile(fileName: str) -> list:
    logging.info('Reading document {}'.format(fileName))
    with open(fileName) as f:
        lines = f.readlines()
    return lines

def writeFile(fileName: str, data: list) -> None:
    text_file = open(fileName, "wt")
    text_file.write('\n'.join(data))
    text_file.close()

data = readFile('data/trips.csv')

output = []
lineNumber = 1
for line in data:
    if lineNumber > 1:
        region = f"'{line.split(',')[0]}'"
        origin_coord = f"'{line.split(',')[1]}'"
        destination_coord = f"'{line.split(',')[2]}'"
        datetime = f"'{line.split(',')[3]}'"
        datasource = f"'{line.split(',')[4]}'".strip().replace('\n', '')
        statement = f"INSERT INTO challenge.trip_event values ({region}, {origin_coord}, {destination_coord}, {datetime}, {datasource});"
        output.append(statement)
    lineNumber += 1

writeFile('data/insert.sql', output)
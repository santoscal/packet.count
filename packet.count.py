import csv

# Open the CSV file in read mode
with open('packets.csv', 'r') as file:

    # Create a CSV reader object
    reader = csv.reader(file)

    # Initialize a counter variable
    packet_count = 0

    # Loop through each row in the CSV file
    for row in reader:

        # Increment the counter variable
        packet_count += 1

    # Print the total number of packets
    print("Total packets:", packet_count)

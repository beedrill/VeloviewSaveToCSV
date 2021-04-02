# Python processing script for VeloView
## save PCAT to point cloud CSVs
To save a recorded PCAP to CSV, do the following:
1. read pcap in Veloview
2. change the DATADIR in script **saveToCSV.py** to the directory you want, use __ABSOLUTE__ path, make sure the folder already exist.
3. make sure the Veloview animation progress bar is at the beginning of the animation 
4. after editting, save the script.
5. in Veloview, open python console and load the script **saveToCSV.py**

Each CSV name is using the point cloud's current timestamp
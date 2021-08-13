![alt text](https://go.redpitaya.com/hs-fs/hubfs/Red-pitaya-logo.jpg?width=850&name=Red-pitaya-logo.jpg)
# Red Pitaya TDMS Data Plotter
## Program Purpose
This program reads .tdms files (National Instruments file format) and plots the data that is recorded with the Red Pitaya Stream Server application.
The user has the option to display graphs together or separately, as well as save the images to the computer.
## Specifications/Limits
**The current minimum supported sampling frequency is 1.9 kHz.** Developers are working on updating the software to accomodate lower frequencies. The Red Pitaya has 2 fast analog inputs from which data can be recorded. Prior to recording the data, the user can specify if input 1, input 2, or both inputs are to be used for data acquisition. This means that a maximum of two graphs will be output. The program only works if the data is a .tdms file format, **no other file types are currently supported**.

## Instructions
1. Ensure a proper connection to the Red Pitaya. This can be done via by direct ethernet or utilizing the same network.
2. Type the Red Pitaya address into a search engine bar. The URL can be found on a label on the Red Pitaya's ethernet port.
3. Click the application labeled "Data Stream Control."
4. Select the "local file" setting* near the top of the GUI.
5. Enter the amount of samples and sampling rate in the appropriate boxes.
6. Edit other settings as necessary.
7. At the bottom, select ".tdms" for the file format setting.
8. Select "RUN" to start collecting.
9. When collection is finished, click "browse" to view the file selector and download.
10. Run the "data plotter.py" script and when prompted enter in necessary information.

## Upcoming Work
- Awaiting software fix for data stream control application
- Add option to save graphs as .PNG files
- Edit code to run faster

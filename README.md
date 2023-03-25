# FFXIV Submarine Salvaged Goods Calculator
**SubSalvageCalculator** is a lightweight python-based program that takes inputs from Final Fantasy XIV's loot-log to calculate the total value of salvaged goods. The program is meant to be utilized by users who wish to track or otherwise bookkeep earnings from each submarine, whether for the purpose of optimizing loot gains, logging Free Company gil income, or other potential uses. The backend logic is majority input cleaning, cutting out non-salvaged goods first before searching for the eight different potential salvaged goods. After finding hits under those criteria, the number next to each of the entries are extracted and stored for later computation. A final sum is then sent to the frontend to be printed. The frontend was made with the [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) library.



## Within the package
- A bundled version of CustomTkinter
- Source code for the logical and front end display compilation found in [subSumCalc.py](subSumCalc.py)
- A .txt file with a test input found in [entrytest.txt](entrytest.txt)

## Installation and Usage
1. Download the .zip release on the sidebar.
2. Run [subSumCalc.exe](subSumCalc.exe).
3. Copy the text output by FFXIV once you finalize a voyage.
4. Paste the output into the 'Paste chatlog here...' field.
5. Press 'Calculate raw gil'.
6. Read the program's output in the box below.

## Screenshots
![image](https://user-images.githubusercontent.com/98601809/227738591-8e44bd97-0cf8-4b2c-aa6d-df0fd758d29b.png)
![image](https://user-images.githubusercontent.com/98601809/227738595-4ef69767-ff5c-4a10-961a-788eb18de84d.png)

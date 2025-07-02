import os
folder=input("enter the folder to create")
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Fodler '{folder} 'created")
else:
    print("folder already exists")
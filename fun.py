from colors import bcolors
import glob, os


path = r'E:\BackHandData'
all_files = glob.glob(os.path.join(path, "*.csv"))
names = [os.path.basename(x).split('.')[-2] for x in all_files]

print()

def indexProz(id, strign):
    print("der körper is da")

    if id in strign:
        print(strign.index(id))

        print("yes der ist drin ")
        print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")




print(type(names[55]), "\n" , names[55])

indexProz(names[55], names[55])

#...
progress = -1
for i in range(2, len(names) + 1):
    current_progress = int(100. * (float(i)/len(names))**2 + .5)
    if current_progress > progress:
        progress = current_progress
        print("%i %%" % progress)
    c = 0
#...

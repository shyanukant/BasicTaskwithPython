import os
def changeName(dir, file):
    currentDir = os.listdir(dir)
    os.chdir(dir)

    for i in range(len(currentDir)):
        # print(file[i])
        if file in currentDir[i] and (str(i+1)+file) not in currentDir:
            os.rename(currentDir[i], str(i+1)+file)

    return "File Update Succesfully"

if __name__ == '__main__':

    print(changeName("C:/Users/admin/OneDrive/Pictures/Saved Pictures/4x", '.png'))

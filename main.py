import serial
import csv


def write_csv():
    # recuperer les valeur de CO2 à partir du COM5
    portserie = serial.Serial('COM5', baudrate = 9600, timeout = 5)
    fieldnames = ["t", "x"]
    # creer un ficher data.csv et mettre le header
    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    t = 1
    # remplir le ficher data.csv par les valeur de CO2
    while 1:
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            x = portserie.readline().decode('ascii')
            info = {
                "t": t,
                "x": x,
            }

            csv_writer.writerow(info)
            print(t, x)
            t += 1
            csv_file.close()




def write_to_file():
    portserie = serial.Serial('COM5', baudrate = 9600, timeout = 5)

    while 1:
        fichier = open('CO2d.txt','a')
        CO2_donnees = portserie.readline().decode('ascii')
        print(CO2_donnees)
        fichier.write(CO2_donnees)
        fichier.close()


if __name__ == "__main__":
    write_csv()
    #write_to_file()
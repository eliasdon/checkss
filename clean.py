import csv

final_new_listings = []

with open('final_results.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # loop thru csv rows
    for row in csv_reader:

        manfac = row[0].replace(',', '').strip()
        year = row[1].replace('Circa', '').replace(',', '').strip()

        try:
            year = str(int(year))
        except:
            pass

        price = row[2].replace('CHF', '').replace(
            'HK$', '').replace('none', '0').replace(',', '').replace('$', '').strip()

        if not len(year) > 4:

            try:
                price = str(int(price))
                row = manfac + ',' + year + ',' + price + '\n'

                final_new_listings.append(row)
            except:
                pass


f = open('final.csv', "a", encoding='utf-8')

for listing in final_new_listings:
    # print(listing)

    f.write(str(listing))
f.close()

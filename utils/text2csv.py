import csv

if __name__ == '__main__':
    with open('plots.txt', 'r', encoding='UTF8') as file_, open('clean_plots.csv', 'w', encoding='UTF8') as csvfile:
        lines = [x for x in file_.read().strip().split('<EOS>') if x]
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(('ID', 'Plot'))
        for idx, line in enumerate(lines, 1):
            writer.writerow((idx, line.strip('<EOS>')))

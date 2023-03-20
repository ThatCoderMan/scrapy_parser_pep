import csv
import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = {}

    def process_item(self, item, spider):
        self.statuses[
            item['status']
        ] = self.statuses.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        results = [('Статус', 'Количество')]
        results += self.statuses.items()
        total = sum(self.statuses.values())
        results += [('Total', total)]
        time = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = BASE_DIR / f'results/status_summary_{time}.csv'
        with open(file_path, 'w', encoding='utf-8') as file:
            csv_writer = csv.writer(file, dialect='unix')
            csv_writer.writerows(results)

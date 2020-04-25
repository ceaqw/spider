# ending: utf8
# describe: csv数据处理

import csv


def read_csv_demo1():
    """
    csv文件普通格式读取
    """
    with open("./stock.csv", "r") as fp:
        reader = csv.reader(fp)
        for line in reader:
            print(line[0])

def read_csv_demo2():
    """
    csv文件按字典格式读取
    """
    with open("stock.csv", "r") as fp:
        reader = csv.DictReader(fp)
        for line in reader:
            print(line["secShortName"])


def write_csv_demo1():
    """
    csv文件普通写入
    """
    fp = open("csv_write_test.csv", "a", encoding="utf8", newline="")
    header = ["key", "value"]
    test_data = [
        ("key1", "value1"),
        ("key2", "value2"),
    ]

    write = csv.writer(fp)
    write.writerow(header)
    write.writerows(test_data)


def write_csv_demo2():
    """
    按字典格式写入
    """
    fp = open("csv_write_test.csv", "a", encoding="utf8", newline="")
    header = ["key", "value"]
    data = [
        {"key": "key1", "value": "value1"},
        {"key": "key2", "value": "value2"},
    ]

    write = csv.DictWriter(fp, header)
    write.writeheader()
    write.writerows(data)



if __name__ == "__main__":
    write_csv_demo2()
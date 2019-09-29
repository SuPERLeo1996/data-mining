if __name__ == '__main__':
    infos = []
    with open('detail1.csv', 'r', encoding='utf-8') as list_file:
        for line in list_file.readlines():
            infos.append(line.strip())

    with open('detail2.csv', 'r', encoding='utf-8') as list_file:
        for line in list_file.readlines():
            infos.append(line.strip())

    with open('detail3.csv', 'r', encoding='utf-8') as list_file:
        for line in list_file.readlines():
            infos.append(line.strip())

    with open('detail4.csv', 'r', encoding='utf-8') as list_file:
        for line in list_file.readlines():
            infos.append(line.strip())

    with open('detail5.csv', 'r', encoding='utf-8') as list_file:
        for line in list_file.readlines():
            infos.append(line.strip())

    with open('detail6.csv', 'r', encoding='utf-8') as list_file:
        for line in list_file.readlines():
            infos.append(line.strip())

    with open('detail.csv', 'w', encoding='utf-8') as file:
        for info in infos:
            file.writelines(info+"\n")

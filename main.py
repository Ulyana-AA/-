id = str(input())

res = worksheet.col_values(1)
res1 = worksheet.col_values(2)
res2 = worksheet.get_all_records()

if len(id) >= 3 and len(id) < 8:
    tire = id.find("-")
    if tire == -1:
        print('Не удалось распознать штрих-код')
    else:
        a = id[:tire]
        b = id[(tire+1):]
        if len(a) == len(b) == 3:
            if b not in res:
                print('Неизвестный абонемент')
            if not a == res1:
                if not b == res:
                    print('Внимание, поддельный штрих-код')
            for i in range(1, len(worksheet.col_values(1))):
                res3 = worksheet.row_values(i)
                res4 = worksheet.row_values(i)
                if b in res3:
                    if a in res4:
                        K = str('E' + str(i))
                        M = str('F' + str(i))
                        res5 = worksheet.get('M')
                        res6 = worksheet.get('K')
                        if res5 == res6:
                            print('Лимит посещений по абонементу исчерпан')
else:
    print("Не удалось распознать штрих-код")

if __name__ == '__main__':
    print(id)

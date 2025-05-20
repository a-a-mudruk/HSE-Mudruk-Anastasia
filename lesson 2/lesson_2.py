name_1=input('Введите имя первого участника: ')
status_1=input('Введите статус первого участника: ')
inn_1=input('Введите ИНН первого участника: ')
name_2=input('Введите имя второго участника: ')
status_2=input('Введите статус второго участника: ')
inn_2=input('Введите ИНН второго участника: ')
name_3=input('Введите имя третьего участника: ')
status_3=input('Введите статус третьего участника: ')
inn_3=input('Введите ИНН третьего участника: ')
disputant_1 ={"name":name_1, "status":status_1, "inn":inn_1}
disputant_2 ={"name":name_2, "status":status_2, "inn":inn_2}
disputant_3 ={"name":name_3, "status":status_3, "inn":inn_3}
disputants = [disputant_1,disputant_2,disputant_3]
print(disputants)
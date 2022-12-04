A = {'Sasha', 'Pasha', 'Igor', 'Dima', 'Viktor', 'Sergey','Stepan', 'Vasya','Vika','Tamara', 'Inna', 'Anna'}
B = {'Max', 'Evgenii', 'Denis', 'Andrii', 'Stepan', 'Vasya','Sasha', 'Pasha', 'Igor','Anna','Inna','Gliya'}

print(f'Должники за Сентябрь и Октябрь {A} \n  {B}')
print('Должники за Октябрь у которых нет долга за Сентябрь:')
print(', '.join(set.difference(B, A)))
#print(f'Должники за Октябрь у которых нет долга за Сентябрь {set.difference(B,A)}')
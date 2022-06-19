# find companies that pay less than minimum salary

companies = {
    'ACompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
    'BCompany' : {'Ann' : 4, 'Lee' : 9, 'Chris' : 7},
    'CCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}
}

illegal = {x for x in companies if any(v < 9 for v in companies[x].values())}

print(illegal)
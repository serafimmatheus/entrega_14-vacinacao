# entrega_14-vacinacao

POST em /vaccinations

{
"cpf": "00000000000",
"name": "Jhoe Doe",
"first_shot_date": "29/03/2022",
"vaccine_name": "Pfaiser",
"health_unit_name": "LT-04"
}

GET em /vaccinations
retorna todos os cadastrados

GET em /vaccinations/00000000000
retorna um unico paciente pelo cpf
{
"cpf": "00000000000",
"name": "Jhoe Doe",
"first_shot_date": "29/03/2022",
"vaccine_name": "Pfaiser",
"health_unit_name": "LT-04"
}

GET em /vaccinations/Jhoe Doe
retorna um unico paciente pelo nome completo
{
"cpf": "00000000000",
"name": "Jhoe Doe",
"first_shot_date": "29/03/2022",
"vaccine_name": "Pfaiser",
"health_unit_name": "LT-04"
}

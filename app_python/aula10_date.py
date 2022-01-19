from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A, %d of %B of %Y')
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    hora = time(hour=15, minute=18, second=30)
    print(hora)
    hora_str = hora.strftime('%H:%M:%S')
    print(hora_str)
    print(type(hora_str))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y, %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_str = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_str, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)

def trabalando_com_timedelta():
    data_str = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_str, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    #trabalhando_com_datetime()
    trabalando_com_timedelta()

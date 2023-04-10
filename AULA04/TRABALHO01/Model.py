from DateStruct import DateStruct


class Model:
    def lerData(self):
        day = int(input("Digite o dia: "))
        month = int(input("Digite o mês: "))
        year = int(input("Digite o ano: "))
        return DateStruct(day, month, year)

    def validarData(self, data):
        if data.get_month() == 2:
            if data.get_year() % 4 == 0 and (data.get_year() % 100 != 0 or data.get_year() % 400 == 0):
                max_day = 29
            else:
                max_day = 28
        elif data.get_month() in [4, 6, 9, 11]:
            max_day = 30
        else:
            max_day = 31

        if data.get_day() < 1 or data.get_day() > max_day:
            return 0
        elif data.get_month() < 1 or data.get_month() > 12:
            return 0
        elif data.get_year() < 1900:
            return 0
        else:
            return 1

    def verificarBissexto(self, data):
        if data.get_year() % 4 == 0 and (data.get_year() % 100 != 0 or data.get_year() % 400 == 0):
            return 1
        else:
            return 0

    def verificarPascoa(self, data):
        if isinstance(data, int):
            year = data
        else:
            year = data.get_year()

        a = year % 19
        b = year // 100
        c = year % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1

        return DateStruct(day, month, year)

    def escreverExtenso(self, data):
        if self.validarData(data):
            dia = data.get_day()
            mes = data.get_month()
            ano = data.get_year()

            meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                     "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

            data_extenso = f"{dia} de {meses[mes-1]} de {ano}"
            print(data_extenso)
            return True
        else:
            return False

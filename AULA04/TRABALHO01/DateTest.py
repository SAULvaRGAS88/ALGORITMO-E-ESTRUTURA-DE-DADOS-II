from DateStruct import DateStruct
from Model import Model


class DateTest:
    def test(self):
        # Criando uma instância da classe Model
        model = Model()

        # Testando o método "lerData"
        data = model.lerData()
        print(f"Data lida: {data}")

        # Testando o método "validarData"
        if model.validarData(data):
            print("Data válida!")
        else:
            print("Data inválida!")

        # Testando o método "verificarBissexto"
        if model.verificarBissexto(data):
            print("Ano bissexto!")
        else:
            print("Ano não é bissexto!")

        # Testando o método "verificarPascoa"
        pascoa = model.verificarPascoa(data)
        print(f"Páscoa em {pascoa}")

        # Testando o método "escreverExtenso"
        if model.escreverExtenso(data):
            print("Data escrita por extenso com sucesso!")
        else:
            print("Erro ao escrever data por extenso!")


# Criando uma instância da classe DateTest e testando os métodos implementados na classe Model
test = DateTest()
test.test()

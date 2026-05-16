from faker import Faker 
import tkinter as tk
fake = Faker("pt_BR")

janela = tk.Tk()
janela.title("Gerador de dados BR")
janela.config(bg = '#101828')
janela.geometry("800x800")

imagem = tk.PhotoImage(file = 'unimar_logo.png')
imagem_ajustada = imagem.subsample(3, 3)
label_imagem = tk.Label(janela, image = imagem_ajustada)
label_imagem.config(bg = '#101828')
label_imagem.pack(pady=0)

texto1 = tk.Label(janela, text = "Bem Vindo ao Gerador de Dados Brasileiros!")
texto1.config(font = ("Arial", 25), bg = '#101828', fg = 'white')
texto1.pack(pady=0)

texto2 = tk.Label(janela, text = "Selecione o sexo que deseja gerar")
texto2.config(font = ("Arial", 20), bg = '#101828', fg = 'white')
texto2.pack(pady=1)

variavel_sexo = tk.StringVar(value = "m")
tk.Radiobutton(janela, text = "Masculino", variable = variavel_sexo, value = "m", font = ("Arial", 11), bg = '#101828', fg ='white', selectcolor='black').pack()
tk.Radiobutton(janela, text = "Feminino", variable = variavel_sexo, value = "f", font = ("Arial", 11), bg = '#101828', fg ='white', selectcolor='black').pack()

quadrado_resultado = tk.Label(janela, text = "")
quadrado_resultado.config(justify ="left", font = ("Consolas", 10), width = 65, height = 25, relief = "sunken", bg = '#364153', fg = 'white', pady = 8)
quadrado_resultado.pack()



lista_signo = ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"]
lista_sanguinea = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
lista_olho = ["Castanho", "Azul", "Preto", "Verde"]
lista_pele = ["Branco", "Pardo", "Negro", "Amarela"]
lista_times = ["Palmeiras", "Corinthians", "São Paulo", "Santos", "Flamengo", "Vasco", "Fluminense", "Botafogo", "Grêmio", "Internacional", "Atlético-MG", "Cruzeiro"]

def gerar_informacoes():
    sexo = variavel_sexo.get()

    pai = fake.first_name_male()
    pai_s = fake.last_name()
    mae = fake.first_name_female()
    mae_s = fake.last_name()

    pai += f' {pai_s}'
    mae += f' {mae_s}'

    if sexo == "m":
        sexo = "Masculino"
        nome= fake.first_name_male()
    else:
        sexo = "Feminino"
        nome = fake.first_name_female()

    nome += f' {mae_s} {pai_s}'



    idade = fake.random_int(min = 18, max = 100)
    cpf = fake.cpf()
    rg = fake.rg()
    signo = fake.random_element(elements = lista_signo)
    email = fake.email()
    senha = fake.password(length = 12)
    cep = fake.postcode()
    endereco = fake.street_name()
    numero = fake.building_number()
    bairro = fake.neighborhood()
    cidade = fake.city()
    estado = fake.state_abbr()
    telefone = fake.phone_number()
    celular = fake.cellphone_number()
    altura = f'{fake.pyfloat(min_value = 1.50, max_value = 2.10, right_digits = 2):.2f}m'
    peso = f'{fake.pyfloat(min_value = 40.0, max_value = 120.0, right_digits = 1):.1f}kg'
    tipo_sanguineo = fake.random_element(elements = lista_sanguinea)
    cor_fav = fake.color_name()
    cor_olhos = fake.random_element(elements = lista_olho)
    cor_pele = fake.random_element(elements = lista_pele)
    time = fake.random_element(elements = lista_times)

    dados = [
        ["Nome", nome],
        ["Nome do Pai", pai],
        ["Nome da Mãe", mae],
        ["Sexo", sexo],
        ["Idade", idade],
        ["CPF", cpf],
        ["RG", rg],
        ["Signo", signo],
        ["Email", email],
        ["Senha", senha],
        ["CEP", cep],
        ["Endereço", endereco],
        ["Número", numero],
        ["Bairro", bairro],
        ["Cidade", cidade],
        ["Estado", estado],
        ["Telefone", telefone],
        ["Celular", celular],
        ["Altura", altura],
        ["Peso", peso],
        ["Tipo Sanguíneo", tipo_sanguineo],
        ["Cor Favorita", cor_fav],
        ["Cor do Olho", cor_olhos],
        ["Cor de Pele", cor_pele],
        ["Time", time]
    ]

    texto_exibicao = ""
    for informacao, valor in dados:
        texto_exibicao += f"{informacao:<15}: {valor}\n"

    quadrado_resultado.config(text = texto_exibicao)


botao = tk.Button(janela, text = "GERAR DADOS", command = gerar_informacoes, font = ("Arial", 15),bg = 'white', activebackground = '#c3c2c2')
botao.pack(pady = 21)
rodape = tk.Label(
    janela, 
    text="Desenvolvido por: Henrique, Kelvin e Matheus.", 
    font=("Arial", 10), 
    bg='#101828', 
    fg="#e7e7e7")
rodape.place(relx=0.98, rely=0.99, anchor="se")

janela.mainloop()
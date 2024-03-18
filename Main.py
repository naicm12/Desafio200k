import streamlit as st
import mysql.connector
import re
from datetime import date

conexao = mysql.connector.connect(
    host='200k.mysql.uhserver.com',
    user='ecm200',
    password='@Musica17',
    database='200k'
)

st.set_page_config(page_title="3º Desafio 200k")
tela_ativa = 0

from PIL import Image
img = Image.open('02.png')
st.image(img)

st.markdown("### 3º Desafio 200k - Porto Velho/Humaítá")

form_informativo = st.empty()

with ((form_informativo.form("Informativo"))):
    st.markdown("##### Informativo do Desafio")
    st.write("📅 Dia 05 de Julho de 2024")
    st.write("🏃🏻 Largada às 16hs 🕗")
    st.write("📍 Saída: Início do Espaço Alternativo - Av. Jorge Teixeira (Praia)")
    st.caption("")
    st.write("💲 Valor da Inscrição: 500,00 reais Solo e 400,00 reais se for em equipe (valor da inscrição é individual)")
    st.write(" Forma de Pagamento: ")
    st.write("  Pix kelioesteves@hotmail.com - Kélio Esteves Xavier - Mercado pago.")
    st.write("📱 Mais informações: (69) 99925-9005/ (69) 99308-8323 / (69) 99958-3207")
    st.caption("")
    st.write("🏆 Os atletas receberão camiseta, viseira, sacolinha, medalha e um troféu por equipe ou solo.")
    st.write("🚙 Os apoio devem fazer a inscrição para receber camisa e medalha do evento. Em breve link para inscrição do apoio")
    st.caption("")
    st.write("INSCRIÇÕES:")
    st.write("✍️ Período de inscrição:")
    st.write("  Início: 17 de março de 2024")
    st.write("  Término: 20 de maio 2024 ou até o limite das vagas")

    st.page_link("https://www.4shared.com/web/preview/pdf/fFCk8nZrjq?", label="{$} Clique aqui para ver o Regulamento {$}")
    btn_regul = st.form_submit_button("",disabled=True)

def concluido():
    global tela_ativa
    #placeholder.empty()
    #placeholder2 = st.empty()

    #with placeholder2.form("Regulamento"):
    st.success("INSCRIÇÃO REALIZADA COM SUCESSO")
    #st.write(incricao().modalidade)
    #st.write(incricao().idmodalidade)
    #st.write(incricao().kmsolo)
    #st.write("id_atleta ", inscricao().idatleta)



form_inscricao = st.empty()

def inscricao():
    global tela_ativa
    global concluido

    with ((form_inscricao.form("Inscricao"))):
        st.markdown("### Formulário de Inscrição")

        input_email = st.text_input(label="E-mail:", key="01")
        input_nome = st.text_input(label="Primeiro Nome:", placeholder="Insira apenas seu primeiro nome", key="02")
        input_sobrenome = st.text_input(label="Sobrenome:", placeholder="Insira seu sobrenome",key="03")
        c1,c2 = st.columns([1,1])
        with c1:
            input_cpf = st.text_input(label="CPF (99999999999):", placeholder="Somente números", max_chars=11,key="04")
        with c2:
            input_dn = st.date_input(label="Data de Nascimento:",format="DD/MM/YYYY", value=None, key="05")
        input_telefone = st.text_input(label="Nº Celular 99 99999-9999:", max_chars=15, key="06")
        input_equipe = st.text_input(label="Equipe/Grupo/Academia pessoal:",placeholder="Se percente a alguma Equipe, Grupo ou academia, informe aqui",key="22")
        st.caption("Endereço:")
        e1, e2 = st.columns([4,1])
        with e1:
            input_rua = st.text_input(label="Rua:", key="07")
        with e2:
            input_numero = st.text_input(label="Número:", key="15")
        input_comp = st.text_input(label="Complemento:", key="28")
        input_bairro = st.text_input(label="Bairro:", key="08")
        g1, g2 = st.columns([2, 1])
        with g1:
            input_cidade = st.text_input(label="Cidade:", value="Porto Velho", key="09")
        with g2:
            input_estado = st.selectbox("Estado:",("Acre (AC)",
                                                   "Alagoas (AL)",
                                                   "Amapá (AP)",
                                                   "Amazonas (AM)",
                                                   "Bahia (BA)",
                                                   "Ceará (CE)",
                                                   "Distrito Federal (DF)",
                                                   "Espírito Santo (ES)",
                                                   "Goiás (GO)",
                                                   "Maranhão (MA)",
                                                   "Mato Grosso (MT)",
                                                   "Mato Grosso do Sul (MS)",
                                                   "Minas Gerais (MG)",
                                                   "Pará (PA)",
                                                   "Paraíba (PB)",
                                                   "Paraná (PR)",
                                                   "Pernambuco (PE)",
                                                   "Piauí (PI)",
                                                   "Rio de Janeiro (RJ)",
                                                   "Rio Grande do Norte (RN)",
                                                   "Rio Grande do Sul (RS)",
                                                   "Rondônia (RO)",
                                                   "Roraima (RR)",
                                                   "Santa Catarina (SC)",
                                                   "São Paulo (SP)",
                                                   "Sergipe (SE)",
                                                   "Tocantins (TO)"),index=21)

        f1,f2,f3 = st.columns([1,1,1])
        with f1:
            input_genero = st.radio("Gênero:", ["Masculino", "Feminino"])
        with f2:
            input_camiseta = st.radio("Camiseta:", ["PP", "P", "M", "G"])
        with f3:
            input_modalidade = st.radio("Modalidade:", ["Solo", "Dupla", "Quarteto", "Octeto"],
                                    captions=["200Km", "100Km cada", "50km cada", "25Km cada"])
        input_participantes = st.text_input(label="Informe os nomes dos participantes incluindo o seu:", key="11",placeholder="Exemplo: João/Maria/Jose/Francica")
        st.caption("Obs: Peça para que os demais intengrates da Equipe informe os mesmo nomes separados por '/'")
        input_equipe200 = st.text_input(label="Nome da equipe do 3º Desafio 200K:",placeholder="Informe o Nome da Equipe que compõe o Desafio",key="12")

        st.divider()

        st.write("Termo de Responsabilidade")

        def termo():
            with open('Termo.txt', 'r', encoding='UTF-8') as f:
                lines = f.readlines()
                for line in lines:
                    st.caption(line)

        #exibtermo = st.checkbox(label="Exibir Termo de Responsabilidade",bool=False)
        #if exibtermo:
        termo()

        check_aceita = False
        #check_aceita = st.checkbox(label="LI E ACEITO O TERMO DE RESPONSABILIDADE",bool=False)
        agree = st.checkbox('LI E ACEITO O TERMO DE RESPONSABILIDADE')

        if agree:
            check_aceita = True

        cursor = conexao.cursor()
        comando = f'SELECT ID_ATLETA FROM 200k.ATLETA_PRECAD WHERE CPF = "{input_cpf}"'
        cursor.execute(comando)
        resultado_cpf = cursor.fetchone()
        #s_cpf = resultado_cpf[0]

        cursor1 = conexao.cursor()
        comando = f'SELECT ID_ATLETA FROM 200k.ATLETA_PRECAD WHERE EMAIL = "{input_email}"'
        cursor1.execute(comando)
        resultado_email = cursor1.fetchone()
        #s_email = resultado_email[0]

        cursor2 = conexao.cursor()
        id_ = f'SELECT IFNULL(MAX(ID_ATLETA)+1,1) FROM ATLETA_PRECAD'
        cursor2.execute(id_)
        newid = cursor2.fetchone()
        idatleta = newid[0]

        confirma_button = st.form_submit_button("CONFIRMAR INSCRIÇÃO",type="primary")

        if confirma_button:
            if input_email == '':
                st.warning("Informe o E-mail!", icon="⚠️")
                st.stop()

            if input_cpf == '':
                st.warning("Informe o CPF!", icon="⚠️")
                st.stop()

            if input_nome == '':
                st.warning("Informe o primeiro Nome!", icon="⚠️")
                st.stop()

            if input_sobrenome == '':
                st.warning("Informe o primeiro Nome!", icon="⚠️")
                st.stop()

            if input_dn == '':
                st.warning("Informe sua Data de Nascimento!", icon="⚠️")
                st.stop()

            if input_telefone == '':
                st.warning("Informe o número do Celular!", icon="⚠️")
                st.stop()

            if input_rua == '':
                st.warning("Informe a Rua!", icon="⚠️")
                st.stop()

            if input_bairro == '':
                st.warning("Informe o Bairro!", icon="⚠️")
                st.stop()

            if input_cidade == '':
                st.warning("Informe a Cidade e Estado (UF)!", icon="⚠️")
                st.stop()

            if resultado_cpf is not None:
                st.warning("CPF Já cadastrado!", icon="⚠️")
                st.stop()

            if resultado_email is not None:
                st.warning("E-mail Já cadastrado!", icon="⚠️")
                st.stop()

            if not check_aceita:
                st.warning("Necessário aceitar o Termo de Responsabildade!", icon="⚠️")
                st.stop()

            if input_genero == 'Masculino':
                sexo = "M"
            else:
                sexo = "F"

            if input_modalidade == 'Solo':
               modalidade = "Solo - 200km"
               idmodalidade = 1
               kmsolo = 200
            elif input_modalidade == 'Dupla':
               modalidade = "Dupla - 100km"
               idmodalidade = 2
               kmsolo = 100
            elif input_modalidade == 'Quarteto':
               modalidade = "Quarteto - 50km"
               idmodalidade = 3
               kmsolo = 50
            elif input_modalidade == 'Octeto':
               modalidade = "Octeto - 25km"
               idmodalidade = 4
               kmsolo = 25

            data = date.today()
            dataf = data.strftime('%d/%m/%Y')
            datanasc = input_dn.strftime('%d/%m/%Y')

            if idmodalidade > 1 and input_participantes == '':
                st.warning("Informe os nomes dos integrantes da Equipe do Desafio 200k", icon="⚠️")
                st.stop()

            if idmodalidade > 1 and input_equipe200 == '':
                st.warning("Informe o Nome da Equipe do Desafio 200k", icon="⚠️")
                st.stop()


            try:

                qry_insert = f"""INSERT INTO 200k.ATLETA_PRECAD (
                                 ID_ATLETA, CPF, NOME, ENDERECO, NR_ENDERECO, COMP_ENDERECO, CIDADE, ESTADO_UF, 
                                 DT_NASCIMENTO, NR_CELULAR, SEXO, CAMISETA, DE_EQUIPE, EMAIL, MODALIDADE, ID_MODALIDADE, 
                                 DE_EQUIPE200, INTEGRANTES, KM_SOLO, FL_STATUS, ATIVO, DT_INSCRICAO, ACEITO_TERMO)
                                 VALUES (
                                        {idatleta},"{input_cpf}","{input_nome + ' ' + input_sobrenome}","{input_rua}","{input_numero}",
                                        "{input_comp}","{input_cidade}","{input_estado}","{datanasc}","{input_telefone}","{sexo}",
                                        "{input_camiseta}","{input_equipe}","{input_email}","{modalidade}",{idmodalidade},
                                        "{input_equipe200}","{input_participantes}","{kmsolo}",'P','S',"{dataf}",'S' ) """

                cursor = conexao.cursor()
                cursor.execute(qry_insert)
                conexao.commit()
                cursor.close()

            except mysql.connector.Error as error:
                st.warning("Erro no Banco de Daods, tente novamente, se persistir contate o Administrador do Sistema! {}".format(error), icon="⚠️")
                st.stop()

            finally:
                if conexao.is_connected():
                    conexao.close()

            #st.write(sexo)
            #st.write(modalidade)
            #st.write(idmodalidade)
            #st.write(kmsolo)
            #st.write("id_atleta ",idatleta)

            tela_ativa = 2

            form_inscricao.empty()


inscricao()

if tela_ativa == 2:
    form_informativo.empty()
    st.success("PRÉ INSCRIÇÃO REALIZADA COM SUCESSO")
    st.warning("ATENÇÃO", icon="⚠️")
    st.warning("A efetivação da sua Inscrição está condicionada ao envio do comprovante de pagamento para o número (69) 99925-9005, ou pelo link a baixo:")
    st.warning("https://wa.me/5569999259005", icon="📱")

from PIL import Image
img = Image.open('003.png')
st.image(img)




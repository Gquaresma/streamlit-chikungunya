from components.header import header
import streamlit as st

header(st)

tab1, tab2, tab3 = st.tabs(["Sobre", "Pré processamento", "O melhor modelo"])

with tab1:
    st.write("<h3>Sobre o projeto</h3>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify;'> Em 2022, na 37ª semana epidemiológica, o Brasil registrou 166.197 casos prováveis de Chikungunya, \
        uma arbovirose que, apesar de pouco mortal, pode causar sintomas de longa duração. \
        Esse número corresponde a um aumento de 89% \
        de casos em relação ao ano anterior, \
        tendo uma incidência de 77,9 a cada 100 mil habitantes. </p>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify;'> O processo de diagnóstico da Chikungunya pode ser realizado por profissionais de saúde de forma manual \
        ou utilizando artifícios tecnológicos. Modelos de aprendizado de máquina são capazes de aprender padrões \
        a partir de um conjunto de dados, tendo potencial para auxiliar no processo de diagnóstico de doenças e \
        tomada de decisão. Dessa forma, é possível reduzir a possibilidade de erros de diagnósticos, reduzir \
        custos de exames laboratoriais e até mesmo realizar atendimento em maior escala, especialmente em \
        locais com poucos recursos disponíveis para saúde. </p>", unsafe_allow_html=True)

with tab2:
    st.write("<h3>Pré processamento dos dados</h3>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify;'> Nesse projeto é utilizada uma base com dados \
    reais de 140.516 pacientes brasileiros, coletados do Sistema de Informação de \
    Agravos de Notificação (SIAN). Originalmente, a base contava com 120 colunas, também chamados\
    de atributos. Desses, foram removidos atributos capazes de enviezar os aprendizado do modelo \
    tais quais resultados de exames. Também foram removidos aqueles irrelevantes para a identificação \
    da Chikungunya, como região, datas, raça, idade e outros. Dessa forma, o número de atributos foi reduzido, e, com aplicação \
    de feature selection, foram mantidos 10 atributos. </p>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify;'>É importante lembrar que os modelos treinados \
    trabalham apenas com dados numéricos. Sendo assim, todos os atributos que não estavam nesse \
    formato foram convertidos, processo chamado de transformação dos dados. Por exemplo: para sexo, \
    o modelo interpretará \"Masculino\" como 1, \"Feminino\" como 2 e \"Não informado\" como 0. \
    </p>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify;'>Nota-se também que a base de dados original está \
    desbalanceada, ou seja, os casos cuja classificação constava como outra doença são muito mais \
    numeroso do que os casos classificados como Chikungunya. Por esse motivo foi realizado o balanceamento \
    utilizando a técnica de Under Sampling, onde a quantidade de dados é nivelado entre as classificações \
    pelo menor número. O Under Sampling foi escolhido por se tratarem de dados reais de indivíduos, os \
    os quais não poderiam ser criados para dar suporte a um Over Sampling. Ao fim do processo, ambas as \
    as classificações possuiam 7095 resultados cada, totalizando um conjunto de 14.190 dados.</p>", unsafe_allow_html=True)

    st.image("./assets/img/balance_before.png", caption="Antes do under sampling", width=500)

    st.image("./assets/img/balance_after.png", caption="Depois do under sampling", width=500)

with tab3:

    st.write("<h3>O melhor modelo</h3>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify;'>O modelo que utiliza o método Random Forest foi selecionado \
    como melhor modelo, tendo acurácia de 84.61%, e média macro para precisão, sensibilidade e f1-score de 85%. \
    Tais resultados são idênticos aos de outro modelo que utilizou Gradient Boosting para o treinamento, porém, \
    o modelo escolhido possui um tempo de processamento muito menor, portanto, apresenta vantagem.   \
    .</p>", unsafe_allow_html=True)

    st.write("<h5>Feature Selection</h5>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify;'>Foi aplicada no modelo a estratégia de feature selection, a fim \
    de itendificar os melhores atributos a serem utilizados no mesmo. Ao final do processo, o algorítimo selecionou \
    os seguintes atributos: tempo gestacional, febre, mialgia, dor nas costas, artrite, \
    artralgia, diabetes, gengivorragia, metrorragia e petequias. \
    .</p>", unsafe_allow_html=True)

    st.write("<h5>Grid Search</h5>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify;'>Outra estratégia aplicada foi a de grid search, utilizada para \
    identificar os melhores parâmetros para treinamento do modelo. Os parâmetros selecionados foram utilizados \
    treinamento final, sendo eles:</p>", unsafe_allow_html=True)
    st.write("<span>bootstrap: True</span>", unsafe_allow_html=True)
    st.write("<span>criterion: gini</span>", unsafe_allow_html=True)
    st.write("<span>max_depth: None, </span>", unsafe_allow_html=True)
    st.write("<span>min_samples_leaf: 5, </span>", unsafe_allow_html=True)
    st.write("<span>min_samples_split: 5, </span>", unsafe_allow_html=True)
    st.write("<span>n_estimators: 150</span>", unsafe_allow_html=True)

    st.write("<h5>Matriz de Confusão</h5>", unsafe_allow_html=True)
    st.image("./assets/img/random_forest_grid_search.png", caption="Matriz de confusão dos resultados do melhor modelo.", width=500)




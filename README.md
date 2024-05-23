# DevopsPipelineTrabalho

Este é um projeto de demonstração de execução de um projeto simples em uma pipeline.
O projeto é um calculadora feita em python e possui seus testes unitários também em python usando framework de testes unittest.
A pipeline é definida no arquivo pipeline.yml e é acionada sempre que ocorre um push no main branch do repositório. 
A pipeline é executado em uma máquina virtual com sistema operacional Ubuntu mais recente. Consiste em um job chamado "build", que é composto por várias etapas.
      1.	Checkout de código: A primeira etapa do pipeline é fazer o checkout do código-fonte do repositório utilizando a ação "actions/checkout@v2".
      2.	Configuração do Python: Em seguida, é realizada a configuração do ambiente Python utilizando a ação "actions/setup-python@v2". A versão 3.9 do Python é especificada.
      3.	Instalação de dependências: A próxima etapa é a instalação das dependências do projeto. Isso é feito executando o comando "pip install -r requerimentos.txt".
      4.	Execução de testes unitários: Por fim, são executados os testes unitários utilizando o comando "python -m unittest discover -s tests -p "*testes.py"". Essa etapa é responsável por descobrir e executar todos os testes unitários presentes na pasta "tests" que correspondem ao padrão "*testes.py".

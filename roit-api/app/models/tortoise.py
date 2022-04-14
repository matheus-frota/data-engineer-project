from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Empresa(models.Model):
    cnpj_basico = fields.TextField(null=True)
    razao_social = fields.TextField(max_length=255, null=True)
    cod_natureza_juridica = fields.TextField(null=True)
    cod_qualificacao_do_responsavel = fields.TextField(null=True)
    capital_social = fields.TextField(null=True)
    cod_porte_da_empresa = fields.TextField(null=True)
    desc_ente_federativo_responsavel = fields.TextField(max_length=128, null=True)
    created_at = fields.DateField()

    def __str__(self):
        return self.razao_social


class Estabelecimento(models.Model):
    cnpj_basico = fields.TextField(null=True)
    cnpj_ordem = fields.TextField(null=True)
    cnpj_dv = fields.TextField(null=True)
    cod_identificador_matriz_filial = fields.TextField(null=True)
    nome_fantasia = fields.TextField(null=True)
    cod_situacao_cadastral = fields.TextField(null=True)
    data_situacao_cadastral = fields.TextField(null=True)
    cod_motivo_situacao_cadastral = fields.TextField(null=True)
    end_nome_cidade_no_exterior = fields.TextField(null=True)
    end_cod_pais = fields.TextField(null=True)
    data_inicio_atividade = fields.TextField(null=True)
    cod_cnae_fiscal_primaria = fields.TextField(null=True)
    cod_cnae_fiscal_secundaria = fields.TextField(null=True)
    end_tipo_de_logradouro = fields.TextField(null=True)
    end_logradouro = fields.TextField(null=True)
    end_numero = fields.TextField(null=True)
    end_complemento = fields.TextField(null=True)
    end_bairro = fields.TextField(null=True)
    end_cep = fields.TextField(null=True)
    end_uf = fields.TextField(null=True)
    end_cod_municipio = fields.TextField(null=True)
    ddd1 = fields.TextField(null=True)
    telefone1 = fields.TextField(null=True)
    ddd2 = fields.TextField(null=True)
    telefone2 = fields.TextField(null=True)
    dddfax = fields.TextField(null=True)
    fax = fields.TextField(null=True)
    email = fields.TextField(null=True)
    cod_situacao_especial = fields.TextField(null=True)
    data_situacao_especial = fields.TextField(null=True)
    created_at = fields.DateField()

    def __str__(self):
        return self.nome_fantasia


EmpresaSchema = pydantic_model_creator(Empresa)
EstabelecimentoSchema = pydantic_model_creator(Estabelecimento)

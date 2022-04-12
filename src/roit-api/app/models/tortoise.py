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


EmpresaSchema = pydantic_model_creator(Empresa)

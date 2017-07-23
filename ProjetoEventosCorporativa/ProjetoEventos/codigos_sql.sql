--Necessario importar todos os models antes
--from ProjetoEventos.models import *

-- Usuario

Usuario.objects.all()
Usuario.objects.create(nome="nome", senha="senha", email="email")

user = Usuario.objects.get(nome="nome")

Usuario.objects.filter(nome="kairo")
Usuario.objects.filter(nome__contains="k")
Usuario.objects.order_by(nome) 
Usuario.objects.order_by(-nome) --inverso
user.delete 


--Instituicao

Instituicao.objects.all()
Instituicao.objects.create(nome="infoway", local_instituicao="sdvagsdgasv", descricao="nfjkdjdfbsdbfhbsd")
instituicao = Instituicao.objects.get(nome="infoway")
instituicao.delete

--Cupom
Cupom.objects.all()
Cupom.objects.create(cod_cupom="cod1", desconto=30, data_validade="2017-12-30")
cupom_evento = Cupom.objects.get(cod_cupom="cod1")
cupom_evento.remove

--Evento

Evento.objects.all()
Evento.objects.create(nome="nome", tipo_evento=Tipo_Evento, estado_evento=Estado_Evento, usuario=user, data_inicio="2017-12-30" data_fim="2017-12-31", cupom=cupom_evento)
evento_teste=Evento.objects.get(nome="nome")
evento_teste.remove

--Apoio Realizacao
Apoio_Realizacao.objects.all()
Apoio_Realizacao.objects.create(cod_apoio='121',instituicao_cod=instituicao, evento_cod=evento_teste, tipo_ApoioRealizacao=tipo_apoio)
apoio=Apoio_Realizacao.objects.get(cod_apoio='125')
apoio.delete


--Atividade
Atividade.objects.all()
Atividade.objects.create(nome="palestra xxx", tipoAtividade = tipoAtividade, evento_cod_evento = evento_teste, valor=45.9)
ativ1 = Atividade.objects.get(nome="palestra xxx")
Atividade.objects.order_by(valor)
Atividade.objects.filter(nome__contains="palestra")
ativ1.delete

--Inscricao
Inscricao.objects.all()
Inscricao.objects.filter(evento_cod.nome__contains="evento")
Inscricao.objects.order_by(-estado)
status_pagamento = Estado_Inscricao.objects.create(estado='0')
Inscricao.objects.create(usuario_cod=user,data_inscricao="2017-12-31",valor_total=45.9,evento_cod=evento_teste,pagamento="####-##-##",estado=status_pagamento)
inscricao = Inscricao.objects.get(usuario.name="kairo", evento_cod.nome=="Evento")
inscricao.delete

--Item Inscricao
Item_Inscricao.objects.all()
Item_Inscricao.objects.create(inscricao_cod=inscricao,atividade_cod=ativ1)
teste_item = Item_Inscricao.objects.get(inscricao.evento_cod("evento"))
teste_item.delete




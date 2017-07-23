# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-23 04:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetoEventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apoio_Realizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Cupom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_cupom', models.CharField(max_length=45)),
                ('desconto', models.IntegerField()),
                ('data_validade', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('0', 'ABERTO'), ('1', 'EMANDAMENTO'), ('2', 'ENCERRADO')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('0', 'PAGO'), ('1', 'NAOPAGO')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('cupom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Cupom')),
                ('estado_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Estado_Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inscricao', models.DateField()),
                ('valor_total', models.FloatField()),
                ('pagamento', models.DateField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Estado_Inscricao')),
                ('evento_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Evento')),
                ('usuario_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('local_instituicao', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atividade_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Atividade')),
                ('inscricao_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Inscricao')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_ApoioRealizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('0', 'APOIO'), ('1', 'REALIZACAO')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('0', 'PALESTRA'), ('1', 'MINICURSO'), ('2', 'MESAREDONDA')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('0', 'SIMPOSIO'), ('1', 'CONGRESSO'), ('2', 'JORNADA'), ('3', 'SEMANACIENTIFICA'), ('4', 'CICLODEPALESTRA')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Tipo_Evento'),
        ),
        migrations.AddField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Usuario'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='evento_cod_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Evento'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='tipoAtividade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Tipo_Atividade'),
        ),
        migrations.AddField(
            model_name='apoio_realizacao',
            name='eventos_cod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Evento'),
        ),
        migrations.AddField(
            model_name='apoio_realizacao',
            name='instituicao_cod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Instituicao'),
        ),
        migrations.AddField(
            model_name='apoio_realizacao',
            name='tipo_ApoioRealizacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetoEventos.Tipo_ApoioRealizacao'),
        ),
    ]

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gncomprobante, Gnopcion, Ivbodega, Ivgrupo1, Ivgrupo2, Ivgrupo3, Ivgrupo4, Ivgrupo5, Ivgrupo6, Ivinventario, Ivkardex, Ivkardexrecargo, Pcgrupo1, Pcgrupo2, Pcgrupo3, Pcgrupo4, Pcprovcli, ViewReports
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import pandas as pd
from datetime import datetime, date
from plotly.offline import plot
import plotly.express as px
from django.views.decorators.cache import cache_page

def home(request):
    return render(request, 'home.html', {
    })


@login_required
def panel_center(request):
    # type: ignore # type: ignore
    try:
        modelFcvendedor = ViewReports.objects.values('nombrevendedor').order_by('nombrevendedor')

        modelIvgrupo1 = ViewReports.objects.values('descripciongrupo1lineas').order_by('descripciongrupo1lineas')

        modelIvgrupo2 = ViewReports.objects.values('descripciongrupo2lineas').order_by('descripciongrupo2lineas')

        modelIvgrupo3 = ViewReports.objects.values('descripciongrupo3lineas').order_by('descripciongrupo3lineas')

        modelIvgrupo4 = ViewReports.objects.values('descripciongrupo4lineas').order_by('descripciongrupo4lineas')

        modelIvgrupo5 = ViewReports.objects.values('descripciongrupo5lineas').order_by('descripciongrupo5lineas')

        modelIvgrupo6 = ViewReports.objects.values('descripciongrupo6lineas').order_by('descripciongrupo6lineas')

        modelPcgrupo1 = ViewReports.objects.values('descripciong1cliente').order_by('descripciong1cliente')

        modelPcgrupo2 = ViewReports.objects.values('descripciong2cliente').order_by('descripciong2cliente')

        modelPcgrupo3 = ViewReports.objects.values('descripciong3cliente').order_by('descripciong3cliente')

        modelPcgrupo4 = ViewReports.objects.values('descripciong4cliente').order_by('descripciong4cliente')

        modelGnopcionG1 = Gnopcion.objects.values('etiquetagrupo1')
        modelGnopcionG2 = Gnopcion.objects.values('etiquetagrupo2')
        modelGnopcionG3 = Gnopcion.objects.values('etiquetagrupo3')
        modelGnopcionG4 = Gnopcion.objects.values('etiquetagrupo4')
        modelGnopcionG5 = Gnopcion.objects.values('etiquetagrupo5')
        modelGnopcionG6 = Gnopcion.objects.values('etiquetagrupo6')

        modelempresa = Gnopcion.objects.values('nombreempresa')

        modelGnopcionPc1 = Gnopcion.objects.values('etiquetapcgrupo1')
        modelGnopcionPc2 = Gnopcion.objects.values('etiquetapcgrupo2')
        modelGnopcionPc3 = Gnopcion.objects.values('etiquetapcgrupo3')
        modelGnopcionPc4 = Gnopcion.objects.values('etiquetapcgrupo4')


        report = ViewReports.objects.all()
        report_query = ViewReports.objects.all()

        # GRAFICOS
        projects_data = [
            {
                'Cantidad': (x.cantidad*-1),
                'NombreVendedor': x.nombrevendedor,
                'Precio Total': (x.preciorealtotal*-1),
                'Proveedor': x.nombrecliente,
                'Utilidad': (x.utilidad*-1),
                'Costo Total Real': (x.costorealtotal*-1),
                'Linea Grupo1': x.descripciongrupo1lineas,
                'Linea Grupo2': x.descripciongrupo2lineas,
                'Linea Grupo3': x.descripciongrupo3lineas,
                'Linea Grupo4': x.descripciongrupo4lineas,
                'Linea Grupo5': x.descripciongrupo5lineas,
                'Linea Grupo6': x.descripciongrupo6lineas,
                'Item': x.descripcionitem,
                'Clinete Grupo1': x.descripciong1cliente,
                'Clinete Grupo2': x.descripciong2cliente,
                'Clinete Grupo3': x.descripciong3cliente,
                'Clinete Grupo4': x.descripciong4cliente,
                'Fecha': x.fechatrans,
            } for x in report
        ]
        df = pd.DataFrame(projects_data)
        df1 = pd.DataFrame(df.groupby(by=['Fecha'])['Precio Total'].sum())
        df_rename = df.rename(columns={'Clinete Grupo4': 'Cliente4', 'Clinete Grupo1': 'Cliente1', 'Clinete Grupo2': 'Cliente2', 'Clinete Grupo3': 'Cliente3', 'Linea Grupo1': 'Linea1', 'Linea Grupo2': 'Linea2', 'Linea Grupo3': 'Linea3', 'Linea Grupo4': 'Linea4', 'Linea Grupo5': 'Linea5', 'Linea Grupo6': 'Linea6'})

        df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
        df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
        df_list_table_line1 = df_list_table_line1.reset_index()
        df_list_table_line1 = df_list_table_line1.to_dict('records')

        df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
        df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
        df_list_table_line2 = df_list_table_line2.reset_index()
        df_list_table_line2 = df_list_table_line2.to_dict('records')

        df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
        df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
        df_list_table_line3 = df_list_table_line3.reset_index()
        df_list_table_line3 = df_list_table_line3.to_dict('records')

        df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
        df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
        df_list_table_line4 = df_list_table_line4.reset_index()
        df_list_table_line4 = df_list_table_line4.to_dict('records')

        df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
        df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
        df_list_table_line5 = df_list_table_line5.reset_index()
        df_list_table_line5 = df_list_table_line5.to_dict('records')

        df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
        df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
        df_list_table_line6 = df_list_table_line6.reset_index()
        df_list_table_line6 = df_list_table_line6.to_dict('records')


        df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
        df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
        df_list_table_client1 = df_list_table_client1.reset_index()
        df_list_table_client1 = df_list_table_client1.to_dict('records')

        df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
        df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
        df_list_table_client2 = df_list_table_client2.reset_index()
        df_list_table_client2 = df_list_table_client2.to_dict('records')

        df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
        df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
        df_list_table_client3 = df_list_table_client3.reset_index()
        df_list_table_client3 = df_list_table_client3.to_dict('records')

        df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
        df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
        df_list_table_client4 = df_list_table_client4.reset_index()
        df_list_table_client4 = df_list_table_client4.to_dict('records')

        fig = px.histogram(
            df, x='NombreVendedor', y=['Precio Total', 'Costo Total Real','Utilidad'], barmode='group',text_auto=True,title='General')
        # CREACION DEL LAYOAUT PARA SELECCIONAR GRAFICOS
        fig.update_layout(
            updatemenus=[
                dict(
                    buttons=list([
                        dict(
                            args=["type", "histogram"],
                            label="Histograma",
                            method="restyle"
                        ),
                        dict(
                            args=["type", "scatter"],
                            label="Lineas",
                            method="restyle"
                        ),
                        dict(
                            args=["type", "box"],
                            label="Cajas",
                            method="restyle"
                        )
                    ]),
                    direction="down",
                )
            ]
        )

        df1.reset_index(inplace=True)
        donut_fig = px.pie(df, values='Precio Total',
                        names='Proveedor', hole=.3, title='General')
        fig_proov = px.histogram(df, x='Linea Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'], hover_name="Proveedor", title='General',barmode='group',text_auto=True)

        fig_date = px.line(df1, x="Fecha", y="Precio Total", title='General')
        fig_date.update_layout(hovermode="x unified")

        donut_fig.update_traces(textposition='inside')
        donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

        gantt_plot = plot(fig, output_type="div")
        gantt_donut = plot(donut_fig, output_type="div")
        gantt_proov = plot(fig_proov, output_type="div")
        gantt_time_line = plot(fig_date, output_type="div")

        vendedor_query = request.GET.getlist('vendedor')

        nomb_cliente_grupo1_query = request.GET.getlist('clientGrup1')
        nomb_cliente_grupo2_query = request.GET.getlist('clientgrup2')
        nomb_cliente_grupo3_query = request.GET.getlist('clientGrup3')
        nomb_cliente_grupo4_query = request.GET.getlist('clientGrup4')

        nomb_linea_grupo1_query = request.GET.getlist('lineG1')
        nomb_linea_grupo2_query = request.GET.getlist('lineG2')
        nomb_linea_grupo3_query = request.GET.getlist('lineG3')
        nomb_linea_grupo4_query = request.GET.getlist('lineG4')
        nomb_linea_grupo5_query = request.GET.getlist('lineG5')
        nomb_linea_grupo6_query = request.GET.getlist('lineG6')

        fecha_inicio_query = request.GET.get('since')
        fecha_final_query = request.GET.get('to')

        today=datetime.now()
        date_first_day="0%s/01/%s" % (today.month, today.year)

        date_actually = datetime.today().strftime('%m/%d/%Y')


        # CODIGO PARA LA CREACION DE CONTADOR DE DATOS PARA LOS DATA SETS-----------------------------------------------------------------------------------------------------------
        # CHECKS PARA VENDEDORES
        modelFcvendedor = pd.DataFrame(modelFcvendedor)
        modelFcvendedor = modelFcvendedor.pivot_table(index = ['nombrevendedor'], aggfunc ='size')
        modelFcvendedor = modelFcvendedor.to_frame()
        modelFcvendedor = modelFcvendedor.reset_index()
        modelFcvendedor = modelFcvendedor.rename(columns = {0:'Size'})
        modelFcvendedor = modelFcvendedor.to_dict('records')

        # CHECKS PARA LINEA GRUPO 1
        modelIvgrupo1 = pd.DataFrame(modelIvgrupo1)
        modelIvgrupo1 = modelIvgrupo1.pivot_table(index = ['descripciongrupo1lineas'], aggfunc ='size')
        modelIvgrupo1 = modelIvgrupo1.to_frame()
        modelIvgrupo1 = modelIvgrupo1.reset_index()
        modelIvgrupo1 = modelIvgrupo1.rename(columns = {0:'Size'})
        modelIvgrupo1 = modelIvgrupo1.to_dict('records')

        # CHECKS PARA LINEA GRUPO2
        modelIvgrupo2 = pd.DataFrame(modelIvgrupo2)
        modelIvgrupo2 = modelIvgrupo2.pivot_table(index = ['descripciongrupo2lineas'], aggfunc ='size')
        modelIvgrupo2 = modelIvgrupo2.to_frame()
        modelIvgrupo2 = modelIvgrupo2.reset_index()
        modelIvgrupo2 = modelIvgrupo2.rename(columns = {0:'Size'})
        modelIvgrupo2 = modelIvgrupo2.to_dict('records')

        # CHECKS PARA LINEA GRUPO 3
        modelIvgrupo3 = pd.DataFrame(modelIvgrupo3)
        modelIvgrupo3 = modelIvgrupo3.pivot_table(index = ['descripciongrupo3lineas'], aggfunc ='size')
        modelIvgrupo3 = modelIvgrupo3.to_frame()
        modelIvgrupo3 = modelIvgrupo3.reset_index()
        modelIvgrupo3 = modelIvgrupo3.rename(columns = {0:'Size'})
        modelIvgrupo3 = modelIvgrupo3.to_dict('records')

        # CHECK PARA LINEA GRUPO 4
        modelIvgrupo4 = pd.DataFrame(modelIvgrupo4)
        modelIvgrupo4 = modelIvgrupo4.pivot_table(index = ['descripciongrupo4lineas'], aggfunc ='size')
        modelIvgrupo4 = modelIvgrupo4.to_frame()
        modelIvgrupo4 = modelIvgrupo4.reset_index()
        modelIvgrupo4 = modelIvgrupo4.rename(columns = {0:'Size'})
        modelIvgrupo4 = modelIvgrupo4.to_dict('records')

        # CHECK PARA LINEA GRUPO 5
        modelIvgrupo5 = pd.DataFrame(modelIvgrupo5)
        modelIvgrupo5 = modelIvgrupo5.pivot_table(index = ['descripciongrupo5lineas'], aggfunc ='size')
        modelIvgrupo5 = modelIvgrupo5.to_frame()
        modelIvgrupo5 = modelIvgrupo5.reset_index()
        modelIvgrupo5 = modelIvgrupo5.rename(columns = {0:'Size'})
        modelIvgrupo5 = modelIvgrupo5.to_dict('records')

        # CHECK PARA LINEA GRUPO 6
        modelIvgrupo6 = pd.DataFrame(modelIvgrupo6)
        modelIvgrupo6 = modelIvgrupo6.pivot_table(index = ['descripciongrupo6lineas'], aggfunc ='size')
        modelIvgrupo6 = modelIvgrupo6.to_frame()
        modelIvgrupo6 = modelIvgrupo6.reset_index()
        modelIvgrupo6 = modelIvgrupo6.rename(columns = {0:'Size'})
        modelIvgrupo6 = modelIvgrupo6.to_dict('records')

        # CHECK PARA CLIENTE GRUPO 1
        modelPcgrupo1 = pd.DataFrame(modelPcgrupo1)
        modelPcgrupo1 = modelPcgrupo1.pivot_table(index = ['descripciong1cliente'], aggfunc ='size')
        modelPcgrupo1 = modelPcgrupo1.to_frame()
        modelPcgrupo1 = modelPcgrupo1.reset_index()
        modelPcgrupo1 = modelPcgrupo1.rename(columns = {0:'Size'})
        modelPcgrupo1 = modelPcgrupo1.to_dict('records')

        # CHECK PARA CLIENTE GRUPO 2
        modelPcgrupo2 = pd.DataFrame(modelPcgrupo2)
        modelPcgrupo2 = modelPcgrupo2.pivot_table(index = ['descripciong2cliente'], aggfunc ='size')
        modelPcgrupo2 = modelPcgrupo2.to_frame()
        modelPcgrupo2 = modelPcgrupo2.reset_index()
        modelPcgrupo2 = modelPcgrupo2.rename(columns = {0:'Size'})
        modelPcgrupo2 = modelPcgrupo2.to_dict('records')

        # CHECK PARA CLIENTE GRUPO 3
        modelPcgrupo3 = pd.DataFrame(modelPcgrupo3)
        modelPcgrupo3 = modelPcgrupo3.pivot_table(index = ['descripciong3cliente'], aggfunc ='size')
        modelPcgrupo3 = modelPcgrupo3.to_frame()
        modelPcgrupo3 = modelPcgrupo3.reset_index()
        modelPcgrupo3 = modelPcgrupo3.rename(columns = {0:'Size'})
        modelPcgrupo3 = modelPcgrupo3.to_dict('records')

        # CHECK PARA CLIENTE GRUPO 4
        modelPcgrupo4 = pd.DataFrame(modelPcgrupo4)
        modelPcgrupo4 = modelPcgrupo4.pivot_table(index = ['descripciong4cliente'], aggfunc ='size')
        modelPcgrupo4 = modelPcgrupo4.to_frame()
        modelPcgrupo4 = modelPcgrupo4.reset_index()
        modelPcgrupo4 = modelPcgrupo4.rename(columns = {0:'Size'})
        modelPcgrupo4 = modelPcgrupo4.to_dict('records')

        # CODIGO PARA LA CREACION DE LOS FILTROS -----------------------------------------------------------------------------------------
        # DATASETS
        data_frame_vendedor = pd.DataFrame()
        data_frame_grupo1_client = pd.DataFrame()
        data_frame_grupo2_client = pd.DataFrame()
        data_frame_grupo3_client = pd.DataFrame()
        data_frame_grupo4_client = pd.DataFrame()
        data_frame_grupo1_linea = pd.DataFrame()
        data_frame_grupo2_linea = pd.DataFrame()
        data_frame_grupo3_linea = pd.DataFrame()
        data_frame_grupo4_linea = pd.DataFrame()
        data_frame_grupo5_linea = pd.DataFrame()
        data_frame_grupo6_linea = pd.DataFrame()
        data_frame_date_inicio = pd.DataFrame()
        data_frame_date_final = pd.DataFrame()
        data_frame_date_range = pd.DataFrame()

        # CONSULTA DE VENDEDOR
        if vendedor_query != None and vendedor_query is not None:
            df_list = []
            for i in range(len(vendedor_query)):
                model_list = report_query.filter(nombrevendedor=vendedor_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_vendedor = pd.concat(df_list, sort='False', ignore_index='True')


        # CONSULTA DE CLIENTES
        # CONSULTA DE CLIENTES GRUPO 1
        if nomb_cliente_grupo1_query != None and nomb_cliente_grupo1_query is not None:
            df_list = []
            for i in range(len(nomb_cliente_grupo1_query)):
                model_list = report_query.filter(descripciong1cliente = nomb_cliente_grupo1_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_grupo1_client = pd.concat(df_list, sort='False', ignore_index='True')

        # CONSULTA DE CLIENTES GRUPO 2
        if nomb_cliente_grupo2_query != None and nomb_cliente_grupo2_query is not None:
            df_list = []
            for i in range(len(nomb_cliente_grupo2_query)):
                model_list = report_query.filter(descripciong2cliente=nomb_cliente_grupo2_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_grupo2_client = pd.concat(df_list, sort='False', ignore_index='True')

        # CONSULTA DE CLEINTES GRUPO3
        if nomb_cliente_grupo3_query != None and nomb_cliente_grupo3_query is not None:
            df_list = []
            for i in range(len(nomb_cliente_grupo3_query)):
                model_list = report_query.filter(descripciong3cliente=nomb_cliente_grupo3_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_grupo3_client = pd.concat(df_list, sort='False', ignore_index='True')

        # CUNSULTA DE CLIENTES GRUPO 4
        if nomb_cliente_grupo4_query != None and nomb_cliente_grupo4_query is not None:
            df_list = []
            for i in range(len(nomb_cliente_grupo4_query)):
                model_list = report_query.filter(descripciong4cliente=nomb_cliente_grupo4_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_grupo4_client = pd.concat(df_list, sort='False', ignore_index='True')


        # CONSULTA DE LINEAS
        # CONSULTA DE LINEAS GRUPO 1
        if nomb_linea_grupo1_query != None and nomb_linea_grupo1_query is not None:
            df_list = []
            for  i in range(len(nomb_linea_grupo1_query)):
                model_list = report_query.filter(descripciongrupo1lineas=nomb_linea_grupo1_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_grupo1_linea = pd.concat(df_list, sort='False', ignore_index='True')

        # CONSULTAS DE LINEAS GRUPO 2
        if nomb_linea_grupo2_query != None and nomb_linea_grupo2_query is not None:
            df_list = []
            for  i in range(len(nomb_linea_grupo2_query)):
                model_list = report_query.filter(descripciongrupo2lineas=nomb_linea_grupo2_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_grupo2_linea = pd.concat(df_list, sort='False', ignore_index='True')

        # CONSULTAS DE LINEAS GRUPO 3
        if nomb_linea_grupo3_query != None and nomb_linea_grupo3_query is not None:
            df_list = []
            for  i in range(len(nomb_linea_grupo3_query)):
                model_list = report_query.filter(descripciongrupo3lineas=nomb_linea_grupo3_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_grupo3_linea = pd.concat(df_list, sort='False', ignore_index='True')

        # CONSULTAS DE LINEAS GRUPO 4
        if nomb_linea_grupo4_query != None and nomb_linea_grupo4_query is not None:
            df_list = []
            for  i in range(len(nomb_linea_grupo4_query)):
                model_list = report_query.filter(descripciongrupo4lineas=nomb_linea_grupo4_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_grupo4_linea = pd.concat(df_list, sort='False', ignore_index='True')

        # CONSULTAS DE LINEAS GRUPO 5
        if nomb_linea_grupo5_query != None and nomb_linea_grupo5_query is not None:
            df_list = []
            for  i in range(len(nomb_linea_grupo5_query)):
                model_list = report_query.filter(descripciongrupo5lineas=nomb_linea_grupo5_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_grupo5_linea = pd.concat(df_list, sort='False', ignore_index='True')

        # CONSULTAS DE LINEAS GRUPO 6
        if nomb_linea_grupo6_query != None and nomb_linea_grupo6_query is not None:
            df_list = []
            for  i in range(len(nomb_linea_grupo6_query)):
                model_list = report_query.filter(descripciongrupo6lineas=nomb_linea_grupo6_query[i])
                projects_data = [
                    {
                        'Cantidad': (x.cantidad*-1),
                        'NombreVendedor': x.nombrevendedor,
                        'Precio Total': (x.preciorealtotal*-1),
                        'Proveedor': x.nombrecliente,
                        'Utilidad': (x.utilidad*-1),
                        'Costo Total Real': (x.costorealtotal*-1),
                        'Linea_Grupo1': x.descripciongrupo1lineas,
                        'Linea_Grupo2': x.descripciongrupo2lineas,
                        'Linea_Grupo3': x.descripciongrupo3lineas,
                        'Linea_Grupo4': x.descripciongrupo4lineas,
                        'Linea_Grupo5': x.descripciongrupo5lineas,
                        'Linea_Grupo6': x.descripciongrupo6lineas,
                        'Item': x.descripcionitem,
                        'Clinete_Grupo1': x.descripciong1cliente,
                        'Clinete_Grupo2': x.descripciong2cliente,
                        'Clinete_Grupo3': x.descripciong3cliente,
                        'Clinete_Grupo4': x.descripciong4cliente,
                        'Fecha': x.fechatrans,
                    } for x in model_list
                ]
                df_list.append(pd.DataFrame(projects_data))
                data_frame_grupo6_linea = pd.concat(df_list, sort='False', ignore_index='True')


        # CONSULTA DE FECHAS ------------------------------------------------------------------------------------------------------------------
        # CONSULTA DE FECHA INICIAL A FECHA FINAL
        if (fecha_final_query != None and fecha_inicio_query != None) and ( fecha_final_query != '' and fecha_inicio_query != '' ):
            date_since = datetime.strptime(fecha_inicio_query, '%m/%d/%Y')
            date_to = datetime.strptime(fecha_final_query, '%m/%d/%Y')
            model_list = report_query.filter(fechatrans__range=(date_since,date_to))
            print('ESTAS AQUI')
            projects_data = [
                {
                    'Cantidad': (x.cantidad*-1),
                    'NombreVendedor': x.nombrevendedor,
                    'Precio Total': (x.preciorealtotal*-1),
                    'Proveedor': x.nombrecliente,
                    'Utilidad': (x.utilidad*-1),
                    'Costo Total Real': (x.costorealtotal*-1),
                    'Linea_Grupo1': x.descripciongrupo1lineas,
                    'Linea_Grupo2': x.descripciongrupo2lineas,
                    'Linea_Grupo3': x.descripciongrupo3lineas,
                    'Linea_Grupo4': x.descripciongrupo4lineas,
                    'Linea_Grupo5': x.descripciongrupo5lineas,
                    'Linea_Grupo6': x.descripciongrupo6lineas,
                    'Item': x.descripcionitem,
                    'Clinete_Grupo1': x.descripciong1cliente,
                    'Clinete_Grupo2': x.descripciong2cliente,
                    'Clinete_Grupo3': x.descripciong3cliente,
                    'Clinete_Grupo4': x.descripciong4cliente,
                    'Fecha': x.fechatrans,
                } for x in model_list
            ]
            data_frame_date_range = pd.DataFrame(projects_data)
            df_sum = pd.DataFrame(data_frame_date_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df_sum.reset_index(inplace=True)
            
            df_rename = data_frame_date_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(data_frame_date_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0], fecha_inicio_query,title[1] ,fecha_final_query]),text_auto=True)

            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )

            donut_fig = px.pie(data_frame_date_range, values='Precio Total', names='Proveedor', hole=.3, title=str([title[0], fecha_inicio_query,title[1] ,fecha_final_query]))
            fig_proov = px.histogram(data_frame_date_range, x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'], hover_name="Linea_Grupo1", title=str([title[0], fecha_inicio_query,title[1] ,fecha_final_query]),barmode='group',text_auto=True)
            fig_date = px.line(df_sum, x="Fecha", y="Precio Total", title=str([title[0], fecha_inicio_query,title[1] ,fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        #  CONSULTAS COMBINADAS------------------------------------------------------------------------------------------------------------------------------------
        # COMBINACION ENTRE VENDEDOR Y EL RANGO ENTRE FECHAS
        if data_frame_vendedor.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_vend_fecha_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vend_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vend_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] , vendedor_query, title[1], fecha_inicio_query,title[2] ,fecha_final_query]),text_auto=True)

            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )

            donut_fig = px.pie(df_vend_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] , vendedor_query, title[1], fecha_inicio_query,title[2] ,fecha_final_query]))
            fig_proov = px.histogram(df_vend_fecha_range, x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'], hover_name="Linea_Grupo1", title=str([ title[0] , vendedor_query, title[1], fecha_inicio_query,title[2] ,fecha_final_query]),barmode='group',text_auto=True)
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] , vendedor_query, title[1], fecha_inicio_query,title[2] ,fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION DE CLIENTES 1 + FECHA INICIAL, FINAL, RANGO ...
        if data_frame_grupo1_client.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_cliente1_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_cliente1_fecha_range=data_frame_grupo1_client[(data_frame_grupo1_client["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_grupo1_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_cliente1_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_cliente1_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_cliente1_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] , nomb_cliente_grupo1_query, title[1] ,fecha_inicio_query, title[2], fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_cliente1_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] , nomb_cliente_grupo1_query, title[1] ,fecha_inicio_query, title[2], fecha_final_query]))
            fig_proov = px.histogram(df_cliente1_fecha_range, x='Linea Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'], hover_name="Linea_Grupo1", title=str([ title[0] , nomb_cliente_grupo1_query, title[1] ,fecha_inicio_query, title[2], fecha_final_query]),barmode='group',text_auto=True)
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] , nomb_cliente_grupo1_query, title[1] ,fecha_inicio_query, title[2], fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION DE CLIENTES 2  + FECHA INICIAL, FINA, RANGO ...

        if data_frame_grupo2_client.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_cliente2_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_cliente2_fecha_range=data_frame_grupo2_client[(data_frame_grupo2_client["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_grupo2_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_cliente2_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_cliente2_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_cliente2_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] , nomb_cliente_grupo2_query, title[1] ,fecha_inicio_query,title[2], fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_cliente2_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] , nomb_cliente_grupo2_query, title[1] ,fecha_inicio_query,title[2], fecha_final_query]))
            fig_proov = px.histogram(df_cliente2_fecha_range, x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'], hover_name="Linea_Grupo1", title=str([ title[0] , nomb_cliente_grupo2_query, title[1] ,fecha_inicio_query,title[2], fecha_final_query]),text_auto=True,barmode='group')
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] , nomb_cliente_grupo2_query, title[1] ,fecha_inicio_query,title[2], fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION DE CLEINTES 3 + FECHA INICIAL, FINAL, RANGO

        if data_frame_grupo3_client.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_cliente3_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_cliente3_fecha_range=data_frame_grupo3_client[(data_frame_grupo3_client["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_grupo3_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_cliente3_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_cliente3_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_cliente3_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_cliente_grupo3_query, title[1] ,fecha_inicio_query,title[2],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_cliente3_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_cliente_grupo3_query, title[1] ,fecha_inicio_query,title[2],fecha_final_query]))
            fig_proov = px.histogram(df_cliente3_fecha_range, x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True, hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_cliente_grupo3_query, title[1] ,fecha_inicio_query,title[2],fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_cliente_grupo3_query, title[1] ,fecha_inicio_query,title[2],fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION DE CLIENTE 4 + FECHA INICIAL, FINAL, RANGO

        if data_frame_grupo4_client.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_cliente4_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_cliente4_fecha_range=data_frame_grupo4_client[(data_frame_grupo4_client["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_grupo4_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_cliente4_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_cliente4_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_cliente4_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0],  nomb_cliente_grupo4_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_cliente4_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0],  nomb_cliente_grupo4_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            fig_proov = px.histogram(df_cliente4_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0],  nomb_cliente_grupo4_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0],  nomb_cliente_grupo4_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACIONES ENTRE LINEA G1 Y LINEA G2, G3, G4, G5, G6, FECHA INICIO, FECHA FINAL, RANGO DE FECHA, CLIENTE G1, G2, G3, G4

        if data_frame_grupo1_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_linea1_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_linea1_fecha_range=data_frame_grupo1_linea[(data_frame_grupo1_linea["Linea_Grupo1"].isin(nomb_linea_grupo1_query))&(data_frame_grupo1_linea["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_linea1_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_linea1_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')


            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_linea1_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_linea_grupo1_query, title[1] , fecha_inicio_query, title[2],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_linea1_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_linea_grupo1_query, title[1] , fecha_inicio_query, title[2],fecha_final_query]))
            fig_proov = px.histogram(df_linea1_fecha_range, x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True, hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_linea_grupo1_query, title[1] , fecha_inicio_query, title[2],fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_linea_grupo1_query, title[1] , fecha_inicio_query, title[2],fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION ENTRE LINEA G2 Y G3, G4, G5, G6, FECHA INICIO, RANGO, CLIENTE G1, G2, G3, G4
        if data_frame_grupo2_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_linea2_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_linea2_fecha_range=data_frame_grupo2_linea[(data_frame_grupo2_linea["Linea_Grupo2"].isin(nomb_linea_grupo2_query))&(data_frame_grupo2_linea["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_linea2_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_linea2_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_linea2_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_linea_grupo2_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_linea2_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_linea_grupo2_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            fig_proov = px.histogram(df_linea2_fecha_range, x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_linea_grupo2_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_linea_grupo2_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION ENTRE LINEA G3 Y G4, G5, G6, FECHA INICIAL, FECHA FINAL, RANGO, CLIENTE G1, G2, G3, G4
        if data_frame_grupo3_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_linea3_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_linea3_fecha_range=data_frame_grupo3_linea[(data_frame_grupo3_linea["Linea_Grupo3"].isin(nomb_linea_grupo3_query))&(data_frame_grupo3_linea["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_linea3_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_linea3_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_linea3_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_linea_grupo3_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_linea3_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_linea_grupo3_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            fig_proov = px.histogram(df_linea3_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True, hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_linea_grupo3_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_linea_grupo3_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION ENTRE LINEA G4 Y G5, G6, FECHA INICIAL, FINAL, RANGO, CLIENTE G1, G2, G3 ,G4
        if data_frame_grupo4_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_linea4_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_linea4_fecha_range=data_frame_grupo4_linea[(data_frame_grupo4_linea["Linea_Grupo4"].isin(nomb_linea_grupo4_query))&(data_frame_grupo4_linea["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_linea4_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()


            df_rename = df_linea4_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_linea4_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0], nomb_linea_grupo4_query, title[1] , fecha_inicio_query, title[2],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_linea4_fecha_range,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0], nomb_linea_grupo4_query, title[1] , fecha_inicio_query, title[2],fecha_final_query]))
            fig_proov = px.histogram(df_linea4_fecha_range, x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True, hover_name="Linea_Grupo1", title=str([title[0], nomb_linea_grupo4_query, title[1] , fecha_inicio_query, title[2],fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([title[0], nomb_linea_grupo4_query, title[1] , fecha_inicio_query, title[2],fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION ENTRE LINEA G5 Y G6, INICIAL, FINAL, RANGO, CLIENTE G1, G2, G3, G4
        if data_frame_grupo5_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_linea5_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_linea5_fecha_range=data_frame_grupo5_linea[(data_frame_grupo5_linea["Linea_Grupo5"].isin(nomb_linea_grupo5_query))&(data_frame_grupo5_linea["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_linea5_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_linea5_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_linea5_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_linea_grupo5_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_linea5_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_linea_grupo5_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            fig_proov = px.histogram(df_linea5_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True, hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_linea_grupo5_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_linea_grupo5_query, title[1] ,fecha_inicio_query, title[2],fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION ENTRE LINEA G6 y FECHA DE INICIO, FINAL, RANGO, CLIENTE G1, G2, G3, G4

        if data_frame_grupo6_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_linea6_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_linea6_fecha_range=data_frame_grupo6_linea[(data_frame_grupo6_linea["Linea_Grupo6"].isin(nomb_linea_grupo6_query))&(data_frame_grupo6_linea["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_linea6_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_linea6_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_linea6_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_linea_grupo6_query, title[1] ,fecha_inicio_query, title[2], fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_linea6_fecha_range,values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_linea_grupo6_query, title[1] ,fecha_inicio_query, title[2], fecha_final_query]))
            fig_proov = px.histogram(df_linea6_fecha_range, x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_linea_grupo6_query, title[1] ,fecha_inicio_query, title[2], fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_linea_grupo6_query, title[1] ,fecha_inicio_query, title[2], fecha_final_query]))
            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION CLIENTE G1 MAS FECHAS DE INICIO, FECHA Y RANGE
        # COMBINACION TRIPLE -------------------------------------------------------------------------------------------------------------------------------

        # COMBINACION TRIPLE DE VENDEDOR + LINEA 1 + RANGO
        if data_frame_vendedor.empty == False and data_frame_grupo1_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_linea1_fecha_rango= pd.concat(df_list ,ignore_index='True')
            df_vend_linea1_fecha_rango=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Linea_Grupo1"].isin(nomb_linea_grupo1_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vend_linea1_fecha_rango.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()


            df_rename = df_vend_linea1_fecha_rango.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_linea1_fecha_rango, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo1_query, title[2] ,fecha_inicio_query, title[3] , fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vend_linea1_fecha_rango, values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo1_query, title[2] ,fecha_inicio_query, title[3] , fecha_final_query]))
            fig_proov = px.histogram(df_vend_linea1_fecha_rango,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo1_query, title[2] ,fecha_inicio_query, title[3] , fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo1_query, title[2] ,fecha_inicio_query, title[3] , fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE DE VENDEDOR + LINEA 2 + RANGO
        if data_frame_vendedor.empty == False and data_frame_grupo2_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_linea2_fecha_rango= pd.concat(df_list ,ignore_index='True')
            df_vend_linea2_fecha_rango=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Linea_Grupo2"].isin(nomb_linea_grupo2_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vend_linea2_fecha_rango.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()


            df_rename = df_vend_linea2_fecha_rango.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_linea2_fecha_rango, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] , vendedor_query, title[1] ,nomb_linea_grupo2_query, title[2] ,fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vend_linea2_fecha_rango,values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] , vendedor_query, title[1] ,nomb_linea_grupo2_query, title[2] ,fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_vend_linea2_fecha_rango,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] , vendedor_query, title[1] ,nomb_linea_grupo2_query, title[2] ,fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] , vendedor_query, title[1] ,nomb_linea_grupo2_query, title[2] ,fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION TRIPLE DE VENDEDOR + LINEA 3 + RANGO
        if data_frame_vendedor.empty == False and data_frame_grupo3_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_linea3_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_vend_linea3_fecha_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Linea_Grupo3"].isin(nomb_linea_grupo3_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]


            df1 = pd.DataFrame(df_vend_linea3_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vend_linea3_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_linea3_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo3_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vend_linea3_fecha_range,values='Precio Total',names='Proveedor', hole=.3, title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo3_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_vend_linea3_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo3_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo3_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE DE VENDEDOR + LINEA 4 + RANGO

        if data_frame_vendedor.empty == False and data_frame_grupo4_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_linea4_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_vend_linea4_fecha_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Linea_Grupo4"].isin(nomb_linea_grupo4_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vend_linea4_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vend_linea4_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_linea4_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo4_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vend_linea4_fecha_range,values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo4_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_vend_linea4_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo4_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo4_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION TRIPLE DE VENDEDOR + LINEA 5 + RANGO

        if data_frame_vendedor.empty == False and data_frame_grupo5_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_linea5_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_vend_linea5_fecha_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Linea_Grupo5"].isin(nomb_linea_grupo5_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vend_linea5_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vend_linea5_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_linea5_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo5_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vend_linea5_fecha_range,values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo5_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_vend_linea5_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo5_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([ title[0] ,vendedor_query, title[1] ,nomb_linea_grupo5_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE DE VENDEDOR + LINEA 6 + RANGO
        if data_frame_vendedor.empty == False and data_frame_grupo6_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_linea6_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_vend_linea6_fecha_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Linea_Grupo6"].isin(nomb_linea_grupo6_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vend_linea6_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vend_linea6_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_linea6_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0], vendedor_query, title[1], nomb_linea_grupo6_query, title[2],fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vend_linea6_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([title[0], vendedor_query, title[1], nomb_linea_grupo6_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_vend_linea6_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0], vendedor_query, title[1], nomb_linea_grupo6_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1, x="Fecha",y="Precio Total", title=str([title[0], vendedor_query, title[1], nomb_linea_grupo6_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE VENDEDOR + CLIENTE 1  RANGO

        if data_frame_vendedor.empty == False and data_frame_grupo1_client.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_client1_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_vend_client1_fecha_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vend_client1_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vend_client1_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor','Clientes:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_client1_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0] ,vendedor_query, title[1] ,nomb_cliente_grupo1_query,title[2],fecha_inicio_query,title[3] ,fecha_final_query]),text_auto=True)
            donut_fig = px.pie(df_vend_client1_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([title[0] ,vendedor_query, title[1] ,nomb_cliente_grupo1_query,title[2],fecha_inicio_query,title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_vend_client1_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0] ,vendedor_query, title[1] ,nomb_cliente_grupo1_query,title[2],fecha_inicio_query,title[3] ,fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([title[0] ,vendedor_query, title[1] ,nomb_cliente_grupo1_query,title[2],fecha_inicio_query,title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION TRIPLE VENDEDOR + CLIENTE 2  RANGO ...

        if data_frame_vendedor.empty == False and data_frame_grupo2_client.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_client2_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_vend_client2_fecha_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vend_client2_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vend_client2_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor','Clientes:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_client2_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo2_query,title[2],fecha_inicio_query,title[3] ,fecha_final_query]),text_auto=True)
            donut_fig = px.pie(df_vend_client2_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo2_query,title[2],fecha_inicio_query,title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_vend_client2_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Proveedor", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo2_query,title[2],fecha_inicio_query,title[3] ,fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo2_query,title[2],fecha_inicio_query,title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION TRIPLE VENDEDOR + CLIENTE 3  RANGO ..

        if data_frame_vendedor.empty == False and data_frame_grupo3_client.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_client3_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_vend_client3_fecha_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vend_client3_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vend_client3_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor','Clientes:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_client3_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query,title[2], fecha_inicio_query,title[3] ,fecha_final_query]),text_auto=True)
            donut_fig = px.pie(df_vend_client3_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query,title[2], fecha_inicio_query,title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_vend_client3_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query,title[2], fecha_inicio_query,title[3] ,fecha_final_query]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query,title[2], fecha_inicio_query,title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE VENDEDOR + CLIENTE 4  RANGO ...

        if data_frame_vendedor.empty == False and data_frame_grupo4_client.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_vend_client4_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_vend_client4_fecha_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vend_client4_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vend_client4_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor','Clientes:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vend_client4_fecha_range, x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query, title[2]
                            , fecha_inicio_query,title[3] ,fecha_final_query]),text_auto=True)
            donut_fig = px.pie(df_vend_client4_fecha_range, values='Precio Total', names='Proveedor', hole=.3, title=str([vendedor_query, nomb_cliente_grupo4_query
            , fecha_inicio_query ,fecha_final_query ]))
            fig_proov = px.histogram(df_vend_client4_fecha_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([vendedor_query, nomb_cliente_grupo4_query
                            , fecha_inicio_query ,fecha_final_query,]))
            fig_date = px.line(df1, x="Fecha", y="Precio Total", title=str([vendedor_query, nomb_cliente_grupo4_query
            , fecha_inicio_query ,fecha_final_query ]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE G1 + LINEA 1 + FECHA INICIAL, FINAL

        if data_frame_grupo1_client.empty == False and data_frame_grupo1_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client1_linea1_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client1_linea1_fecha_range=data_frame_grupo1_client[(data_frame_grupo1_client["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_grupo1_client["Linea_Grupo1"].isin(nomb_linea_grupo1_query))&(data_frame_grupo1_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client1_linea1_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client1_linea1_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client1_linea1_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo1_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client1_linea1_fecha_range , values='Cantidad', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo1_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_client1_linea1_fecha_range , x="Cantidad", y="Proveedor",
                            color='Item', hover_name="Proveedor", title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo1_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Cantidad", title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo1_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE G1 + LINEA 2 + FECHA INICIAL, FECHA FINAL

        if data_frame_grupo1_client.empty == False and data_frame_grupo2_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client1_linea2_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client1_linea2_fecha_range=data_frame_grupo1_client[(data_frame_grupo1_client["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_grupo1_client["Linea_Grupo2"].isin(nomb_linea_grupo2_query))&(data_frame_grupo1_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client1_linea2_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client1_linea2_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client1_linea2_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] , nomb_linea_grupo2_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client1_linea2_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] , nomb_linea_grupo2_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_client1_linea2_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] , nomb_linea_grupo2_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] , nomb_linea_grupo2_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION TRIPLE CLIENTE G1 + LINEA 3 + FECHA INICIAL, FECHA FINAL....

        if data_frame_grupo1_client.empty == False and data_frame_grupo3_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client1_linea3_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client1_linea3_fecha_range=data_frame_grupo1_client[(data_frame_grupo1_client["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_grupo1_client["Linea_Grupo3"].isin(nomb_linea_grupo3_query))&(data_frame_grupo1_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client1_linea3_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client1_linea3_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client1_linea3_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_cliente_grupo1_query, title[1],nomb_linea_grupo3_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client1_linea3_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_cliente_grupo1_query, title[1],nomb_linea_grupo3_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_client1_linea3_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_cliente_grupo1_query, title[1],nomb_linea_grupo3_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_cliente_grupo1_query, title[1],nomb_linea_grupo3_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE G1 + LINEA 4 + FECHA INICIAL, FINAL, RANGO ......

        if data_frame_grupo1_client.empty == False and data_frame_grupo4_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client1_linea4_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client1_linea4_fecha_range=data_frame_grupo1_client[(data_frame_grupo1_client["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_grupo1_client["Linea_Grupo4"].isin(nomb_linea_grupo4_query))&(data_frame_grupo1_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client1_linea4_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client1_linea4_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client1_linea4_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo4_query, title[2],fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client1_linea4_fecha_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo4_query, title[2],fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_client1_linea4_fecha_range , x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo4_query, title[2],fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo4_query, title[2],fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        if data_frame_grupo1_client.empty == False and data_frame_grupo5_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client1_linea5_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client1_linea5_fecha_range=data_frame_grupo1_client[(data_frame_grupo1_client["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_grupo1_client["Linea_Grupo5"].isin(nomb_linea_grupo5_query))&(data_frame_grupo1_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client1_linea5_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client1_linea5_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client1_linea5_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo5_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client1_linea5_fecha_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo5_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_client1_linea5_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo5_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_cliente_grupo1_query, title[1] ,nomb_linea_grupo5_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE G1 + LINEA 6 + FECHA INICIAL, FINAL RANGO ...

        if data_frame_grupo1_client.empty == False and data_frame_grupo6_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client1_linea6_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client1_linea6_fecha_range=data_frame_grupo1_client[(data_frame_grupo1_client["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_grupo1_client["Linea_Grupo6"].isin(nomb_linea_grupo6_query))&(data_frame_grupo1_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client1_linea6_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client1_linea6_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client1_linea6_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] , nomb_cliente_grupo1_query,title[1] ,nomb_linea_grupo6_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client1_linea6_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] , nomb_cliente_grupo1_query,title[1] ,nomb_linea_grupo6_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_client1_linea6_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] , nomb_cliente_grupo1_query,title[1] ,nomb_linea_grupo6_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([ title[0] , nomb_cliente_grupo1_query,title[1] ,nomb_linea_grupo6_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE G2 + LINEA 1 + FECHA INICIAL, FINAL, RANGO ...

        if data_frame_grupo2_client.empty == False and data_frame_grupo1_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client2_linea1_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client2_linea1_fecha_range=data_frame_grupo2_client[(data_frame_grupo2_client["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_grupo2_client["Linea_Grupo1"].isin(nomb_linea_grupo1_query))&(data_frame_grupo2_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client2_linea1_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client2_linea1_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client2_linea1_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_cliente_grupo2_query, title[1] ,nomb_linea_grupo1_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client2_linea1_fecha_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_cliente_grupo2_query, title[1] ,nomb_linea_grupo1_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_client2_linea1_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_cliente_grupo2_query, title[1] ,nomb_linea_grupo1_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_cliente_grupo2_query, title[1] ,nomb_linea_grupo1_query, title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE G2 + LINEA 2 + FECHA INICIAL, FINAL, RANGO ...

        if data_frame_grupo2_client.empty == False and data_frame_grupo2_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client2_linea2_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client2_linea2_fecha_range=data_frame_grupo2_client[(data_frame_grupo2_client["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_grupo2_client["Linea_Grupo2"].isin(nomb_linea_grupo2_query))&(data_frame_grupo2_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client2_linea2_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client2_linea2_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client2_linea2_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_cliente_grupo2_query, title[1] ,nomb_linea_grupo2_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client2_linea2_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_cliente_grupo2_query, title[1] ,nomb_linea_grupo2_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_client2_linea2_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_cliente_grupo2_query, title[1] ,nomb_linea_grupo2_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_cliente_grupo2_query, title[1] ,nomb_linea_grupo2_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE G2 + LINEA 3 + FECHA INICIAL, FINAL, RANGO ...

        if data_frame_grupo2_client.empty == False and data_frame_grupo3_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client2_linea3_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client2_linea3_fecha_range=data_frame_grupo2_client[(data_frame_grupo2_client["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_grupo2_client["Linea_Grupo3"].isin(nomb_linea_grupo3_query))&(data_frame_grupo2_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client2_linea3_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client2_linea3_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client2_linea3_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_cliente_grupo2_query,title[1] ,nomb_linea_grupo3_query,title[2], fecha_inicio_query,title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client2_linea3_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_cliente_grupo2_query,title[1] ,nomb_linea_grupo3_query,title[2], fecha_inicio_query,title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_client2_linea3_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_cliente_grupo2_query,title[1] ,nomb_linea_grupo3_query,title[2], fecha_inicio_query,title[3] ,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([ title[0] ,nomb_cliente_grupo2_query,title[1] ,nomb_linea_grupo3_query,title[2], fecha_inicio_query,title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE G2 + LINEA 4 + FECHA INICIAL, FECHA FINAL, RANGO ...

        if data_frame_grupo2_client.empty == False and data_frame_grupo4_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client2_linea4_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client2_linea4_fecha_range=data_frame_grupo2_client[(data_frame_grupo2_client["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_grupo2_client["Linea_Grupo4"].isin(nomb_linea_grupo4_query))&(data_frame_grupo2_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client2_linea4_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client2_linea4_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client2_linea4_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([ title[0] ,nomb_cliente_grupo2_query,title[1] ,nomb_linea_grupo4_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client2_linea4_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([ title[0] ,nomb_cliente_grupo2_query,title[1] ,nomb_linea_grupo4_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_proov = px.histogram(df_client2_linea4_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([ title[0] ,nomb_cliente_grupo2_query,title[1] ,nomb_linea_grupo4_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([ title[0] ,nomb_cliente_grupo2_query,title[1] ,nomb_linea_grupo4_query,title[2], fecha_inicio_query, title[3] ,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE G2 + LINEA 5 + FECHA INICIAL, FECHA FINAL, RANGO ...

        if data_frame_grupo2_client.empty == False and data_frame_grupo5_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client2_linea5_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client2_linea5_fecha_range=data_frame_grupo2_client[(data_frame_grupo2_client["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_grupo2_client["Linea_Grupo5"].isin(nomb_linea_grupo5_query))&(data_frame_grupo2_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client2_linea5_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client2_linea5_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client2_linea5_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo5_query,title[3], fecha_inicio_query,fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client2_linea5_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo5_query,title[3], fecha_inicio_query,fecha_final_query]))
            fig_proov = px.histogram(df_client2_linea5_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo5_query,title[3], fecha_inicio_query,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo5_query,title[3], fecha_inicio_query,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE G2 + LINEA 6 + FECHA INICIAL, FINAL, REANGO ...

        if data_frame_grupo2_client.empty == False and data_frame_grupo6_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client2_linea6_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client2_linea6_fecha_range=data_frame_grupo2_client[(data_frame_grupo2_client["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_grupo2_client["Linea_Grupo6"].isin(nomb_linea_grupo6_query))&(data_frame_grupo2_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client2_linea6_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client2_linea6_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Cliente2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client2_linea6_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo2_query,title[1], nomb_linea_grupo6_query,title[2], fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client2_linea6_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo2_query,title[1], nomb_linea_grupo6_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client2_linea6_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo2_query,title[1], nomb_linea_grupo6_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],nomb_cliente_grupo2_query,title[1], nomb_linea_grupo6_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

            # COMBINACION CON CLIENTE G3 -----------------------------------------------------------------------------------------------------------
        # COMBINACION TRIPLE CLIENTE G3 + LINEA 1 + RANGO ....

        if data_frame_grupo3_client.empty == False and data_frame_grupo1_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client3_linea1_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client3_linea1_fecha_range=data_frame_grupo3_client[(data_frame_grupo3_client["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_grupo3_client["Linea_Grupo1"].isin(nomb_linea_grupo1_query))&(data_frame_grupo3_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client3_linea1_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client3_linea1_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Cliente2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client3_linea1_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo1_query,title[2], fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client3_linea1_fecha_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo1_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client3_linea1_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo1_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo1_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION TRIPLE CLIENTE G3 + LINEA 2 + RANGO ...

        if data_frame_grupo3_client.empty == False and data_frame_grupo2_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client3_linea2_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client3_linea2_fecha_range=data_frame_grupo3_client[(data_frame_grupo3_client["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_grupo3_client["Linea_Grupo2"].isin(nomb_linea_grupo2_query))&(data_frame_grupo3_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client3_linea2_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client3_linea2_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client3_linea2_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo2_query, title[2],fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client3_linea2_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo2_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client3_linea2_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo2_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo2_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE G3 + LINEA 3 + FECHA INICIAL, FINAL, RANGO ...

        if data_frame_grupo3_client.empty == False and data_frame_grupo3_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client3_linea3_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client3_linea3_fecha_range=data_frame_grupo3_client[(data_frame_grupo3_client["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_grupo3_client["Linea_Grupo3"].isin(nomb_linea_grupo3_query))&(data_frame_grupo3_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client3_linea3_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client3_linea3_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client3_linea3_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo3_query,title[2], fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client3_linea3_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([nomb_cliente_grupo3_query, nomb_linea_grupo3_query, fecha_inicio_query,fecha_final_query]))
            fig_proov = px.histogram(df_client3_linea3_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([nomb_cliente_grupo3_query, nomb_linea_grupo3_query, fecha_inicio_query,fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([nomb_cliente_grupo3_query, nomb_linea_grupo3_query, fecha_inicio_query,fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION TRIPLE G3 + LINEA 4 + FECHA INICIAL, FINAL, RANGO ...

        if data_frame_grupo3_client.empty == False and data_frame_grupo4_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client3_linea4_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client3_linea4_fecha_range=data_frame_grupo3_client[(data_frame_grupo3_client["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_grupo3_client["Linea_Grupo4"].isin(nomb_linea_grupo4_query))&(data_frame_grupo3_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client3_linea4_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client3_linea4_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client3_linea4_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo4_query, title[2],fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client3_linea4_fecha_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo4_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client3_linea4_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo4_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo4_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")



        # COMBINACION TRIPLE CLIENTE G3 + LINEA 5 + FECHA INICIAL, FINAL, RANGO ...

        if data_frame_grupo3_client.empty == False and data_frame_grupo5_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client3_linea5_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client3_linea5_fecha_range=data_frame_grupo3_client[(data_frame_grupo3_client["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_grupo3_client["Linea_Grupo5"].isin(nomb_linea_grupo5_query))&(data_frame_grupo3_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]


            df1 = pd.DataFrame(df_client3_linea5_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client3_linea5_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client3_linea5_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo5_query, title[2],fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client3_linea5_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo5_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client3_linea5_fecha_range , x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo5_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],nomb_cliente_grupo3_query,title[1], nomb_linea_grupo5_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")



        # COMBINACION TRIPLE CLIENTE G3 + LINEA 6 + FECHA INICIAL, FINAL, RANGO ...

        if data_frame_grupo3_client.empty == False and data_frame_grupo6_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client3_linea6_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client3_linea6_fecha_range=data_frame_grupo3_client[(data_frame_grupo3_client["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_grupo3_client["Linea_Grupo6"].isin(nomb_linea_grupo6_query))&(data_frame_grupo3_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client3_linea6_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client3_linea6_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client3_linea6_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo3_query, title[1],nomb_linea_grupo6_query, title[2],fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client3_linea6_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo3_query, title[1],nomb_linea_grupo6_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client3_linea6_fecha_range , x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo3_query, title[1],nomb_linea_grupo6_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],nomb_cliente_grupo3_query, title[1],nomb_linea_grupo6_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")



        # COMBINACION DEL CLIENTE 4  --------------------------------------------
        # COMBINACION TRIPLE CLIENTE 4 + LINEA 1 + FECHA INICIO, FINAL, RANGO ...

        if data_frame_grupo4_client.empty == False and data_frame_grupo1_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client4_linea1_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client4_linea1_fecha_range=data_frame_grupo4_client[(data_frame_grupo4_client["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_grupo4_client["Linea_Grupo1"].isin(nomb_linea_grupo1_query))&(data_frame_grupo4_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client4_linea1_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client4_linea1_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client4_linea1_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo1_query,title[2], fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client4_linea1_fecha_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo1_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client4_linea1_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo1_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo1_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE 4 + LINEA 2 + FECHA INICIO, FINAL, RANGO ...

        if data_frame_grupo4_client.empty == False and data_frame_grupo2_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client4_linea2_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client4_linea2_fecha_range=data_frame_grupo4_client[(data_frame_grupo4_client["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_grupo4_client["Linea_Grupo2"].isin(nomb_linea_grupo2_query))&(data_frame_grupo4_client["Fecha"].between(fecha_inicio_query))]

            df1 = pd.DataFrame(df_client4_linea2_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client4_linea2_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client4_linea2_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo2_query, title[2],fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client4_linea2_fecha_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo2_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client4_linea2_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo2_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo2_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE 4 + LINEA  3 + FECHA INICIO, FINAL, RANGO ...

        if data_frame_grupo4_client.empty == False and data_frame_grupo3_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client4_linea3_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client4_linea3_fecha_range=data_frame_grupo4_client[(data_frame_grupo4_client["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_grupo4_client["Linea_Grupo3"].isin(nomb_linea_grupo3_query))&(data_frame_grupo4_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]


            df1 = pd.DataFrame(df_client4_linea3_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client4_linea3_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client4_linea3_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo3_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client4_linea3_fecha_range , values='Cantidad', names='Item', hole=.3, title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo3_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client4_linea3_fecha_range , x="Cantidad", y="Proveedor",
                            color='Item', hover_name="Proveedor", title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo3_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Cantidad", title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo3_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")



        # COMBINACION TRIPLE CLIENTE 4 + LINEA 4 + FECHA INICIO, FINAL, RANGO ...

        if data_frame_grupo4_client.empty == False and data_frame_grupo4_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client4_linea4_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client4_linea4_fecha_range=data_frame_grupo4_client[(data_frame_grupo4_client["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_grupo4_client["Linea_Grupo4"].isin(nomb_linea_grupo4_query))&(data_frame_grupo4_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]


            df1 = pd.DataFrame(df_client4_linea4_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client4_linea4_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client4_linea4_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo4_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client4_linea4_fecha_range , values='Cantidad', names='Item', hole=.3, title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo4_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client4_linea4_fecha_range , x="Cantidad", y="Proveedor",
                            color='Item', hover_name="Proveedor", title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo4_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Cantidad", title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo4_query, title[2],fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")



        # COMBINACION TRIPLE CLIENTE 4 + LINEA 5 + FECHA INICIO, FINAL, RANGO ...

        if data_frame_grupo4_client.empty == False and data_frame_grupo5_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client4_linea5_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client4_linea5_fecha_range=data_frame_grupo4_client[(data_frame_grupo4_client["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_grupo4_client["Linea_Grupo5"].isin(nomb_linea_grupo5_query))&(data_frame_grupo4_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]


            df1 = pd.DataFrame(df_client4_linea5_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client4_linea5_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_client4_linea5_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo5_query,title[2], fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client4_linea5_fecha_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo5_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client4_linea5_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo5_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([title[0],nomb_cliente_grupo4_query,title[1], nomb_linea_grupo5_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION TRIPLE CLIENTE 4 + LINEA 6 + FECHA INICIO, FINAL, RANGO ...

        if data_frame_grupo4_client.empty == False and data_frame_grupo6_linea.empty == False and data_frame_date_range.empty == False:
            df_list.append(pd.DataFrame(projects_data))
            df_client4_linea6_fecha_range= pd.concat(df_list ,ignore_index='True')
            df_client4_linea6_fecha_range=data_frame_grupo4_client[(data_frame_grupo4_client["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_grupo4_client["Linea_Grupo6"].isin(nomb_linea_grupo6_query))&(data_frame_grupo4_client["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_client4_linea6_fecha_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_client4_linea6_fecha_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_client4_linea6_fecha_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo6_query,title[2], fecha_inicio_query,title[3],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_client4_linea6_fecha_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo6_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_proov = px.histogram(df_client4_linea6_fecha_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo6_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],nomb_cliente_grupo4_query, title[1],nomb_linea_grupo6_query,title[2], fecha_inicio_query,title[3],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")



        # COMBINACION COMPLETA DE VENDEDOR, CLIENTE, LINEAS, FECHAS --------------------------------------------------------------------------------------------------------
        # COMBINACION VENDEDOR, CLIENTE 1 , LINEAS 1 , FECHAS INICIO + FINAL + RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo1_client.empty == False) and (data_frame_grupo1_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client1_linea1_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client1_linea1_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_vendedor["Linea_Grupo1"].isin(nomb_linea_grupo1_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client1_linea1_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client1_linea1_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vendedor_client1_linea1_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query,title[2], nomb_linea_grupo1_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client1_linea1_range , values='Precio Total', names='Proveedor', hole=.3, title=([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query,title[2], nomb_linea_grupo1_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client1_linea1_range , x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True, hover_name="Linea_Grupo1", title=([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query,title[2], nomb_linea_grupo1_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query,title[2], nomb_linea_grupo1_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION VENDEDOR + CLIENTE 1, LINEA 2, FECHA INICIAL + FINAL+ RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo1_client.empty == False) and (data_frame_grupo2_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client1_linea2_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client1_linea2_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_vendedor["Linea_Grupo2"].isin(nomb_linea_grupo2_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client1_linea2_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client1_linea2_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vendedor_client1_linea2_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo1_query, title[2],nomb_linea_grupo2_query,title[3],fecha_inicio_query,title[4], fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client1_linea2_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo1_query, title[2],nomb_linea_grupo2_query,title[3],fecha_inicio_query,title[4], fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client1_linea2_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo1_query, title[2],nomb_linea_grupo2_query,title[3],fecha_inicio_query,title[4], fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo1_query, title[2],nomb_linea_grupo2_query,title[3],fecha_inicio_query,title[4], fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION VENDEDOR, CLIENTE 1 + LINEA 3 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo1_client.empty == False) and (data_frame_grupo3_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client1_linea3_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client1_linea3_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_vendedor["Linea_Grupo3"].isin(nomb_linea_grupo3_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client1_linea3_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client1_linea3_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client1_linea3_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo1_query, title[2],nomb_linea_grupo3_query,title[3],fecha_inicio_query, title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client1_linea3_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo1_query, title[2],nomb_linea_grupo3_query,title[3],fecha_inicio_query, title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client1_linea3_range , x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo1_query, title[2],nomb_linea_grupo3_query,title[3],fecha_inicio_query, title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo1_query, title[2],nomb_linea_grupo3_query,title[3],fecha_inicio_query, title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR, CLIENTE 1 + LINEA 4 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo1_client.empty == False) and (data_frame_grupo4_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client1_linea4_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client1_linea4_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_vendedor["Linea_Grupo4"].isin(nomb_linea_grupo4_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query) )]

            df1 = pd.DataFrame(df_vendedor_client1_linea4_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client1_linea4_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client1_linea4_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query, title[2],nomb_linea_grupo4_query,title[3],fecha_inicio_query,title[4], fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client1_linea4_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query, title[2],nomb_linea_grupo4_query,title[3],fecha_inicio_query,title[4], fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client1_linea4_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query, title[2],nomb_linea_grupo4_query,title[3],fecha_inicio_query,title[4], fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query, title[2],nomb_linea_grupo4_query,title[3],fecha_inicio_query,title[4], fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")



        # COMBINACION VENDEDOR, CLIENTE 1 , LINEA 5 , FECHA INICIAL + FECHA FINAL + RANGO....

        if (data_frame_vendedor.empty == False and data_frame_grupo1_client.empty == False) and (data_frame_grupo5_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client1_linea5_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client1_linea5_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_vendedor["Linea_Grupo5"].isin(nomb_linea_grupo5_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client1_linea5_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client1_linea5_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client1_linea5_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query,title[2], nomb_linea_grupo5_query,title[3],fecha_inicio_query, title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client1_linea5_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query,title[2], nomb_linea_grupo5_query,title[3],fecha_inicio_query, title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client1_linea5_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query,title[2], nomb_linea_grupo5_query,title[3],fecha_inicio_query, title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query,title[2], nomb_linea_grupo5_query,title[3],fecha_inicio_query, title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION VENDEDOR, CLIENTE 1, LINEA 6, FECHA INICIAL, FINAL Y RANGO ....

        if (data_frame_vendedor.empty == False and data_frame_grupo1_client.empty == False) and (data_frame_grupo6_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client1_linea6_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client1_linea6_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo1"].isin(nomb_cliente_grupo1_query))&(data_frame_vendedor["Linea_Grupo6"].isin(nomb_linea_grupo6_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client1_linea6_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client1_linea6_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})


            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vendedor_client1_linea6_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query, title[2],nomb_linea_grupo6_query,title[3],fecha_inicio_query,title[4], fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client1_linea6_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query, title[2],nomb_linea_grupo6_query,title[3],fecha_inicio_query,title[4], fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client1_linea6_range,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query, title[2],nomb_linea_grupo6_query,title[3],fecha_inicio_query,title[4], fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo1_query, title[2],nomb_linea_grupo6_query,title[3],fecha_inicio_query,title[4], fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR CLIENTE 2 + LINEA  1 + FECHA INICIAL, FECHA FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo2_client.empty == False) and (data_frame_grupo1_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client2_linea1_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client2_linea1_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_vendedor["Linea_Grupo1"].isin(nomb_linea_grupo1_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client2_linea1_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client2_linea1_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client2_linea1_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query, title[2],nomb_linea_grupo1_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client2_linea1_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query, title[2],nomb_linea_grupo1_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client2_linea1_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query, title[2],nomb_linea_grupo1_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query, title[2],nomb_linea_grupo1_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 2 + LINEA 2 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo2_client.empty == False) and (data_frame_grupo2_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client2_linea2_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client2_linea2_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_vendedor["Linea_Grupo2"].isin(nomb_linea_grupo2_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client2_linea2_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client2_linea2_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vendedor_client2_linea2_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo2_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client2_linea2_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo2_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client2_linea2_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo2_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo2_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 2 + LINEA 3 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo2_client.empty == False) and (data_frame_grupo3_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client2_linea3_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client2_linea3_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_vendedor["Linea_Grupo3"].isin(nomb_linea_grupo3_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client2_linea3_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client2_linea3_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vendedor_client2_linea3_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo2_query,title[2], nomb_linea_grupo3_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client2_linea3_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo2_query,title[2], nomb_linea_grupo3_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client2_linea3_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo2_query,title[2], nomb_linea_grupo3_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo2_query,title[2], nomb_linea_grupo3_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 2 + LINEA 4 + FECHA INICIA, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo2_client.empty == False) and (data_frame_grupo4_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client2_linea4_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client2_linea4_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_vendedor["Linea_Grupo4"].isin(nomb_linea_grupo4_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client2_linea4_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client2_linea4_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vendedor_client2_linea4_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client2_linea4_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client2_linea4_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 2 + LINEA 5 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo2_client.empty == False) and (data_frame_grupo5_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client2_linea5_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client2_linea5_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_vendedor["Linea_Grupo5"].isin(nomb_linea_grupo5_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client2_linea5_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client2_linea5_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')

            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vendedor_client2_linea5_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo5_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client2_linea5_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo5_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client2_linea5_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo5_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo5_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 2 + LINEA 6 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo2_client.empty == False) and (data_frame_grupo6_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client2_linea6_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client2_linea6_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo2"].isin(nomb_cliente_grupo2_query))&(data_frame_vendedor["Linea_Grupo6"].isin(nomb_linea_grupo6_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client2_linea6_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client2_linea6_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client2_linea6_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo6_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client2_linea6_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo6_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client2_linea6_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo6_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo2_query,title[2], nomb_linea_grupo6_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 3 + LINEA 1 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo3_client.empty == False) and (data_frame_grupo1_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client3_linea1_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client3_linea1_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_vendedor["Linea_Grupo1"].isin(nomb_linea_grupo1_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client3_linea1_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client3_linea1_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client3_linea1_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo1_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client3_linea1_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo1_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client3_linea1_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo1_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo1_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 3 + LINEA 2 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo3_client.empty == False) and (data_frame_grupo2_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client3_linea2_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client3_linea2_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_vendedor["Linea_Grupo2"].isin(nomb_linea_grupo2_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client3_linea2_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client3_linea2_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client3_linea2_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query,title[2], nomb_linea_grupo2_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client3_linea2_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query,title[2], nomb_linea_grupo2_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client3_linea2_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query,title[2], nomb_linea_grupo2_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query,title[2], nomb_linea_grupo2_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 3 + LINEA 3 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo3_client.empty == False) and (data_frame_grupo3_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client3_linea3_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client3_linea3_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_vendedor["Linea_Grupo3"].isin(nomb_linea_grupo3_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client3_linea3_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client3_linea3_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client3_linea3_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo3_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client3_linea3_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo3_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client3_linea3_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo3_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo3_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 3 + LINEA 4 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo3_client.empty == False) and (data_frame_grupo4_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client3_linea4_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client3_linea4_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_vendedor["Linea_Grupo4"].isin(nomb_linea_grupo4_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client3_linea4_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client3_linea4_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client3_linea4_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client3_linea4_range ,values='Precio Total', names='Item', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client3_linea4_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 3 + LINEA 5 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo3_client.empty == False) and (data_frame_grupo5_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client3_linea5_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client3_linea5_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_vendedor["Linea_Grupo5"].isin(nomb_linea_grupo5_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client3_linea5_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client3_linea5_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client3_linea5_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo3_query, title[2],nomb_linea_grupo5_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client3_linea5_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo3_query, title[2],nomb_linea_grupo5_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client3_linea5_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo3_query, title[2],nomb_linea_grupo5_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo3_query, title[2],nomb_linea_grupo5_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")



        # COMBINACION VENDEDOR + CLIENTE 3 + LINEA 6 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo3_client.empty == False) and (data_frame_grupo6_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client3_linea6_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client3_linea6_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo3"].isin(nomb_cliente_grupo3_query))&(data_frame_vendedor["Linea_Grupo6"].isin(nomb_linea_grupo6_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client3_linea6_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client3_linea6_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vendedor_client3_linea6_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo6_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client3_linea6_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo6_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client3_linea6_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo6_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo3_query, title[2],nomb_linea_grupo6_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")



        # COMBINACION VENDEDOR + CLIENTE 4 + LINEA 1 + FICHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo4_client.empty == False) and (data_frame_grupo1_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client4_linea1_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client4_linea1_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_vendedor["Linea_Grupo1"].isin(nomb_linea_grupo1_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client4_linea1_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client4_linea1_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client4_linea1_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query,title[2], nomb_linea_grupo1_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client4_linea1_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query,title[2], nomb_linea_grupo1_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client4_linea1_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query,title[2], nomb_linea_grupo1_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query,title[2], nomb_linea_grupo1_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 4 + LINEA 2 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo4_client.empty == False) and (data_frame_grupo2_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client4_linea2_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client4_linea2_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_vendedor["Linea_Grupo2"].isin(nomb_linea_grupo2_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client4_linea2_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client4_linea2_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client4_linea2_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query, title[2],nomb_linea_grupo2_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client4_linea2_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query, title[2],nomb_linea_grupo2_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client4_linea2_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query, title[2],nomb_linea_grupo2_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query, title[2],nomb_linea_grupo2_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION VENDEDOR + CLIENTE 4 + LINEA 3 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo4_client.empty == False) and (data_frame_grupo3_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client4_linea3_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client4_linea3_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_vendedor["Linea_Grupo3"].isin(nomb_linea_grupo3_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client4_linea3_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client4_linea3_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client4_linea3_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query,title[2], nomb_linea_grupo3_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client4_linea3_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query,title[2], nomb_linea_grupo3_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client4_linea3_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query,title[2], nomb_linea_grupo3_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([title[0],vendedor_query, title[1],nomb_cliente_grupo4_query,title[2], nomb_linea_grupo3_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 4 + LINEA 4 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo4_client.empty == False) and (data_frame_grupo4_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client4_linea4_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client4_linea4_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_vendedor["Linea_Grupo4"].isin(nomb_linea_grupo4_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client4_linea4_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client4_linea4_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client4_linea4_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client4_linea4_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client4_linea4_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo4_query, title[3],fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")

        # COMBINACION VENDEDOR + CLIENTE 4 + LINEA 5 + FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo4_client.empty == False) and (data_frame_grupo5_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client4_linea5_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client4_linea5_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_vendedor["Linea_Grupo5"].isin(nomb_linea_grupo5_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client4_linea5_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client4_linea5_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']

            fig = px.histogram(df_vendedor_client4_linea5_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo5_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client4_linea5_range ,values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo5_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client4_linea5_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo5_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha", y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo5_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        # COMBINACION VENDEDOR + CLIENTE 4 + LINEA 6 +FECHA INICIAL, FINAL, RANGO ...

        if (data_frame_vendedor.empty == False and data_frame_grupo4_client.empty == False) and (data_frame_grupo6_linea.empty == False and data_frame_date_range.empty == False):
            df_list.append(pd.DataFrame(projects_data))
            df_vendedor_client4_linea6_range= pd.concat(df_list ,ignore_index='True')
            df_vendedor_client4_linea6_range=data_frame_vendedor[(data_frame_vendedor["NombreVendedor"].isin(vendedor_query))&(data_frame_vendedor["Clinete_Grupo4"].isin(nomb_cliente_grupo4_query))&(data_frame_vendedor["Linea_Grupo6"].isin(nomb_linea_grupo6_query))&(data_frame_vendedor["Fecha"].between(fecha_inicio_query,fecha_final_query))]

            df1 = pd.DataFrame(df_vendedor_client4_linea6_range.groupby(by=['Fecha'])['Precio Total'].sum())
            df1 = df1.reset_index()

            df_rename = df_vendedor_client4_linea6_range.rename(columns={'Clinete_Grupo4': 'Cliente4', 'Clinete_Grupo1': 'Cliente1', 'Clinete_Grupo2': 'Client2', 'Clinete_Grupo3': 'Cliente3', 'Linea_Grupo1': 'Linea1', 'Linea_Grupo2': 'Linea2', 'Linea_Grupo3': 'Linea3', 'Linea_Grupo4': 'Linea4', 'Linea_Grupo5': 'Linea5', 'Linea_Grupo6': 'Linea6'})

            df_list_table_line1 = pd.DataFrame(df_rename.groupby(by=['Linea1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line1 = df_list_table_line1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line1 = df_list_table_line1.reset_index()
            df_list_table_line1 = df_list_table_line1.to_dict('records')

            df_list_table_line2 = pd.DataFrame(df_rename.groupby(by=['Linea2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line2 = df_list_table_line2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line2 = df_list_table_line2.reset_index()
            df_list_table_line2 = df_list_table_line2.to_dict('records')

            df_list_table_line3 = pd.DataFrame(df_rename.groupby(by=['Linea3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line3 = df_list_table_line3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line3 = df_list_table_line3.reset_index()
            df_list_table_line3 = df_list_table_line3.to_dict('records')

            df_list_table_line4 = pd.DataFrame(df_rename.groupby(by=['Linea4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line4 = df_list_table_line4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line4 = df_list_table_line4.reset_index()
            df_list_table_line4 = df_list_table_line4.to_dict('records')

            df_list_table_line5 = pd.DataFrame(df_rename.groupby(by=['Linea5'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line5 = df_list_table_line5.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line5 = df_list_table_line5.reset_index()
            df_list_table_line5 = df_list_table_line5.to_dict('records')

            df_list_table_line6 = pd.DataFrame(df_rename.groupby(by=['Linea6'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_line6 = df_list_table_line6.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_line6 = df_list_table_line6.reset_index()
            df_list_table_line6 = df_list_table_line6.to_dict('records')


            df_list_table_client1 = pd.DataFrame(df_rename.groupby(by=['Cliente1'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client1 = df_list_table_client1.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client1 = df_list_table_client1.reset_index()
            df_list_table_client1 = df_list_table_client1.to_dict('records')

            df_list_table_client2 = pd.DataFrame(df_rename.groupby(by=['Client2'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client2 = df_list_table_client2.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client2 = df_list_table_client2.reset_index()
            df_list_table_client2 = df_list_table_client2.to_dict('records')

            df_list_table_client3 = pd.DataFrame(df_rename.groupby(by=['Cliente3'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client3 = df_list_table_client3.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client3 = df_list_table_client3.reset_index()
            df_list_table_client3 = df_list_table_client3.to_dict('records')

            df_list_table_client4 = pd.DataFrame(df_rename.groupby(by=['Cliente4'])['Utilidad', 'Costo Total Real', 'Precio Total'].sum())
            df_list_table_client4 = df_list_table_client4.rename(columns={ 'Costo Total Real': 'Costo', 'Precio Total': 'Precio'})
            df_list_table_client4 = df_list_table_client4.reset_index()
            df_list_table_client4 = df_list_table_client4.to_dict('records')
            title = ['Vendedor:','Clientes:','Lineas:', 'Fecha de inicio:', 'Fecha de Fin:']
            fig = px.histogram(df_vendedor_client4_linea6_range , x='NombreVendedor', y=[
                            'Precio Total', 'Costo Total Real','Utilidad'], barmode='group', title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo6_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]),text_auto=True)
            fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["type", "histogram"],
                                    label="Histograma",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "scatter"],
                                    label="Lineas",
                                    method="restyle"
                                ),
                                dict(
                                    args=["type", "box"],
                                    label="Cajas",
                                    method="restyle"
                                )
                            ]),
                            direction="down"
                        )
                    ]
                )
            donut_fig = px.pie(df_vendedor_client4_linea6_range , values='Precio Total', names='Proveedor', hole=.3, title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo6_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_proov = px.histogram(df_vendedor_client4_linea6_range ,x='Linea_Grupo1', y=['Precio Total', 'Costo Total Real', 'Utilidad'],barmode='group',text_auto=True,hover_name="Linea_Grupo1", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo6_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))
            fig_date = px.line(df1 , x="Fecha",y="Precio Total", title=str([title[0],vendedor_query,title[1], nomb_cliente_grupo4_query,title[2], nomb_linea_grupo6_query,title[3], fecha_inicio_query ,title[4],fecha_final_query]))

            donut_fig.update_traces(textposition='inside')
            donut_fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            
            fig_date.update_layout(hovermode="x unified")

            gantt_donut = plot(donut_fig, output_type="div")
            gantt_plot = plot(fig, output_type="div")
            gantt_proov = plot(fig_proov, output_type="div")
            gantt_time_line = plot(fig_date, output_type="div")


        context = {
            'queryset': report,
            'plot_div': gantt_plot,
            'donut': gantt_donut,
            'provee': gantt_proov,
            'time_line': gantt_time_line,
            'contadorVendedor': modelFcvendedor,
            'contadorLinea1': modelIvgrupo1,
            'contadorLinea2': modelIvgrupo2,
            'contadorLinea3': modelIvgrupo3,
            'contadorLinea4': modelIvgrupo4,
            'contadorLinea5': modelIvgrupo5,
            'contadorLinea6': modelIvgrupo6,
            'contadorCliente1': modelPcgrupo1,
            'contadorCliente2': modelPcgrupo2,
            'contadorCliente3': modelPcgrupo3,
            'contadorCliente4': modelPcgrupo4,

            'date_actually': {"date" : date_actually},
            'date_first_day': {"date" : date_first_day},

            'modelGnopcionG1': modelGnopcionG1[0],
            'modelGnopcionG2': modelGnopcionG2[0],
            'modelGnopcionG3': modelGnopcionG3[0],
            'modelGnopcionG4': modelGnopcionG4[0],
            'modelGnopcionG5': modelGnopcionG5[0],
            'modelGnopcionG6': modelGnopcionG6[0],

            'modelGnopcionPc1': modelGnopcionPc1[0],
            'modelGnopcionPc2': modelGnopcionPc2[0],
            'modelGnopcionPc3': modelGnopcionPc3[0],
            'modelGnopcionPc4': modelGnopcionPc4[0],

            'modelempresa': modelempresa[0],

            'df_list_table_client1': df_list_table_client1,
            'df_list_table_client2': df_list_table_client2,
            'df_list_table_client3': df_list_table_client3,
            'df_list_table_client4': df_list_table_client4,

            'df_list_table_line1': df_list_table_line1,
            'df_list_table_line2': df_list_table_line2,
            'df_list_table_line3': df_list_table_line3,
            'df_list_table_line4': df_list_table_line4,
            'df_list_table_line5': df_list_table_line5,
            'df_list_table_line6': df_list_table_line6,
        }

        return render(request, 'dashboard.html', context)
    except:
        return render(request, 'notFound.html')

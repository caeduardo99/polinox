from django.db import models

# Create your models here.
class Fcvendedor(models.Model):
    idvendedor = models.AutoField(db_column='IdVendedor', primary_key=True)  # Field name made lowercase.
    codvendedor = models.CharField(db_column='CodVendedor', unique=True, max_length=10)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=40)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    tipotabla = models.IntegerField(db_column='TipoTabla', blank=True, null=True)  # Field name made lowercase.
    bandvendedor = models.BooleanField(db_column='BandVendedor')  # Field name made lowercase.
    bandcobrador = models.BooleanField(db_column='BandCobrador')  # Field name made lowercase.
    idcuentafaltante = models.IntegerField(db_column='IdCuentaFaltante', blank=True, null=True)  # Field name made lowercase.
    idcuentasobrante = models.IntegerField(db_column='IdCuentaSobrante', blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=40, blank=True, null=True)
    codusuario = models.CharField(db_column='CodUsuario', max_length=10, blank=True, null=True)  # Field name made lowercase.
    idcotizador = models.IntegerField(db_column='idCotizador', blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    lineastablet = models.CharField(db_column='LineasTablet', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    vendedorestablet = models.CharField(db_column='VendedoresTablet', max_length=256, blank=True, null=True)  # Field name made lowercase.
    ordenbodegas = models.CharField(db_column='OrdenBodegas', max_length=256, blank=True, null=True)  # Field name made lowercase.
    bandtodoivg = models.BooleanField(db_column='BandTodoIVG')  # Field name made lowercase.
    bandtodovende = models.BooleanField(db_column='BandTodoVende')  # Field name made lowercase.
    rutastablet = models.CharField(db_column='RutasTablet', max_length=256, blank=True, null=True)  # Field name made lowercase.
    idtablacomision = models.IntegerField(db_column='IDTablaComision', blank=True, null=True)  # Field name made lowercase.
    bandtodoivg2 = models.BooleanField(db_column='BandTodoIVG2')  # Field name made lowercase.
    ivg2tablet = models.CharField(db_column='IVG2Tablet', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    bandacumulapuntos = models.BooleanField(db_column='BandAcumulaPuntos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FCVendedor'


class Gncomprobante(models.Model):
    transid = models.AutoField(db_column='TransID', primary_key=True)  # Field name made lowercase.
    codtrans = models.CharField(db_column='CodTrans', max_length=5)  # Field name made lowercase.
    numtrans = models.IntegerField(db_column='NumTrans')  # Field name made lowercase.
    codasiento = models.IntegerField(db_column='CodAsiento', blank=True, null=True)  # Field name made lowercase.
    fechatrans = models.DateTimeField(db_column='FechaTrans')  # Field name made lowercase.
    horatrans = models.DateTimeField(db_column='HoraTrans')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=120, blank=True, null=True)  # Field name made lowercase.
    codusuario = models.CharField(db_column='CodUsuario', max_length=10)  # Field name made lowercase.
    idresponsable = models.IntegerField(db_column='IdResponsable', blank=True, null=True)  # Field name made lowercase.
    numdocref = models.CharField(db_column='NumDocRef', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='Estado')  # Field name made lowercase.
    posid = models.CharField(db_column='PosID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    numtranscierrepos = models.IntegerField(db_column='NumTransCierrePOS', blank=True, null=True)  # Field name made lowercase.
    idcentro = models.IntegerField(db_column='IdCentro', blank=True, null=True)  # Field name made lowercase.
    idtransfuente = models.IntegerField(db_column='IdTransFuente', blank=True, null=True)  # Field name made lowercase.
    codmoneda = models.CharField(db_column='CodMoneda', max_length=5)  # Field name made lowercase.
    cotizacion2 = models.DecimalField(db_column='Cotizacion2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cotizacion3 = models.DecimalField(db_column='Cotizacion3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cotizacion4 = models.DecimalField(db_column='Cotizacion4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idproveedorref = models.IntegerField(db_column='IdProveedorRef', blank=True, null=True)  # Field name made lowercase.
    idclienteref = models.IntegerField(db_column='IdClienteRef', blank=True, null=True)  # Field name made lowercase.
    idvendedor = models.IntegerField(db_column='IdVendedor', blank=True, null=True)  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=40, blank=True, null=True)  # Field name made lowercase.
    codusuariomodifica = models.CharField(db_column='CodUsuarioModifica', max_length=10)  # Field name made lowercase.
    impresion = models.SmallIntegerField(db_column='Impresion')  # Field name made lowercase.
    idmotivo = models.IntegerField(db_column='IdMotivo', blank=True, null=True)  # Field name made lowercase.
    comision = models.DecimalField(db_column='Comision', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fechadevol = models.DateTimeField(db_column='FechaDevol', blank=True, null=True)  # Field name made lowercase.
    numdias = models.IntegerField(db_column='numDias')  # Field name made lowercase.
    bandcierre = models.SmallIntegerField(db_column='bandCierre')  # Field name made lowercase.
    comisioncobrador = models.DecimalField(db_column='ComisionCobrador', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    autorizacionsri = models.CharField(db_column='AutorizacionSRI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fechacaducidadsri = models.DateTimeField(db_column='FechaCaducidadSRI', blank=True, null=True)  # Field name made lowercase.
    estado1 = models.SmallIntegerField(db_column='Estado1')  # Field name made lowercase.
    estado2 = models.SmallIntegerField(db_column='Estado2')  # Field name made lowercase.
    codusuarioautoriza = models.CharField(db_column='CodUsuarioAutoriza', max_length=10)  # Field name made lowercase.
    idgaranteref = models.IntegerField(db_column='IdGaranteRef')  # Field name made lowercase.
    idobra = models.IntegerField(db_column='IdObra')  # Field name made lowercase.
    idzona = models.IntegerField(db_column='IdZona')  # Field name made lowercase.
    iddescuento = models.IntegerField(db_column='IdDescuento')  # Field name made lowercase.
    idforma = models.IntegerField(db_column='IdForma')  # Field name made lowercase.
    numserieestasri = models.CharField(db_column='NumSerieEstaSRI', max_length=3)  # Field name made lowercase.
    numseriepuntosri = models.CharField(db_column='NumSeriePuntoSRI', max_length=3)  # Field name made lowercase.
    fechaautorizacionsri = models.DateTimeField(db_column='FechaAutorizacionSRI', blank=True, null=True)  # Field name made lowercase.
    codprasiento = models.IntegerField(db_column='CodPRAsiento')  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIVA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idtiporol = models.IntegerField(db_column='idTipoRol')  # Field name made lowercase.
    pcpordesc = models.DecimalField(db_column='PCPorDesc', max_digits=19, decimal_places=4)  # Field name made lowercase.
    bandfinalizado = models.BooleanField(db_column='BandFinalizado', blank=True, null=True)  # Field name made lowercase.
    idcentrohijo = models.IntegerField(db_column='idCentroHijo')  # Field name made lowercase.
    estadofacelect = models.SmallIntegerField(db_column='EstadoFacElect')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GNComprobante'
        unique_together = (('codtrans', 'numtrans'),)


class Gnopcion(models.Model):
    nombreempresa = models.CharField(db_column='NombreEmpresa', max_length=80, primary_key=True)  # Field name made lowercase.
    direccion1 = models.CharField(db_column='Direccion1', max_length=80, blank=True, null=True)  # Field name made lowercase.
    direccion2 = models.CharField(db_column='Direccion2', max_length=80, blank=True, null=True)  # Field name made lowercase.
    telefono1 = models.CharField(db_column='Telefono1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telefono2 = models.CharField(db_column='Telefono2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telefono3 = models.CharField(db_column='Telefono3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax2 = models.CharField(db_column='Fax2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ruc = models.CharField(db_column='RUC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logotipo = models.BinaryField(db_column='LogoTipo', blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafinal = models.DateTimeField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    codasientosi = models.IntegerField(db_column='CodAsientoSI', blank=True, null=True)  # Field name made lowercase.
    codasientofinal = models.IntegerField(db_column='CodAsientoFinal', blank=True, null=True)  # Field name made lowercase.
    idcuentaresultado = models.IntegerField(db_column='IdCuentaResultado', blank=True, null=True)  # Field name made lowercase.
    etiquetagrupo1 = models.CharField(db_column='EtiquetaGrupo1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetagrupo2 = models.CharField(db_column='EtiquetaGrupo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetagrupo3 = models.CharField(db_column='EtiquetaGrupo3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetagrupo4 = models.CharField(db_column='EtiquetaGrupo4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetagrupo5 = models.CharField(db_column='EtiquetaGrupo5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupo1 = models.CharField(db_column='EtiquetaPCGrupo1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupo2 = models.CharField(db_column='EtiquetaPCGrupo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupo3 = models.CharField(db_column='EtiquetaPCGrupo3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    fechalimitedesde = models.DateTimeField(db_column='FechaLimiteDesde', blank=True, null=True)  # Field name made lowercase.
    fechalimitehasta = models.DateTimeField(db_column='FechaLimiteHasta', blank=True, null=True)  # Field name made lowercase.
    codmoneda1 = models.CharField(db_column='CodMoneda1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    codmoneda2 = models.CharField(db_column='CodMoneda2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    codmoneda3 = models.CharField(db_column='CodMoneda3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    codmoneda4 = models.CharField(db_column='CodMoneda4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nombremoneda1 = models.CharField(db_column='NombreMoneda1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombremoneda2 = models.CharField(db_column='NombreMoneda2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombremoneda3 = models.CharField(db_column='NombreMoneda3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombremoneda4 = models.CharField(db_column='NombreMoneda4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formatomoneda1 = models.CharField(db_column='FormatoMoneda1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formatomoneda2 = models.CharField(db_column='FormatoMoneda2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formatomoneda3 = models.CharField(db_column='FormatoMoneda3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formatomoneda4 = models.CharField(db_column='FormatoMoneda4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formatocantidad = models.CharField(db_column='FormatoCantidad', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formatofecha = models.CharField(db_column='FormatoFecha', max_length=20, blank=True, null=True)  # Field name made lowercase.
    costeo = models.SmallIntegerField(db_column='Costeo', blank=True, null=True)  # Field name made lowercase.
    generacoditem = models.SmallIntegerField(db_column='GeneraCodItem', blank=True, null=True)  # Field name made lowercase.
    generacodprov = models.SmallIntegerField(db_column='GeneraCodProv', blank=True, null=True)  # Field name made lowercase.
    generacodcli = models.SmallIntegerField(db_column='GeneraCodCli', blank=True, null=True)  # Field name made lowercase.
    generacodcc = models.SmallIntegerField(db_column='GeneraCodCC', blank=True, null=True)  # Field name made lowercase.
    prefijocoditem = models.CharField(db_column='PrefijoCodItem', max_length=3, blank=True, null=True)  # Field name made lowercase.
    prefijocodprov = models.CharField(db_column='PrefijoCodProv', max_length=3, blank=True, null=True)  # Field name made lowercase.
    prefijocodcli = models.CharField(db_column='PrefijoCodCli', max_length=3, blank=True, null=True)  # Field name made lowercase.
    prefijocodcc = models.CharField(db_column='PrefijoCodCC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    idcuentaprovpre = models.IntegerField(db_column='IdCuentaProvPre', blank=True, null=True)  # Field name made lowercase.
    idcuentaclipre = models.IntegerField(db_column='IdCuentaCliPre', blank=True, null=True)  # Field name made lowercase.
    permiteitemsincuenta = models.BooleanField(db_column='PermiteItemSinCuenta')  # Field name made lowercase.
    ocultacontable = models.BooleanField(db_column='OcultaContable')  # Field name made lowercase.
    los100doccobropago = models.BooleanField(db_column='Los100DocCobroPago')  # Field name made lowercase.
    etiquetapcgrupo4 = models.CharField(db_column='EtiquetaPCGrupo4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tipoempresa = models.CharField(db_column='TipoEmpresa', max_length=20, blank=True, null=True)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    formatocoditem = models.CharField(db_column='FormatoCodItem', max_length=10, blank=True, null=True)  # Field name made lowercase.
    formatocodprov = models.CharField(db_column='FormatoCodProv', max_length=10, blank=True, null=True)  # Field name made lowercase.
    formatocodcli = models.CharField(db_column='FormatoCodCli', max_length=10, blank=True, null=True)  # Field name made lowercase.
    formatocodcc = models.CharField(db_column='FormatoCodCC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    formatocodaf = models.CharField(db_column='FormatoCodAF', max_length=10, blank=True, null=True)  # Field name made lowercase.
    etiquetaestado1 = models.CharField(db_column='EtiquetaEstado1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetaestado2 = models.CharField(db_column='EtiquetaEstado2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numautorizacion_autoimp = models.CharField(db_column='NumAutorizacion_AutoImp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fechacaducidad_autoimp = models.DateTimeField(db_column='FechaCaducidad_AutoImp', blank=True, null=True)  # Field name made lowercase.
    numautorizacion_autoimpold = models.CharField(db_column='NumAutorizacion_AutoImpOld', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fechacaducidad_autoimpold = models.DateTimeField(db_column='FechaCaducidad_AutoImpOld', blank=True, null=True)  # Field name made lowercase.
    etiquetaafgrupo1 = models.CharField(db_column='EtiquetaAFGrupo1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetaafgrupo2 = models.CharField(db_column='EtiquetaAFGrupo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetaafgrupo3 = models.CharField(db_column='EtiquetaAFGrupo3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetaafgrupo4 = models.CharField(db_column='EtiquetaAFGrupo4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetaafgrupo5 = models.CharField(db_column='EtiquetaAFGrupo5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    generacodafitem = models.CharField(db_column='GeneraCodAFItem', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prefijocodafitem = models.CharField(db_column='PrefijoCodAFItem', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formatocodafitem = models.CharField(db_column='FormatoCodAFItem', max_length=20, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=80, blank=True, null=True)  # Field name made lowercase.
    etiquetagncgrupo1 = models.CharField(db_column='EtiquetaGNCGrupo1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetagncgrupo2 = models.CharField(db_column='EtiquetaGNCGrupo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetagncgrupo3 = models.CharField(db_column='EtiquetaGNCGrupo3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetagncgrupo4 = models.CharField(db_column='EtiquetaGNCGrupo4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idcuentaactivopre = models.IntegerField(db_column='IdCuentaActivoPre', blank=True, null=True)  # Field name made lowercase.
    idcuentacostopre = models.IntegerField(db_column='IdCuentaCostoPre', blank=True, null=True)  # Field name made lowercase.
    idcuentaventapre = models.IntegerField(db_column='IdCuentaVentaPre', blank=True, null=True)  # Field name made lowercase.
    etiquetagnvgrupo1 = models.CharField(db_column='EtiquetaGNVGrupo1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetagnvgrupo2 = models.CharField(db_column='EtiquetaGNVGrupo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetagnvgrupo3 = models.CharField(db_column='EtiquetaGNVGrupo3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetagnvgrupo4 = models.CharField(db_column='EtiquetaGNVGrupo4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idcuentasobrantecajapre = models.IntegerField(db_column='IdCuentaSobranteCajaPre')  # Field name made lowercase.
    fechaautorizacion_autoimp = models.DateTimeField(db_column='FechaAutorizacion_AutoImp', blank=True, null=True)  # Field name made lowercase.
    fechaautorizacion_autoimpold = models.DateTimeField(db_column='FechaAutorizacion_AutoImpOld', blank=True, null=True)  # Field name made lowercase.
    montomaximocf = models.DecimalField(db_column='MontoMaximoCF', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rutaxmlvalido = models.CharField(db_column='RutaXMLValido', max_length=150, blank=True, null=True)  # Field name made lowercase.
    rutaxmlanulado = models.CharField(db_column='RutaXMLAnulado', max_length=150, blank=True, null=True)  # Field name made lowercase.
    resolucion = models.CharField(db_column='Resolucion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tipoempresasri = models.CharField(db_column='TipoEmpresaSRI', max_length=4, blank=True, null=True)  # Field name made lowercase.
    autoimpresor = models.BooleanField(db_column='AutoImpresor')  # Field name made lowercase.
    idprovinciapre = models.IntegerField(db_column='IdProvinciaPre')  # Field name made lowercase.
    idcantonpre = models.IntegerField(db_column='IdCantonPre')  # Field name made lowercase.
    utilidadmarkdown = models.BooleanField(db_column='UtilidadMarkDown')  # Field name made lowercase.
    etiquetapcgrupop1 = models.CharField(db_column='EtiquetaPCGrupoP1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupop2 = models.CharField(db_column='EtiquetaPCGrupoP2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupop3 = models.CharField(db_column='EtiquetaPCGrupoP3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupop4 = models.CharField(db_column='EtiquetaPCGrupoP4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupoc1 = models.CharField(db_column='EtiquetaPCGrupoC1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupoc2 = models.CharField(db_column='EtiquetaPCGrupoC2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupoc3 = models.CharField(db_column='EtiquetaPCGrupoC3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupoc4 = models.CharField(db_column='EtiquetaPCGrupoC4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupog1 = models.CharField(db_column='EtiquetaPCGrupoG1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupog2 = models.CharField(db_column='EtiquetaPCGrupoG2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupog3 = models.CharField(db_column='EtiquetaPCGrupoG3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupog4 = models.CharField(db_column='EtiquetaPCGrupoG4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupoe1 = models.CharField(db_column='EtiquetaPCGrupoE1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupoe2 = models.CharField(db_column='EtiquetaPCGrupoE2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupoe3 = models.CharField(db_column='EtiquetaPCGrupoE3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupoe4 = models.CharField(db_column='EtiquetaPCGrupoE4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formatocodemp = models.CharField(db_column='FormatoCodEmp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    generacodemp = models.IntegerField(db_column='GeneraCodEmp', blank=True, null=True)  # Field name made lowercase.
    prefijocodemp = models.CharField(db_column='PrefijoCodEmp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    generacodafitemalt = models.CharField(db_column='GeneraCodAFItemALT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prefijocodafitemalt = models.CharField(db_column='PrefijoCodAFItemALT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formatocodafitemalt = models.CharField(db_column='FormatoCodAFItemALT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupol1 = models.CharField(db_column='EtiquetaPCGrupoL1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupol2 = models.CharField(db_column='EtiquetaPCGrupoL2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupol3 = models.CharField(db_column='EtiquetaPCGrupoL3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etiquetapcgrupol4 = models.CharField(db_column='EtiquetaPCGrupoL4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    versionsql = models.CharField(db_column='VersionSQL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    xx = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    codigosc = models.CharField(db_column='CodigoSC', max_length=7, blank=True, null=True)  # Field name made lowercase.
    banddinardap = models.BooleanField(db_column='BandDINARDAP')  # Field name made lowercase.
    bandchp = models.BooleanField(db_column='BandCHP')  # Field name made lowercase.
    ordenbodegas = models.CharField(db_column='OrdenBodegas', max_length=250, blank=True, null=True)  # Field name made lowercase.
    bandordenitemscodigo = models.BooleanField(db_column='BandOrdenItemsCodigo')  # Field name made lowercase.
    bandordengrupoitemscodigo = models.BooleanField(db_column='BandOrdenGrupoItemsCodigo')  # Field name made lowercase.
    bandordenpccodigo = models.BooleanField(db_column='BandOrdenPCCodigo')  # Field name made lowercase.
    bandordenpcgrupocodigo = models.BooleanField(db_column='BandOrdenPCGrupoCodigo')  # Field name made lowercase.
    bandfactelect = models.BooleanField(db_column='BandFactElect')  # Field name made lowercase.
    comprobantesgenerados = models.CharField(db_column='ComprobantesGenerados', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comprobantesfirmados = models.CharField(db_column='ComprobantesFirmados', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comprobantesautorizados = models.CharField(db_column='ComprobantesAutorizados', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comprobantesnoautorizados = models.CharField(db_column='ComprobantesNoAutorizados', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ubicacionarchivotoken = models.CharField(db_column='UbicacionArchivoToken', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contrasenatoken = models.CharField(db_column='ContrasenaToken', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipoambiente = models.CharField(db_column='TipoAmbiente', max_length=2, blank=True, null=True)  # Field name made lowercase.
    comprobantescontingencia = models.CharField(db_column='ComprobantesContingencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    servidorcorreo = models.CharField(db_column='ServidorCorreo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cuentacorreo = models.CharField(db_column='CuentaCorreo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    passwordcorreo = models.CharField(db_column='PasswordCorreo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mensajecorreo = models.CharField(db_column='MensajeCorreo', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    comprobantesenviados = models.CharField(db_column='ComprobantesEnviados', max_length=255, blank=True, null=True)  # Field name made lowercase.
    puertocorreo = models.CharField(db_column='PuertoCorreo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    copiacorreo = models.CharField(db_column='CopiaCorreo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    conexionsegura = models.BooleanField(db_column='ConexionSegura', blank=True, null=True)  # Field name made lowercase.
    asunto = models.CharField(db_column='Asunto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='NombreUsuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bandportal = models.BooleanField(db_column='BandPortal', blank=True, null=True)  # Field name made lowercase.
    bandcorreoautomatico = models.BooleanField(db_column='BandCorreoAutomatico', blank=True, null=True)  # Field name made lowercase.
    comprobantessubidos = models.CharField(db_column='ComprobantesSubidos', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bandcorreoxequipo = models.BooleanField(db_column='BandCorreoxEquipo', blank=True, null=True)  # Field name made lowercase.
    penalizadesctoxitem = models.CharField(db_column='PenalizaDesctoxItem', max_length=100, blank=True, null=True)  # Field name made lowercase.
    etiquetagrupo6 = models.CharField(db_column='EtiquetaGrupo6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bandrebateivg = models.BooleanField(db_column='BandRebateIVG')  # Field name made lowercase.
    numivgrebate = models.IntegerField(db_column='NumIVGRebate')  # Field name made lowercase.
    porcentajeivaant = models.DecimalField(db_column='PorcentajeIVAAnt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fechaiva = models.DateField(db_column='FechaIVA', blank=True, null=True)  # Field name made lowercase.
    bandomitircambioiva = models.BooleanField(db_column='BandOmitirCambioIVA')  # Field name made lowercase.
    bandcostoucparacosto = models.BooleanField(db_column='BandCostoUCParaCosto')  # Field name made lowercase.
    ivktipodatodouble = models.BooleanField(db_column='IVKTipoDatoDouble')  # Field name made lowercase.
    bandconfiglira = models.BooleanField(db_column='BandConfigLira')  # Field name made lowercase.
    bandpordescgeneral = models.BooleanField(db_column='BandPorDescGeneral')  # Field name made lowercase.
    pordescgeneral = models.DecimalField(db_column='PorDescGeneral', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    banddbleclicknomod = models.BooleanField(db_column='BandDbleClickNOMod')  # Field name made lowercase.
    rutarepcarteragen = models.CharField(db_column='RutaRepCarteraGen', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mensajecorreocartera = models.CharField(db_column='MensajeCorreoCartera', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    mensajepdfcartera = models.CharField(db_column='MensajePDFCartera', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    wssripruebasrecepcion = models.CharField(db_column='WsSriPruebasRecepcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wssripruebasautorizacion = models.CharField(db_column='WsSriPruebasAutorizacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wssriproduccionrecepcion = models.CharField(db_column='WsSriProduccionRecepcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wssriproduccionautorizacion = models.CharField(db_column='WsSriProduccionAutorizacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comprobantesporautorizar = models.CharField(db_column='ComprobantesPorAutorizar', max_length=250, blank=True, null=True)  # Field name made lowercase.
    bandoffline = models.BooleanField(db_column='bandOffLine')  # Field name made lowercase.
    idcuentaprovpreant = models.IntegerField(db_column='IdCuentaProvPreAnt')  # Field name made lowercase.
    idcuentaclipreant = models.IntegerField(db_column='IdCuentaCliPreAnt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GNOpcion'


class Ivbodega(models.Model):
    idbodega = models.AutoField(db_column='IdBodega', primary_key=True)  # Field name made lowercase.
    codbodega = models.CharField(db_column='CodBodega', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=160, blank=True, null=True)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    idsucursal = models.IntegerField(db_column='IdSucursal')  # Field name made lowercase.
    idbodegahijo = models.IntegerField(db_column='IdBodegaHijo')  # Field name made lowercase.
    bandbodegahijo = models.BooleanField(db_column='BandBodegaHijo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVBodega'


class Ivgrupo1(models.Model):
    idgrupo1 = models.AutoField(db_column='IdGrupo1', primary_key=True)  # Field name made lowercase.
    codgrupo1 = models.CharField(db_column='CodGrupo1', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    bandproduccion = models.IntegerField(db_column='BandProduccion')  # Field name made lowercase.
    iditemprod = models.IntegerField(db_column='IdItemProd')  # Field name made lowercase.
    rebate = models.DecimalField(db_column='Rebate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idealdias = models.DecimalField(db_column='Idealdias', max_digits=19, decimal_places=4)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20, blank=True, null=True)  # Field name made lowercase.
    porcomision = models.DecimalField(db_column='porComision', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibrapersonal = models.DecimalField(db_column='precioxlibraPersonal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibracomercial = models.DecimalField(db_column='precioxlibraComercial', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibraotro = models.DecimalField(db_column='precioxlibraOtro', max_digits=19, decimal_places=4)  # Field name made lowercase.
    numgrupo = models.IntegerField(db_column='numGrupo')  # Field name made lowercase.
    idgrupoagrupa = models.IntegerField(db_column='idGrupoAgrupa')  # Field name made lowercase.
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IVGrupo1'


class Ivgrupo2(models.Model):
    idgrupo2 = models.AutoField(db_column='IdGrupo2', primary_key=True)  # Field name made lowercase.
    codgrupo2 = models.CharField(db_column='CodGrupo2', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', unique=True, max_length=50)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    bandproduccion = models.IntegerField(db_column='BandProduccion')  # Field name made lowercase.
    iditemprod = models.IntegerField(db_column='IdItemProd')  # Field name made lowercase.
    rebate = models.DecimalField(db_column='Rebate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idealdias = models.DecimalField(db_column='Idealdias', max_digits=19, decimal_places=4)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20, blank=True, null=True)  # Field name made lowercase.
    porcomision = models.DecimalField(db_column='porComision', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibrapersonal = models.DecimalField(db_column='precioxlibraPersonal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibracomercial = models.DecimalField(db_column='precioxlibraComercial', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibraotro = models.DecimalField(db_column='precioxlibraOtro', max_digits=19, decimal_places=4)  # Field name made lowercase.
    numgrupo = models.IntegerField(db_column='numGrupo')  # Field name made lowercase.
    idgrupoagrupa = models.IntegerField(db_column='idGrupoAgrupa')  # Field name made lowercase.
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IVGrupo2'


class Ivgrupo3(models.Model):
    idgrupo3 = models.AutoField(db_column='IdGrupo3', primary_key=True)  # Field name made lowercase.
    codgrupo3 = models.CharField(db_column='CodGrupo3', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', unique=True, max_length=50)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    bandproduccion = models.IntegerField(db_column='BandProduccion')  # Field name made lowercase.
    iditemprod = models.IntegerField(db_column='IdItemProd')  # Field name made lowercase.
    rebate = models.DecimalField(db_column='Rebate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idealdias = models.DecimalField(db_column='Idealdias', max_digits=19, decimal_places=4)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20, blank=True, null=True)  # Field name made lowercase.
    porcomision = models.DecimalField(db_column='porComision', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibrapersonal = models.DecimalField(db_column='precioxlibraPersonal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibracomercial = models.DecimalField(db_column='precioxlibraComercial', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibraotro = models.DecimalField(db_column='precioxlibraOtro', max_digits=19, decimal_places=4)  # Field name made lowercase.
    numgrupo = models.IntegerField(db_column='numGrupo')  # Field name made lowercase.
    idgrupoagrupa = models.IntegerField(db_column='idGrupoAgrupa')  # Field name made lowercase.
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IVGrupo3'


class Ivgrupo4(models.Model):
    idgrupo4 = models.AutoField(db_column='IdGrupo4', primary_key=True)  # Field name made lowercase.
    codgrupo4 = models.CharField(db_column='CodGrupo4', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', unique=True, max_length=50)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    bandproduccion = models.IntegerField(db_column='BandProduccion')  # Field name made lowercase.
    iditemprod = models.IntegerField(db_column='IdItemProd')  # Field name made lowercase.
    rebate = models.DecimalField(db_column='Rebate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idealdias = models.DecimalField(db_column='Idealdias', max_digits=19, decimal_places=4)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20, blank=True, null=True)  # Field name made lowercase.
    porcomision = models.DecimalField(db_column='porComision', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibrapersonal = models.DecimalField(db_column='precioxlibraPersonal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibracomercial = models.DecimalField(db_column='precioxlibraComercial', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibraotro = models.DecimalField(db_column='precioxlibraOtro', max_digits=19, decimal_places=4)  # Field name made lowercase.
    numgrupo = models.IntegerField(db_column='numGrupo')  # Field name made lowercase.
    idgrupoagrupa = models.IntegerField(db_column='idGrupoAgrupa')  # Field name made lowercase.
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IVGrupo4'


class Ivgrupo5(models.Model):
    idgrupo5 = models.AutoField(db_column='IdGrupo5', primary_key=True)  # Field name made lowercase.
    codgrupo5 = models.CharField(db_column='CodGrupo5', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    bandproduccion = models.IntegerField(db_column='BandProduccion')  # Field name made lowercase.
    iditemprod = models.IntegerField(db_column='IdItemProd')  # Field name made lowercase.
    rebate = models.DecimalField(db_column='Rebate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idealdias = models.DecimalField(db_column='Idealdias', max_digits=19, decimal_places=4)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20, blank=True, null=True)  # Field name made lowercase.
    porcomision = models.DecimalField(db_column='porComision', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibrapersonal = models.DecimalField(db_column='precioxlibraPersonal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibracomercial = models.DecimalField(db_column='precioxlibraComercial', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibraotro = models.DecimalField(db_column='precioxlibraOtro', max_digits=19, decimal_places=4)  # Field name made lowercase.
    numgrupo = models.IntegerField(db_column='numGrupo')  # Field name made lowercase.
    idgrupoagrupa = models.IntegerField(db_column='idGrupoAgrupa')  # Field name made lowercase.
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IVGrupo5'


class Ivgrupo6(models.Model):
    idgrupo6 = models.AutoField(db_column='IdGrupo6', primary_key=True)  # Field name made lowercase.
    codgrupo6 = models.CharField(db_column='CodGrupo6', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=60)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    bandproduccion = models.IntegerField(db_column='BandProduccion')  # Field name made lowercase.
    iditemprod = models.IntegerField(db_column='IdItemProd')  # Field name made lowercase.
    rebate = models.DecimalField(db_column='Rebate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idealdias = models.DecimalField(db_column='Idealdias', max_digits=19, decimal_places=4)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20, blank=True, null=True)  # Field name made lowercase.
    porcomision = models.DecimalField(db_column='porComision', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibrapersonal = models.DecimalField(db_column='precioxlibraPersonal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibracomercial = models.DecimalField(db_column='precioxlibraComercial', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioxlibraotro = models.DecimalField(db_column='precioxlibraOtro', max_digits=19, decimal_places=4)  # Field name made lowercase.
    numgrupo = models.IntegerField(db_column='numGrupo')  # Field name made lowercase.
    idgrupoagrupa = models.IntegerField(db_column='idGrupoAgrupa')  # Field name made lowercase.
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IVGrupo6'


class Ivinventario(models.Model):
    idinventario = models.AutoField(db_column='IdInventario', primary_key=True)  # Field name made lowercase.
    codinventario = models.CharField(db_column='CodInventario', unique=True, max_length=20)  # Field name made lowercase.
    codalterno1 = models.CharField(db_column='CodAlterno1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codalterno2 = models.CharField(db_column='CodAlterno2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    descripciondetalle = models.TextField(db_column='DescripcionDetalle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    precio1 = models.DecimalField(db_column='Precio1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precio2 = models.DecimalField(db_column='Precio2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precio3 = models.DecimalField(db_column='Precio3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precio4 = models.DecimalField(db_column='Precio4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    codmoneda = models.CharField(db_column='CodMoneda', max_length=5)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIVA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    comision1 = models.DecimalField(db_column='Comision1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    comision2 = models.DecimalField(db_column='Comision2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    comision3 = models.DecimalField(db_column='Comision3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    comision4 = models.DecimalField(db_column='Comision4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantlimite1 = models.DecimalField(db_column='CantLimite1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantlimite2 = models.DecimalField(db_column='CantLimite2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantlimite3 = models.DecimalField(db_column='CantLimite3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantlimite4 = models.DecimalField(db_column='CantLimite4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idcuentaactivo = models.IntegerField(db_column='IdCuentaActivo')  # Field name made lowercase.
    idcuentacosto = models.IntegerField(db_column='IdCuentaCosto')  # Field name made lowercase.
    idcuentaventa = models.IntegerField(db_column='IdCuentaVenta')  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=10)  # Field name made lowercase.
    idgrupo1 = models.IntegerField(db_column='IdGrupo1', blank=True, null=True)  # Field name made lowercase.
    idgrupo2 = models.IntegerField(db_column='IdGrupo2', blank=True, null=True)  # Field name made lowercase.
    idgrupo3 = models.IntegerField(db_column='IdGrupo3', blank=True, null=True)  # Field name made lowercase.
    idgrupo4 = models.IntegerField(db_column='IdGrupo4', blank=True, null=True)  # Field name made lowercase.
    idgrupo5 = models.IntegerField(db_column='IdGrupo5', blank=True, null=True)  # Field name made lowercase.
    idproveedor = models.IntegerField(db_column='IdProveedor', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=80, blank=True, null=True)  # Field name made lowercase.
    existenciaminima = models.DecimalField(db_column='ExistenciaMinima', max_digits=19, decimal_places=4)  # Field name made lowercase.
    existenciamaxima = models.DecimalField(db_column='ExistenciaMaxima', max_digits=19, decimal_places=4)  # Field name made lowercase.
    unidadminimacompra = models.DecimalField(db_column='UnidadMinimaCompra', max_digits=19, decimal_places=4)  # Field name made lowercase.
    unidadminimaventa = models.DecimalField(db_column='UnidadMinimaVenta', max_digits=19, decimal_places=4)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    bandservicio = models.BooleanField(db_column='BandServicio')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    valorrecargo = models.DecimalField(db_column='ValorRecargo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descuento1 = models.DecimalField(db_column='Descuento1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descuento2 = models.DecimalField(db_column='Descuento2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descuento3 = models.DecimalField(db_column='Descuento3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descuento4 = models.DecimalField(db_column='Descuento4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    bandfraccion = models.BooleanField(db_column='bandFraccion')  # Field name made lowercase.
    bandarea = models.BooleanField(db_column='bandArea')  # Field name made lowercase.
    bandventa = models.BooleanField(db_column='bandVenta')  # Field name made lowercase.
    idunidad = models.IntegerField(db_column='IdUnidad', blank=True, null=True)  # Field name made lowercase.
    idunidadconteo = models.IntegerField(db_column='IdUnidadConteo', blank=True, null=True)  # Field name made lowercase.
    costoultimoingreso = models.DecimalField(db_column='CostoUltimoIngreso', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bandiva = models.BooleanField(db_column='BandIVA', blank=True, null=True)  # Field name made lowercase.
    porcentajeice = models.DecimalField(db_column='PorcentajeICE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pordesperdicio = models.DecimalField(db_column='PorDesperdicio', max_digits=19, decimal_places=4)  # Field name made lowercase.
    rutafoto = models.CharField(db_column='Rutafoto', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tiposri = models.IntegerField(db_column='TipoSRI', blank=True, null=True)  # Field name made lowercase.
    idice = models.IntegerField(db_column='IdICE', blank=True, null=True)  # Field name made lowercase.
    precio5 = models.DecimalField(db_column='Precio5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    comision5 = models.DecimalField(db_column='Comision5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantlimite5 = models.DecimalField(db_column='CantLimite5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descuento5 = models.DecimalField(db_column='Descuento5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantrelunidad = models.IntegerField(db_column='CantRelUnidad')  # Field name made lowercase.
    cantrelunidadcont = models.IntegerField(db_column='CantRelUnidadCont')  # Field name made lowercase.
    descripcion2 = models.CharField(db_column='Descripcion2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    pesoneto = models.DecimalField(db_column='PesoNeto', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pesobruto = models.DecimalField(db_column='PesoBruto', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idunidadpeso = models.IntegerField(db_column='IdUnidadPeso', blank=True, null=True)  # Field name made lowercase.
    bandconversion = models.BooleanField(db_column='BandConversion')  # Field name made lowercase.
    bandrepgastos = models.BooleanField(db_column='BandRepGastos')  # Field name made lowercase.
    bandnosefactura = models.BooleanField(db_column='BandNoSeFactura')  # Field name made lowercase.
    tiempopromvta = models.DecimalField(db_column='TiempoPromVta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tiemporeposicion = models.DecimalField(db_column='TiempoReposicion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipo1 = models.IntegerField(db_column='Tipo1')  # Field name made lowercase.
    idproceso = models.IntegerField(db_column='idProceso')  # Field name made lowercase.
    utilidad = models.DecimalField(db_column='Utilidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    costoreferencial = models.DecimalField(db_column='CostoReferencial', max_digits=19, decimal_places=4)  # Field name made lowercase.
    utilidad1 = models.DecimalField(db_column='Utilidad1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    utilidad2 = models.DecimalField(db_column='Utilidad2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    utilidad3 = models.DecimalField(db_column='Utilidad3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    utilidad4 = models.DecimalField(db_column='Utilidad4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    utilidad5 = models.DecimalField(db_column='Utilidad5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    bandmodprecio = models.BooleanField(db_column='BandModPrecio')  # Field name made lowercase.
    idarancel = models.IntegerField(db_column='idArancel')  # Field name made lowercase.
    bandconversionuni = models.BooleanField(db_column='bandConversionUni')  # Field name made lowercase.
    precio6 = models.DecimalField(db_column='Precio6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    comision6 = models.DecimalField(db_column='Comision6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantlimite6 = models.DecimalField(db_column='CantLimite6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descuento6 = models.DecimalField(max_digits=19, decimal_places=4)
    bandaltarotacion = models.BooleanField(db_column='BandAltaRotacion')  # Field name made lowercase.
    bandnoobjetoiva = models.BooleanField(db_column='BandNoObjetoIVA')  # Field name made lowercase.
    bandgarantia = models.BooleanField(db_column='BandGarantia')  # Field name made lowercase.
    idcuentadiferida = models.IntegerField(db_column='IdCuentaDiferida')  # Field name made lowercase.
    tipoauto = models.IntegerField(db_column='tipoAuto')  # Field name made lowercase.
    bandcambiadescr = models.BooleanField(db_column='BandCambiaDescr')  # Field name made lowercase.
    bandserie = models.BooleanField(db_column='BandSerie')  # Field name made lowercase.
    precio7 = models.DecimalField(db_column='Precio7', max_digits=19, decimal_places=4)  # Field name made lowercase.
    utilidad7 = models.DecimalField(db_column='Utilidad7', max_digits=19, decimal_places=4)  # Field name made lowercase.
    comision7 = models.DecimalField(db_column='Comision7', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantlimite7 = models.DecimalField(db_column='CantLimite7', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descuento7 = models.DecimalField(max_digits=19, decimal_places=4)
    frecuenciareposicion = models.DecimalField(db_column='FrecuenciaReposicion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    buffer = models.DecimalField(db_column='Buffer', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechamodbuffer = models.DateTimeField(db_column='FechaModBuffer', blank=True, null=True)  # Field name made lowercase.
    bandpeso = models.BooleanField(db_column='BandPeso')  # Field name made lowercase.
    idgrupo6 = models.IntegerField(blank=True, null=True)
    cantidadrelunidad = models.DecimalField(db_column='CantidadRelUnidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantidadrelunidadcont = models.DecimalField(db_column='CantidadRelUnidadCont', max_digits=19, decimal_places=4)  # Field name made lowercase.
    frecuenciareposicionalm = models.DecimalField(db_column='FrecuenciaReposicionALM', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tiemporeposicionalm = models.DecimalField(db_column='TiempoReposicionALM', max_digits=19, decimal_places=4)  # Field name made lowercase.
    bandomitirrebate = models.BooleanField(db_column='BandOmitirRebate')  # Field name made lowercase.
    porcentajeivaant = models.DecimalField(db_column='PorcentajeIVAAnt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    batch = models.DecimalField(db_column='Batch', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    batchprod = models.DecimalField(db_column='BatchProd', max_digits=19, decimal_places=4)  # Field name made lowercase.
    bandnoformula = models.DecimalField(db_column='BandNoFormula', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantreluni = models.DecimalField(db_column='CantReluni', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantrelunicont = models.DecimalField(db_column='CantReluniCont', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idcuentadevolucion = models.IntegerField(db_column='IdCuentaDevolucion')  # Field name made lowercase.
    img1 = models.TextField(blank=True, null=True)
    img2 = models.TextField(blank=True, null=True)
    img3 = models.TextField(blank=True, null=True)
    m3 = models.FloatField(db_column='M3')  # Field name made lowercase.
    cantreuni = models.DecimalField(db_column='CantReUni', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantreunicont = models.DecimalField(db_column='CantReUniCont', max_digits=19, decimal_places=4)  # Field name made lowercase.
    bandgarantiac = models.BooleanField(db_column='BandGarantiaC')  # Field name made lowercase.
    bandgarantiav = models.BooleanField(db_column='BandGarantiaV')  # Field name made lowercase.
    pordescpp = models.DecimalField(db_column='PorDescPP', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idvol = models.IntegerField(db_column='idVol')  # Field name made lowercase.
    bandnopedir = models.IntegerField(db_column='bandNoPedir')  # Field name made lowercase.
    bandpromocion = models.BooleanField(db_column='bandPromocion')  # Field name made lowercase.
    bandmovil = models.BooleanField(db_column='bandMovil')  # Field name made lowercase.
    varianza = models.DecimalField(db_column='Varianza', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idproveedorprin = models.IntegerField(db_column='idProveedorPrin')  # Field name made lowercase.
    bandtienelote = models.IntegerField(db_column='bandtieneLote')  # Field name made lowercase.
    idproveedorsec = models.IntegerField(db_column='idProveedorSec')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVInventario'


class Ivkardex(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    transid = models.IntegerField(db_column='TransID')  # Field name made lowercase.
    idinventario = models.IntegerField(db_column='IdInventario')  # Field name made lowercase.
    idbodega = models.IntegerField(db_column='IdBodega')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    costototal = models.DecimalField(db_column='CostoTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    costorealtotal = models.DecimalField(db_column='CostoRealTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    preciototal = models.DecimalField(db_column='PrecioTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    preciorealtotal = models.DecimalField(db_column='PrecioRealTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    iva = models.DecimalField(db_column='IVA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.
    nota = models.CharField(db_column='Nota', max_length=300, blank=True, null=True)  # Field name made lowercase.
    numeroprecio = models.SmallIntegerField(db_column='NumeroPrecio')  # Field name made lowercase.
    valorrecargoitem = models.DecimalField(db_column='ValorRecargoItem', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tiempoentrega = models.CharField(db_column='TiempoEntrega', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bandimprimir = models.BooleanField(db_column='bandImprimir')  # Field name made lowercase.
    valoriceitem = models.DecimalField(db_column='ValorICEItem', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idice = models.IntegerField(db_column='IdICE', blank=True, null=True)  # Field name made lowercase.
    idpadre = models.IntegerField(db_column='idPadre', blank=True, null=True)  # Field name made lowercase.
    bandver = models.BooleanField()
    idpadresub = models.IntegerField(db_column='idPadreSub', blank=True, null=True)  # Field name made lowercase.
    nota1 = models.CharField(max_length=40, blank=True, null=True)
    tamano = models.CharField(db_column='Tamaño', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fechalleva = models.DateTimeField(db_column='Fechalleva')  # Field name made lowercase.
    fechadevol = models.DateTimeField(db_column='FechaDevol')  # Field name made lowercase.
    numdias = models.DecimalField(db_column='NumDias', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descuentooriginal = models.DecimalField(db_column='DescuentoOriginal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    arancel = models.DecimalField(db_column='Arancel', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ice = models.DecimalField(db_column='ICE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fodin = models.DecimalField(db_column='FODIN', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comision = models.DecimalField(db_column='Comision', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoreferencial = models.DecimalField(db_column='CostoReferencial', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idcentrocosto = models.IntegerField(db_column='idCentroCosto', blank=True, null=True)  # Field name made lowercase.
    recargoarancel = models.DecimalField(db_column='RecargoArancel', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rebate = models.DecimalField(db_column='Rebate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidaddou = models.FloatField(db_column='CantidadDou')  # Field name made lowercase.
    costototaldou = models.FloatField(db_column='CostoTotalDou')  # Field name made lowercase.
    costorealtotaldou = models.FloatField(db_column='CostoRealTotalDou')  # Field name made lowercase.
    preciototaldou = models.FloatField(db_column='PrecioTotalDou')  # Field name made lowercase.
    preciorealtotaldou = models.FloatField(db_column='PrecioRealTotalDou')  # Field name made lowercase.
    idunidadconv = models.IntegerField(db_column='idUnidadConv')  # Field name made lowercase.
    cantidadconv = models.FloatField(db_column='CantidadConv')  # Field name made lowercase.
    idreceta = models.IntegerField(db_column='idReceta')  # Field name made lowercase.
    descuentopp = models.DecimalField(db_column='DescuentoPP', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idafectado = models.IntegerField(db_column='idAfectado')  # Field name made lowercase.
    idcomensal = models.IntegerField(db_column='idComensal')  # Field name made lowercase.
    valorice = models.DecimalField(db_column='ValorICE', max_digits=19, decimal_places=4)  # Field name made lowercase.
    bandpromocion = models.BooleanField(db_column='bandPromocion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVKardex'


class Ivkardexrecargo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    transid = models.IntegerField(db_column='TransID')  # Field name made lowercase.
    idrecargo = models.IntegerField(db_column='IdRecargo')  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4)  # Field name made lowercase.
    valor = models.DecimalField(db_column='Valor', max_digits=19, decimal_places=4)  # Field name made lowercase.
    bandmodificable = models.BooleanField(db_column='BandModificable')  # Field name made lowercase.
    bandorigen = models.SmallIntegerField(db_column='BandOrigen')  # Field name made lowercase.
    bandprorrateado = models.BooleanField(db_column='BandProrrateado')  # Field name made lowercase.
    afectaivaitem = models.BooleanField(db_column='AfectaIvaItem')  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVKardexRecargo'


class Pcgrupo1(models.Model):
    idgrupo1 = models.AutoField(db_column='IdGrupo1', primary_key=True)  # type: ignore # Field name made lowercase.
    codgrupo1 = models.CharField(db_column='CodGrupo1', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', unique=True, max_length=50)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    preciosdisponibles = models.CharField(db_column='PreciosDisponibles', max_length=7, blank=True, null=True)  # Field name made lowercase.
    origen = models.CharField(db_column='Origen', max_length=1, blank=True, null=True)  # Field name made lowercase.
    numeropagos = models.IntegerField(db_column='NumeroPagos', blank=True, null=True)  # Field name made lowercase.
    intervalo = models.IntegerField(db_column='Intervalo', blank=True, null=True)  # Field name made lowercase.
    banddias = models.BooleanField(db_column='BandDias', blank=True, null=True)  # Field name made lowercase.
    idgasto = models.IntegerField(db_column='IdGasto')  # Field name made lowercase.
    idturno = models.IntegerField(db_column='idTurno')  # Field name made lowercase.
    numpreciopre = models.IntegerField(db_column='NumPrecioPre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PCGrupo1'


class Pcgrupo2(models.Model):
    idgrupo2 = models.AutoField(db_column='IdGrupo2', primary_key=True)  # Field name made lowercase.
    codgrupo2 = models.CharField(db_column='CodGrupo2', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', unique=True, max_length=50)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    preciosdisponibles = models.CharField(db_column='PreciosDisponibles', max_length=7, blank=True, null=True)  # Field name made lowercase.
    origen = models.CharField(db_column='Origen', max_length=1, blank=True, null=True)  # Field name made lowercase.
    numeropagos = models.IntegerField(db_column='NumeroPagos', blank=True, null=True)  # Field name made lowercase.
    intervalo = models.IntegerField(db_column='Intervalo', blank=True, null=True)  # Field name made lowercase.
    banddias = models.BooleanField(db_column='BandDias', blank=True, null=True)  # Field name made lowercase.
    idgasto = models.IntegerField(db_column='IdGasto')  # Field name made lowercase.
    idturno = models.IntegerField(db_column='idTurno')  # Field name made lowercase.
    numpreciopre = models.IntegerField(db_column='NumPrecioPre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PCGrupo2'


class Pcgrupo3(models.Model):
    idgrupo3 = models.AutoField(db_column='IdGrupo3', primary_key=True)  # Field name made lowercase.
    codgrupo3 = models.CharField(db_column='CodGrupo3', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', unique=True, max_length=50)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    preciosdisponibles = models.CharField(db_column='PreciosDisponibles', max_length=7, blank=True, null=True)  # Field name made lowercase.
    origen = models.CharField(db_column='Origen', max_length=1, blank=True, null=True)  # Field name made lowercase.
    numeropagos = models.IntegerField(db_column='NumeroPagos', blank=True, null=True)  # Field name made lowercase.
    intervalo = models.IntegerField(db_column='Intervalo', blank=True, null=True)  # Field name made lowercase.
    banddias = models.BooleanField(db_column='BandDias', blank=True, null=True)  # Field name made lowercase.
    idgasto = models.IntegerField(db_column='IdGasto')  # Field name made lowercase.
    idturno = models.IntegerField(db_column='idTurno')  # Field name made lowercase.
    numpreciopre = models.IntegerField(db_column='NumPrecioPre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PCGrupo3'


class Pcgrupo4(models.Model):
    idgrupo4 = models.AutoField(db_column='IdGrupo4', primary_key=True)  # Field name made lowercase.
    codgrupo4 = models.CharField(db_column='CodGrupo4', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', unique=True, max_length=50)  # Field name made lowercase.
    bandvalida = models.BooleanField(db_column='BandValida')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    preciosdisponibles = models.CharField(db_column='PreciosDisponibles', max_length=7, blank=True, null=True)  # Field name made lowercase.
    origen = models.CharField(db_column='Origen', max_length=1, blank=True, null=True)  # Field name made lowercase.
    numeropagos = models.IntegerField(db_column='NumeroPagos', blank=True, null=True)  # Field name made lowercase.
    intervalo = models.IntegerField(db_column='Intervalo', blank=True, null=True)  # Field name made lowercase.
    banddias = models.BooleanField(db_column='BandDias', blank=True, null=True)  # Field name made lowercase.
    idgasto = models.IntegerField(db_column='IdGasto')  # Field name made lowercase.
    idturno = models.IntegerField(db_column='idTurno')  # Field name made lowercase.
    numpreciopre = models.IntegerField(db_column='NumPrecioPre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PCGrupo4'


class Pcprovcli(models.Model):
    idprovcli = models.AutoField(db_column='IdProvCli', primary_key=True)  # Field name made lowercase.
    codprovcli = models.CharField(db_column='CodProvCli', unique=True, max_length=20)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=256, blank=True, null=True)  # Field name made lowercase.
    bandproveedor = models.BooleanField(db_column='BandProveedor')  # Field name made lowercase.
    bandcliente = models.BooleanField(db_column='BandCliente')  # Field name made lowercase.
    idcuentacontable = models.IntegerField(db_column='IdCuentaContable')  # Field name made lowercase.
    direccion1 = models.CharField(db_column='Direccion1', max_length=80, blank=True, null=True)  # Field name made lowercase.
    direccion2 = models.CharField(db_column='Direccion2', max_length=80, blank=True, null=True)  # Field name made lowercase.
    codpostal = models.CharField(db_column='CodPostal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=20, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telefono1 = models.CharField(db_column='Telefono1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telefono2 = models.CharField(db_column='Telefono2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telefono3 = models.CharField(db_column='Telefono3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=250, blank=True, null=True)  # Field name made lowercase.
    limitecredito = models.DecimalField(db_column='LimiteCredito', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    banco = models.CharField(db_column='Banco', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numcuenta = models.CharField(db_column='NumCuenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    swit = models.CharField(db_column='Swit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direcbanco = models.CharField(db_column='DirecBanco', max_length=80, blank=True, null=True)  # Field name made lowercase.
    telbanco = models.CharField(db_column='TelBanco', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idvendedor = models.IntegerField(db_column='IdVendedor', blank=True, null=True)  # Field name made lowercase.
    idgrupo1 = models.IntegerField(db_column='IdGrupo1', blank=True, null=True)  # Field name made lowercase.
    idgrupo2 = models.IntegerField(db_column='IdGrupo2', blank=True, null=True)  # Field name made lowercase.
    idgrupo3 = models.IntegerField(db_column='IdGrupo3', blank=True, null=True)  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='Estado')  # Field name made lowercase.
    fechagrabado = models.DateTimeField(db_column='FechaGrabado', blank=True, null=True)  # Field name made lowercase.
    idcuentacontable2 = models.IntegerField(db_column='IdCuentaContable2')  # Field name made lowercase.
    tipodocumento = models.CharField(db_column='TipoDocumento', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=5, blank=True, null=True)  # Field name made lowercase.
    numautsri = models.CharField(db_column='NumAutSRI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombrealterno = models.CharField(db_column='NombreAlterno', max_length=256, blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateTimeField(db_column='FechaNacimiento')  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega')  # Field name made lowercase.
    fechaexpiracion = models.DateTimeField(db_column='FechaExpiracion')  # Field name made lowercase.
    totaldebe = models.DecimalField(db_column='TotalDebe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    totalhaber = models.DecimalField(db_column='TotalHaber', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idgrupo4 = models.IntegerField(db_column='idGrupo4', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tipoprovcli = models.CharField(db_column='TipoProvCli', max_length=20, blank=True, null=True)  # Field name made lowercase.
    referidopor = models.CharField(db_column='ReferidoPor', max_length=80, blank=True, null=True)  # Field name made lowercase.
    idtipodocumento = models.IntegerField(db_column='IdTipoDocumento', blank=True, null=True)  # Field name made lowercase.
    bandempresapublica = models.BooleanField(db_column='BandEmpresaPublica')  # Field name made lowercase.
    idgarante = models.IntegerField(db_column='IdGarante', blank=True, null=True)  # Field name made lowercase.
    bandgarante = models.BooleanField(db_column='BandGarante')  # Field name made lowercase.
    diasplazo = models.DecimalField(db_column='DiasPlazo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    codigousuario = models.CharField(db_column='CodigoUsuario', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idprovincia = models.IntegerField(db_column='idProvincia')  # Field name made lowercase.
    idcanton = models.IntegerField(db_column='idCanton')  # Field name made lowercase.
    idparroquia = models.IntegerField(db_column='idParroquia')  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='FechaCreacion', blank=True, null=True)  # Field name made lowercase.
    bandempleado = models.BooleanField(db_column='BandEmpleado')  # Field name made lowercase.
    numserie = models.CharField(db_column='NumSerie', max_length=3, blank=True, null=True)  # Field name made lowercase.
    numpunto = models.CharField(db_column='numPunto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fechacaducidad = models.DateTimeField(db_column='FechaCaducidad', blank=True, null=True)  # Field name made lowercase.
    iddiascredito = models.IntegerField(db_column='IdDiasCredito', blank=True, null=True)  # Field name made lowercase.
    fechalote1 = models.DateTimeField(db_column='FechaLote1')  # Field name made lowercase.
    fechalote2 = models.DateTimeField(db_column='FechaLote2')  # Field name made lowercase.
    bandlote = models.BooleanField(db_column='BandLote')  # Field name made lowercase.
    numpagos = models.IntegerField(db_column='NumPagos')  # Field name made lowercase.
    intervalo = models.IntegerField(db_column='Intervalo')  # Field name made lowercase.
    pordescneto = models.IntegerField(db_column='PorDescNeto')  # Field name made lowercase.
    pordescpp = models.IntegerField(db_column='PorDescPP')  # Field name made lowercase.
    bandrucvalido = models.BooleanField(db_column='BandRUCValido', blank=True, null=True)  # Field name made lowercase.
    tipoturno = models.IntegerField(db_column='TipoTurno', blank=True, null=True)  # Field name made lowercase.
    idturno = models.IntegerField(db_column='idTurno')  # Field name made lowercase.
    bandrelacionado = models.BooleanField(db_column='BandRelacionado', blank=True, null=True)  # Field name made lowercase.
    bandomitirpendientes = models.BooleanField(db_column='BandOmitirPendientes', blank=True, null=True)  # Field name made lowercase.
    tiposujeto = models.CharField(db_column='TipoSujeto', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    estadocivil = models.CharField(db_column='EstadoCivil', max_length=1, blank=True, null=True)  # Field name made lowercase.
    origeningresos = models.CharField(db_column='OrigenIngresos', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bandsolicitudcredito = models.BooleanField(db_column='BandSolicitudCredito')  # Field name made lowercase.
    bandsupergarante = models.BooleanField(db_column='BandSuperGarante')  # Field name made lowercase.
    descripciondetalle = models.TextField(db_column='DescripcionDetalle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nombreconyuge = models.CharField(db_column='NombreConyuge', max_length=80, blank=True, null=True)  # Field name made lowercase.
    rucconyuge = models.CharField(db_column='RUCConyuge', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codigoreloj = models.CharField(db_column='CodigoReloj', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bandomitirdinardap = models.BooleanField(db_column='BandOmitirDinardap')  # Field name made lowercase.
    idcobrador = models.IntegerField(db_column='idCobrador')  # Field name made lowercase.
    bandrebate = models.BooleanField(db_column='BandRebate')  # Field name made lowercase.
    idpais = models.IntegerField(db_column='idPais')  # Field name made lowercase.
    cordenadax = models.IntegerField(db_column='CordenadaX')  # Field name made lowercase.
    cordenaday = models.IntegerField(db_column='CordenadaY')  # Field name made lowercase.
    bandcompensaiva = models.BooleanField(db_column='bandCompensaIVA')  # Field name made lowercase.
    idcallepri = models.IntegerField(db_column='idCallePri')  # Field name made lowercase.
    idcallesec = models.IntegerField(db_column='idCalleSec')  # Field name made lowercase.
    idgarante2 = models.IntegerField(db_column='idGarante2')  # Field name made lowercase.
    posgooglemaps = models.CharField(db_column='posGoogleMaps', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numcasa = models.CharField(db_column='NumCasa', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bandesconsumidorfinal = models.BooleanField(db_column='BandEsConsumidorFinal')  # Field name made lowercase.
    bandivcodigoigual = models.BooleanField(db_column='BandIVCodigoIgual')  # Field name made lowercase.
    idcuentacontablegasto = models.IntegerField(db_column='idCuentaContableGasto')  # Field name made lowercase.
    garantia = models.CharField(db_column='Garantia', max_length=30, blank=True, null=True)  # Field name made lowercase.
    predio = models.CharField(db_column='Predio', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bandncpp = models.BooleanField(db_column='bandNCPP')  # Field name made lowercase.
    diasplazodin = models.IntegerField(db_column='diasPlazoDin')  # Field name made lowercase.
    bandequifax = models.BooleanField(db_column='bandEquifax')  # Field name made lowercase.
    ruc_new = models.CharField(db_column='RUC_NEW', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ruc = models.BinaryField(db_column='RUC', blank=True, null=True)  # Field name made lowercase.
    idvendedorcreo = models.IntegerField(db_column='idVendedorCreo')  # Field name made lowercase.
    bandmigrante = models.BooleanField(db_column='bandMigrante')  # Field name made lowercase.
    bandconsignatario = models.BooleanField(db_column='bandConsignatario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PCProvCli'


class ViewReports(models.Model):
    idvendedor = models.IntegerField(db_column='IdVendedor',primary_key=True)  # Field name made lowercase.
    nombrevendedor = models.CharField(db_column='NombreVendedor', max_length=40)  # Field name made lowercase.
    idlineasg1 = models.IntegerField(db_column='IdLineasG1', blank=True, null=True)  # Field name made lowercase.
    descripciongrupo1lineas = models.CharField(db_column='DescripcionGrupo1Lineas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idlineasg2 = models.IntegerField(db_column='IdLineasG2', blank=True, null=True)  # Field name made lowercase.
    descripciongrupo2lineas = models.CharField(db_column='DescripcionGrupo2Lineas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idlineasg3 = models.IntegerField(db_column='IdLineasG3', blank=True, null=True)  # Field name made lowercase.
    descripciongrupo3lineas = models.CharField(db_column='DescripcionGrupo3Lineas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idlineasg4 = models.IntegerField(db_column='IdLineasG4', blank=True, null=True)  # Field name made lowercase.
    descripciongrupo4lineas = models.CharField(db_column='DescripcionGrupo4Lineas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idlineasg5 = models.IntegerField(db_column='IdLineasG5', blank=True, null=True)  # Field name made lowercase.
    descripciongrupo5lineas = models.CharField(db_column='DescripcionGrupo5Lineas', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idlineasg6 = models.IntegerField(db_column='IdLineasG6', blank=True, null=True)  # Field name made lowercase.
    descripciongrupo6lineas = models.CharField(db_column='DescripcionGrupo6Lineas', max_length=60, blank=True, null=True)  # Field name made lowercase.
    descripcionitem = models.CharField(db_column='DescripcionItem', max_length=300, blank=True, null=True)  # Field name made lowercase.
    codtrans = models.CharField(max_length=5)
    numtrans = models.IntegerField()
    fechatrans = models.DateTimeField(db_column='FechaTrans')  # Field name made lowercase.
    horatrans = models.DateTimeField(db_column='HoraTrans')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    costorealtotal = models.DecimalField(db_column='CostoRealTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    preciorealtotal = models.DecimalField(db_column='PrecioRealTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    utilidad = models.DecimalField(db_column='Utilidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=20, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idg1cliente = models.IntegerField(db_column='IdG1Cliente', blank=True, null=True)  # Field name made lowercase.
    descripciong1cliente = models.CharField(db_column='DescripcionG1Cliente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idg2cliente = models.IntegerField(db_column='IdG2Cliente', blank=True, null=True)  # Field name made lowercase.
    descripciong2cliente = models.CharField(db_column='DescripcionG2Cliente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idg3cliente = models.IntegerField(db_column='IdG3Cliente', blank=True, null=True)  # Field name made lowercase.
    descripciong3cliente = models.CharField(db_column='DescripcionG3Cliente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idg4cliente = models.IntegerField(db_column='IdG4Cliente', blank=True, null=True)  # Field name made lowercase.
    descripciong4cliente = models.CharField(db_column='DescripcionG4Cliente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idcliente = models.IntegerField(db_column='IdCliente')  # Field name made lowercase.
    nombrecliente = models.CharField(db_column='NombreCliente', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_reports'

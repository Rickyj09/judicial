from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField,\
    TextAreaField, SelectField, PasswordField
from wtforms.fields.html5 import EmailField
from flask_wtf.file import FileField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, FileField, SelectField, RadioField
from wtforms import FloatField
from wtforms.validators import DataRequired, Email, Length, ValidationError, AnyOf
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField, FileRequired
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required


def validar_obvio(form, field):
    if field.data == "12345678":
        raise ValidationError('La clave debe ser más segura!!')


class buscaform(FlaskForm):
    iden = StringField('Número Reporte', validators=[DataRequired(),Length(min=10,max=14)], render_kw={"placeholder": ""})
    submit = SubmitField('Buscar')


class Publicaciones(FlaskForm):
    post = TextAreaField('Notas de las fotos', validators=[
        DataRequired(), Length(min=1, max=140)
    ])
    imagen = FileField('image')

    submit = SubmitField('Subir')


class FormArticulo(FlaskForm):
    nombre = StringField("Nombre:",
                         validators=[Required("Tienes que introducir el dato")]
                         )
    precio = DecimalField("Precio:", default=0,
                          validators=[Required("Tienes que introducir el dato")
                                      ])
    iva = IntegerField("IVA:", default=21,
                       validators=[Required("Tienes que introducir el dato")])
    descripcion = TextAreaField("Descripción:")
    photo = FileField('Selecciona imagen:')
    stock = IntegerField("Stock:", default=1,
                         validators=[Required("Tienes que introducir el dato")]
                         )
    CategoriaId = SelectField("Categoría:", coerce=int)
    submit = SubmitField('Enviar')


class FormSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')


class LoginForm(FlaskForm):
    username = StringField('User', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Entrar')


class FormUsuario(FlaskForm):
    username = StringField('Login', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    nombre = StringField('Nombre completo')
    email = EmailField('Email')
    submit = SubmitField('Aceptar')


class datos_equipo(FlaskForm):
    de_marca = StringField('MARCA', validators=[DataRequired()], render_kw={
                           "placeholder": "Marca"})
    de_serie = StringField('SERIE', validators=[DataRequired()])
    de_tipo = StringField('TIPO', validators=[DataRequired()])
    de_modelo = StringField('MODELO', validators=[DataRequired()])
    de_capacidad = StringField('CAPACIDAD', validators=[DataRequired()])
    de_horometro = StringField('HORÓMETRO', validators=[DataRequired()])
    dm_kilometraje = StringField('KILOMETRAJE', validators=[DataRequired()])
    de_anio = StringField('AÑO', validators=[DataRequired()])
    de_cod_interno = StringField('CODIGO INTERNO', validators=[DataRequired()])
    dm_marca = StringField('MARCA', validators=[DataRequired()])
    dm_serie = StringField('SERIE', validators=[DataRequired()])
    dm_modelo = StringField('MODELO', validators=[DataRequired()])
    ct_capmax = StringField('CAPACIDAD MAXIMA', validators=[DataRequired()])
    ct_longpluma = StringField('LONG PLUMA', validators=[DataRequired()])
    ct_radio = StringField('RADIO', validators=[DataRequired()])
    ct_angulo = StringField('ANGULO', validators=[DataRequired()])
    conf_caratula = RadioField('', choices=[(
        'c', 'Conforme'), ('NC', 'No Conforme')], default='C', render_kw={}, id='conf_caratula')
    marca = StringField('MARCA', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    placa = StringField('PLACA/SERIE', validators=[DataRequired()])
    bloque_carga = StringField('CAPACIDAD BLOQUE PRINCIPAL', validators=[DataRequired()])
    numero_estabi = StringField('Nº DE ESTABILIZADORES', validators=[DataRequired()])
    tipo_montaje = StringField('TIPO DE MONTAJE', validators=[DataRequired()])

    submit = SubmitField('Enviar')




class list_formulario(FlaskForm):
    nombre = SelectField('Formulario', choices=[('Reporte Inspeccion Poleas', 'Poleas'), ('Formato Inspección visual Eslinga Cable Acero', 'Eslinga Cable Acero'),('Reporte Inspección Cadena','Cadena'),('Reporte Inspección visual Eslinga Faja Sintética','Eslinga Faja Sintética'),('Reporte Inspección visual Ganchos','Ganchos'),('Reporte Inspección visual Grilletes','Grilletes'),('Reporte Inspeccion King Pin','King Pin'),('Reporte Inspeccion Quinta Rueda','Quinta Rueda'),('Reporte Inspeccion Sistemas de Elevación de Personal','Sistemas de Elevación de Personal'),('Reporte Inspeccion Horquillas','Horquillas'),('Reporte Inspección  Pasteca Principal','Pasteca Principal'),('Reporte Inspeccion Pasteca Auxiliar','Pasteca Auxiliar'),('Reporte Inspección Aparejos','Aparejos'),('Reporte Inspección Tensor Trinquete','Tensor Trinquete')])
    
    submit = SubmitField('Enviar')

class formu1(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'DIRECTA', 'DIRECTA'), ('INDIRECTA', 'INDIRECTA')], default='D', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('NATURAL', 'NATURAL'), ('ASISTIDA', 'ASISTIDA')], default='N', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[(
        'AMBIENTE', 'AMBIENTE'), ('HORNO', 'HORNO')], default='AMBIENTE', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN ', validators=[DataRequired()])
    

    submit = SubmitField('Enviar')


class formu1_1(FlaskForm):
    ref = StringField('REFERENCIA', validators=[DataRequired()])
    ancho = StringField('ANCHO (mm)', validators=[DataRequired()])
    diam = StringField('DIÁMETRO (mm)', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')

    submit = SubmitField('Enviar')


class formu2(FlaskForm):
    
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'DIRECTA', 'DIRECTA'), ('INDIRECTA', 'INDIRECTA')], default='DIRECTA', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('NATURAL', 'NATURAL'), ('ASISTIDA', 'ASISTIDA')], default='NATURAL', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    elem_ens = StringField('ELEMENTO A ENSAYAR', validators=[DataRequired()])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[(
        'AMBIENTE', 'AMBIENTE'), ('HORNO', 'HORNO')], default='AMBIENTE', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN ', validators=[DataRequired()])
    
    submit = SubmitField('Enviar')


class formu2_2(FlaskForm):
    ref = StringField('REFERENCIA', validators=[DataRequired()])
    tipo_ter = StringField('TIPO DE TERMINAL', validators=[DataRequired()])
    medidas = StringField('MEDIDAS (mm)', validators=[DataRequired()])
    capac = StringField('CAPACIDAD (Kg)', validators=[DataRequired()])
    dia_elin = StringField('DIAMETRO ESLINGA (mm)',
                           validators=[DataRequired()])
    med_aces = StringField('MEDIDA DEL ACCESORIO (mm)',
                           validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')



    submit = SubmitField('Enviar')


class formu3(FlaskForm):
    
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'DIRECTA', 'DIRECTA'), ('INDIRECTA', 'INDIRECTA')], default='DIRECTA', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('N', 'NATURAL'), ('A', 'ASISTIDA')], default='N', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[
                          ('AMBIENTE', 'AMBIENTE'), ('HORNO', 'HORNO')], default='AMBIENTE', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN ', validators=[DataRequired()])

    submit = SubmitField('Enviar')


class formu3_3(FlaskForm):
    tipo_ace = StringField('TIPO DE ACCESORIO (mm)', validators=[DataRequired()])
    ref = StringField('REFERENCIA', validators=[DataRequired()])
    eslabon = StringField('ESLABÓN (diámetro) mm', validators=[DataRequired()])
    medidas = StringField('MEDIDAS (mm)', validators=[DataRequired()])
    capac = StringField('CAPACIDAD (Kg)', validators=[DataRequired()])
    gancho1 = StringField('GANCHO 1 (E-B) mm', validators=[DataRequired()])
    gancho2 = StringField('GANCHO 2 (E-B) mm', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')



    submit = SubmitField('Enviar')

class formu4(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'DIRECTA', 'DIRECTA'), ('INDIRECTA', 'INDIRECTA')], default='DIRECTA', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('NATURAL', 'NATURAL'), ('ASISTIDA', 'ASISTIDA')], default='NATURAL', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN ', validators=[DataRequired()])
    

    submit = SubmitField('Enviar')



class formu4_4(FlaskForm):
    ref = StringField('REFERENCIA', validators=[DataRequired()])
    tipo = StringField('TIPO', validators=[DataRequired()])
    medidas = StringField('MEDIDAS (mm)', validators=[DataRequired()])
    capac = StringField('CAPACIDAD (Kg)', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
   

    submit = SubmitField('Enviar')




class formu5(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'DIRECTA', 'DIRECTA'), ('INDIRECTA', 'INDIRECTA')], default='DIRECTA', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('N', 'NATURAL'), ('A', 'ASISTIDA')], default='N', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    elem_en = StringField('ELEMENTO A ENSAYAR', validators=[DataRequired()])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[
                          ('AMBIENTE', 'AMBIENTE'), ('HORNO', 'HORNO')], default='AMBIENTE', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN ', validators=[DataRequired()])
   

    submit = SubmitField('Enviar')



class formu5_5(FlaskForm):
    ref = StringField('REFERENCIA', validators=[DataRequired()])
    asiento = StringField('ASIENTO (mm)', validators=[DataRequired()])
    medidas = StringField('MEDIDAS (mm)', validators=[DataRequired()])
    capac = StringField('CAPACIDAD (Kg)', validators=[DataRequired()])
    garganta = StringField('GARGANTA (mm)', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt') 



    submit = SubmitField('Enviar')



class formu6(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'DIRECTA', 'DIRECTA'), ('INDIRECTA', 'INDIRECTA')], default='DIRECTA', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('N', 'NATURAL'), ('A', 'ASISTIDA')], default='N', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    elem_en = StringField('ELEMENTO A ENSAYAR', validators=[DataRequired()])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[
                          ('AMBIENTE', 'AMBIENTE'), ('HORNO', 'HORNO')], default='AMBIENTE', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN ', validators=[DataRequired()])
   

    submit = SubmitField('Enviar')


class formu6_6(FlaskForm):
    ref = StringField('REFERENCIA', validators=[DataRequired()])
    medidas = StringField('MEDIDAS (mm)', validators=[DataRequired()])
    capac = StringField('CAPACIDAD (Kg)', validators=[DataRequired()])
    diam_cue = StringField('DIÁMETRO DE CUERPO (mm)', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')  



    submit = SubmitField('Enviar')



class formu7(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'DIRECTA', 'DIRECTA'), ('INDIRECTA', 'INDIRECTA')], default='DIRECTA', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('NATURAL', 'NATURAL'), ('ASISTIDA', 'ASISTIDA')], default='NATURAL', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    elem_en = StringField('ELEMENTO A ENSAYAR', validators=[DataRequired()])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[
                          ('A', 'AMBIENTE'), ('H', 'HORNO')], default='A', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    marca = StringField('MARCA', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN ', validators=[DataRequired()])
    marca_pk = StringField('MARCA', validators=[DataRequired()])
    iden_pk = StringField('IDENTIFICACIÓN', validators=[DataRequired()])
    modelo_pk = StringField('MODELO', validators=[DataRequired()])
    capac_pk = StringField('CAPACIDAD', validators=[DataRequired()])
    dia_sup = StringField('Ø diámetro superior (A)  mm',
                          validators=[DataRequired()])
    dia_cen = StringField('Ø  diámetro central (B) mm',
                          validators=[DataRequired()])
    dia_inf = StringField('Ø  diámetro inferior (C) mm',
                          validators=[DataRequired()])
    obs = StringField('OBSERVACIONES', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt') 

    submit = SubmitField('Enviar')




class formu8(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'DIRECTA', 'DIRECTA'), ('INDIRECTA', 'INDIRECTA')], default='DIRECTA', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('N', 'NATURAL'), ('A', 'ASISTIDA')], default='N', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[
                          ('AMBIENTE', 'AMBIENTE'), ('HORNO', 'HORNO')], default='AMBIENTE', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    marca = StringField('MARCA', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN ', validators=[DataRequired()])
    marca_pk = StringField('MARCA', validators=[DataRequired()])
    iden_pk = StringField('IDENTIFICACIÓN', validators=[DataRequired()])
    modelo_pk = StringField('MODELO', validators=[DataRequired()])
    capac_pk = StringField('CAPACIDAD', validators=[DataRequired()])
    obs = StringField('OBSERVACIONES', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')

    submit = SubmitField('Enviar')


class formu9(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'DIRECTA', 'DIRECTA'), ('INDIRECTA', 'INDIRECTA')], default='DIRECTA', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('NATURAL', 'NATURAL'), ('ASISTIDA', 'ASISTIDA')], default='NATURAL', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[
                          ('AMBIENTE', 'AMBIENTE'), ('HORNO', 'HORNO')], default='AMBIENTE', render_kw={}, id='tipo_sec')
    marca_pk = StringField('MARCA', validators=[DataRequired()])
    iden_pk = StringField('IDENTIFICACIÓN', validators=[DataRequired()])
    modelo_pk = StringField('MODELO', validators=[DataRequired()])
    capac_pk = StringField('CAPACIDAD', validators=[DataRequired()])
    obs = StringField('OBSERVACIONES', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')

    submit = SubmitField('Enviar')


class formu10(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'D', 'DIRECTA'), ('I', 'INDIRECTA')], default='D', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('N', 'NATURAL'), ('A', 'ASISTIDA')], default='N', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[
                          ('A', 'AMBIENTE'), ('H', 'HORNO')], default='A', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN', validators=[DataRequired()])
    marca_hd = StringField('MARCA', validators=[DataRequired()])
    iden_hd = StringField('IDENTIFICACIÓN', validators=[DataRequired()])
    modelo_hd = StringField('MODELO', validators=[DataRequired()])
    capac_hd = StringField('CAPACIDAD', validators=[DataRequired()])
    medidas_hd = StringField(
        'MEDIDAS (ESPESOR, ANCHO, LONGITUD)(mm)', validators=[DataRequired()])
    marca_hi = StringField('MARCA', validators=[DataRequired()])
    iden_hi = StringField('IDENTIFICACIÓN', validators=[DataRequired()])
    modelo_hi = StringField('MODELO', validators=[DataRequired()])
    capac_hi = StringField('CAPACIDAD', validators=[DataRequired()])
    medidas_hi = StringField(
        'MEDIDAS (ESPESOR, ANCHO, LONGITUD)(mm)', validators=[DataRequired()])
    desghd = StringField('DESGASTE  HORQUILLA DERECHA', validators=[DataRequired()])
    desapd = StringField('DESALINEACIÓN PUNTAS DERECHA', validators=[DataRequired()])
    vastagod = StringField('VÁSTAGO', validators=[DataRequired()])
    hojad = StringField('HOJA DERECHA', validators=[DataRequired()])
    angulod = StringField('ANGULO DERECHA ', validators=[DataRequired()])
    obsd = StringField('OBSERVACIONES DERECHA ', validators=[DataRequired()])
    vtd = RadioField('INSPECCIÓN VISUAL DERECHA(VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    ptd = RadioField('LÍQUIDOS PENETRANTES DERECHA(PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')
    desghi = StringField('DESGASTE  HORQUILLA IZQUIERDA', validators=[DataRequired()])
    desapi = StringField('DESALINEACIÓN PUNTAS IZQUIERDA', validators=[DataRequired()])
    vastagoi = StringField('VÁSTAGO IZQUIERDA ', validators=[DataRequired()])
    hojai = StringField('HOJA IZQUIERDA', validators=[DataRequired()])
    anguloi = StringField('ANGULO IZQUIERDA', validators=[DataRequired()])
    obsi = StringField('OBSERVACIONES IZQUIERDA ', validators=[DataRequired()])
    vti = RadioField('INSPECCIÓN VISUAL IZQUIERDA(VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pti = RadioField('LÍQUIDOS PENETRANTES IZQUIERDA(PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')

    submit = SubmitField('Enviar')


class formu11(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'DIRECTA', 'DIRECTA'), ('INDIRECTA', 'INDIRECTA')], default='DIRECTA', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('NATURAL', 'NATURAL'), ('ASISTIDA', 'ASISTIDA')], default='NATURAL', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[
                          ('AMBIENTE', 'AMBIENTE'), ('HORNO', 'HORNO')], default='AMBIENTE', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN', validators=[DataRequired()])
    marca_pas = StringField('MARCA', validators=[DataRequired()])
    iden_pas = StringField('IDENTIFICACIÓN', validators=[DataRequired()])
    modelo_pas = StringField('MODELO', validators=[DataRequired()])
    capac_pas = StringField('CAPACIDAD', validators=[DataRequired()])
    numero = StringField('Nº', validators=[DataRequired()])
    asi_gan = StringField('ASIENTO GANCHO(mm)', validators=[DataRequired()])
    gar_gan = StringField('GARGANTA GANCHO(mm)', validators=[DataRequired()])
    med_gri = StringField('MEDIDAS GRILLETES(mm)', validators=[DataRequired()])
    obs = StringField('OBSERVACIONES', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')

    submit = SubmitField('Enviar')


class formu12(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'D', 'DIRECTA'), ('I', 'INDIRECTA')], default='D', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('N', 'NATURAL'), ('A', 'ASISTIDA')], default='N', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    elem_ens = StringField('ELEMENTO A ENSAYAR', validators=[DataRequired()])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[
                          ('A', 'AMBIENTE'), ('H', 'HORNO')], default='A', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN', validators=[DataRequired()])
    tipo_acce  = StringField('TIPO DE ACCESORIO ', validators=[DataRequired()])
    c1 = RadioField('1 Identificación faltante o ilegible ', choices=[
                    ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c1')
    c2 = RadioField('2 Daños por calor, salpicaduras, soldadura, golpes ', choices=[
                    ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c2')
    c3 = RadioField('3 Picaduras o corrosión excesivas', choices=[
                    ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c3')
    c4 = RadioField('4 Componentes de reemplazo no autorizados', choices=[
                    ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c4')
    c5 = RadioField('5 Componentes doblados, torcidos, estirados', choices=[
                    ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c5')
    c6 = RadioField('6 Daños visibles que causen duda', choices=[
                    ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c6')
    c7 = RadioField('7 Montaje incorrecto u otras condiciones', choices=[
                    ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c7')
    c8 = RadioField('8 Componentes alargados, agrietados o rotos', choices=[
                    ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c8')
    c9 = RadioField('9 Mellas o ranuras excesivas', choices=[
                    ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c9')
    c10 = RadioField('10 Capacidad de rotar, pivotar', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c10')
    c11 = RadioField('11 Daño excesivo hilos de rosca', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c11')
    c12 = RadioField('12 Modificaciones, soldaduras no autorizadas', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c12')
    c13 = RadioField('13 Reducción + del 10% en cualquier punto cuerpo', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c13')
    c14 = RadioField('14 Decoloración áreas frágiles o rígidas en cualquier parte', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c14')
    c15 = RadioField('15 Indicaciones de cable dañado', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c15')
    c16 = RadioField('16 Carbonización de cualquier parte de cinta', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c16')
    c17 = RadioField('17 Tuercas sueltas, faltantes, pernos, pasadores de chaveta', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c17')
    c18 = RadioField('18 Capacidad de rotar, pivotar', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c18')
    c19 = RadioField('19 Costuras rotas o desgastadas en empalmes de carga', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c19')
    c20 = RadioField('20 Nudos en cualquier parte de la cinta', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c20')
    c21 = RadioField('21 Modificaciones, soldaduras no autorizadas.', choices=[
                     ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO'), ('N/A', 'NO APLICA')], default='APROBADO', id='c21')
 
    

    submit = SubmitField('Enviar')



class formu12_1(FlaskForm):
    tipo_acc = StringField('TIPO DE ACCESORIO ', validators=[DataRequired()])
    ref = StringField('REFERENCIA', validators=[DataRequired()])
    medidas = StringField('MEDIDAS (mm)', validators=[DataRequired()])
    capac = StringField('CAPACIDAD (kg)', validators=[DataRequired()])
    medida_cu = StringField('MEDIDA DEL CUERPO (mm)', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')


    submit = SubmitField('Enviar')


class formu13(FlaskForm):
    revis = StringField('REVISIÓN Nº', validators=[DataRequired()])
    nivel_il = StringField('NIVEL DE ILUMINACIÓN:',
                           validators=[DataRequired()])
    con_sup = StringField('CONDICIÓN SUPERFICIAL:',
                          validators=[DataRequired()])
    met_insp = RadioField('MÉTODO DE INSPECCIÓN:', choices=[(
        'D', 'DIRECTA'), ('I', 'INDIRECTA')], default='D', render_kw={}, id='met_insp')
    tipo_il = RadioField('TIPO DE ILUMINACIÓN:', choices=[
                         ('N', 'NATURAL'), ('A', 'ASISTIDA')], default='N', render_kw={}, id='tipo_il')
    check1 = SelectField('ESPEJOS:', choices=[(' ', ' '), ('X', 'X')])
    check2 = SelectField('LENTES:', choices=[(' ', ' '), ('X', 'X')])
    check3 = SelectField(u'OTROS:', choices=[(' ', ' '), ('X', 'X')])
    detalle = StringField('Detalla:', validators=[])
    ele_ens = StringField('ELEMENTO A ENSAYAR', validators=[DataRequired()])
    revis_p = StringField('REVISIÓN Nº', validators=[DataRequired()])
    temp_ens = StringField('TEMPERATURA DE ENSAYO',
                           validators=[DataRequired()])
    tipo_il_p = StringField('TIPO DE ILUMINACIÓN', validators=[DataRequired()])
    nivel_il_p = StringField('NIVEL DE ILUMINACIÓN',
                             validators=[DataRequired()])
    mater_base = StringField('MATERIAL BASE', validators=[DataRequired()])
    tipo_sec = RadioField('TIPO DE SECADO:', choices=[
                          ('A', 'AMBIENTE'), ('H', 'HORNO')], default='A', render_kw={}, id='tipo_sec')
    equipo = StringField('EQUIPO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    iden = StringField('IDENTIFICACIÓN', validators=[DataRequired()])


    submit = SubmitField('Enviar')


class formu13_1(FlaskForm):
    ref = StringField('REFERENCIA', validators=[DataRequired()])
    medidas = StringField('MEDIDAS (mm)', validators=[DataRequired()])
    capac = StringField('CAPACIDAD (kg)', validators=[DataRequired()])
    gancho1 = StringField('GANCHO 1 (A-E) mm', validators=[DataRequired()])
    gancho2 = StringField('GANCHO 2  (A-E) mm', validators=[DataRequired()])
    vt = RadioField('INSPECCIÓN VISUAL (VT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='vt')
    pt = RadioField('LÍQUIDOS PENETRANTES (PT)', choices=[
                    ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Aprobado', id='pt')


    submit = SubmitField('Enviar')




class CHECK_LIST():
    submit = SubmitField('Grabar')


class check_list1(FlaskForm):
    check1 = RadioField('1.- Matricula Doc Identificación', choices=[
                        ('S', 'Satisfactorio'), ('DL', 'Defecto Leve')], default='S', id='check1')
    check2 = RadioField('2. Manual de Operación', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('3. Manual de servicio-partes', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('4. Programa de Mantenimiento', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')
    check5 = RadioField('5. Registros de Reparaciones', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check5')
    check6 = RadioField('6. Tablas de Carga', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check6')
    check7 = RadioField('7. File de Inspecciones', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check7')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list2(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check6')
    check7 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check7')
    check8 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check8')
    check9 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check9')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list3(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check5')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list4(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DL', 'Defecto Leve'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check6')
    check7 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check7')
    check8 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DL', 'Defecto Leve'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check8')
    check9 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check9')
    check10 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check10')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list5(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check2')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list6(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check6')
    check7 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check7')
    check8 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check8')
    check9 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DL', 'Defecto Leve'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check9')
    check10 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check10')
    check11 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check11')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list7(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DL', 'Defecto Leve')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DL', 'Defecto Leve')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list8(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check4')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list9(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check6')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list10(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check6')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list11(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check6')
    check7 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check7')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list12(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list13(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list14(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DL', 'Defecto Leve')], default='S', render_kw={}, id='check4')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list15(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DL', 'Defecto Leve')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check5')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list16(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list17(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check6')
    check7 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check7')
    check8 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check8')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list18(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check6')
    check7 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check7')
    check8 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check8')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list19(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DL', 'Defecto Leve'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check6')
    check7 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DL', 'Defecto Leve'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check7')
    check8 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check8')
    check9 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check9')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list20(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check6')
    check7 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check7')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list21(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check5')
    check6 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check6')
    check7 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check7')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list22(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list23(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list24(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class check_list25(FlaskForm):
    check1 = RadioField(u'CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1')
    check2 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2')
    check3 = RadioField('CONDICIÓN', choices=[('S', 'Satisfactorio'), (
        'DG', 'Defecto Grave'), ('NA', 'No Aplica')], default='S', render_kw={}, id='check3')
    check4 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')
    check5 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check5')
    checkobs = TextAreaField(
        'OBSERVACIONES', validators=[], render_kw={}, id='observaciones')

    submit = SubmitField('Grabar')


class CHECK_LIST_FIN(FlaskForm):
    check1 = StringField('ZONA INSPECCIONADA ', validators=[], render_kw={})
    check2 = StringField('ENSAYO APLICADO', validators=[], render_kw={})
    check3 = StringField('REFERENCIA', validators=[], render_kw={})
    check4 = StringField('ZONA INSPECCIONADA ', validators=[], render_kw={})
    check5 = StringField('ENSAYO APLICADO', validators=[], render_kw={})
    check6 = StringField('REFERENCIA', validators=[], render_kw={})
    check7 = RadioField('CONDICIÓN', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check4')

    submit = SubmitField('Grabar')


class prueba_carga(FlaskForm):
    conforme = RadioField('', choices=[
                          ('c', 'Conforme'), ('nc', 'No Conforme')], render_kw={}, id='conforme')
    carga_utli_est = FloatField('CARGA UTILIZADA', validators=[DataRequired()])
    peso_carga_est = FloatField('PESO CARGA', validators=[DataRequired()])
    peso_aparejo_est = FloatField('PESO APAREJOS', validators=[DataRequired()])
    peso_total = FloatField('PESO TOTAL')
    long_pluma_est = FloatField('Longitud Pluma', validators=[DataRequired()])
    rad_oper_est = FloatField('Radio de Operación',
                              validators=[DataRequired()])
    ang_pluma_est = FloatField(
        'Angulo de Pluma (°)', validators=[DataRequired()])
    cap_maxima_est = FloatField(
        'Capacidad Máxima', validators=[DataRequired()])
    carga = FloatField('Carga', validators=[DataRequired()])
    ESTAB1 = FloatField('ESTAB. 1', validators=[DataRequired()])
    ESTAB2 = FloatField('ESTAB. 2', validators=[DataRequired()])
    ESTAB3 = FloatField('ESTAB. 3', validators=[DataRequired()])
    ESTAB4 = FloatField('ESTAB. 4', validators=[DataRequired()])
    carga2 = FloatField('Carga', validators=[DataRequired()])
    ESTAB12 = FloatField('ESTAB. 1', validators=[DataRequired()])
    ESTAB22 = FloatField('ESTAB. 2', validators=[DataRequired()])
    ESTAB32 = FloatField('ESTAB. 3', validators=[DataRequired()])
    ESTAB42 = FloatField('ESTAB. 4', validators=[DataRequired()])
    carga3 = FloatField('Carga', validators=[DataRequired()])
    ESTAB13 = FloatField('ESTAB. 1', validators=[DataRequired()])
    ESTAB23 = FloatField('ESTAB. 2', validators=[DataRequired()])
    ESTAB33 = FloatField('ESTAB. 3', validators=[DataRequired()])
    ESTAB43 = FloatField('ESTAB. 4', validators=[DataRequired()])

    submit = SubmitField('Grabar')


class prueba_carga3(FlaskForm):
    carga_utli_din = FloatField('CARGA UTILIZADA', validators=[DataRequired()])
    peso_carga_din = FloatField('PESO CARGA', validators=[DataRequired()])
    peso_aparejo_din = FloatField('PESO APAREJOS', validators=[DataRequired()])
    long_pluma_din = FloatField('Longitud Pluma', validators=[DataRequired()])
    rad_oper_din = FloatField('Radio de Operación',
                              validators=[DataRequired()])
    ang_pluma_din = FloatField(
        'Angulo de Pluma (°)', validators=[DataRequired()])
    cap_maxima_din = FloatField(
        'Capacidad Máxima', validators=[DataRequired()])
    check1_pru_car = RadioField('Estado de corona (tornamesa)', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check1_pru_car')
    check2_pru_car = RadioField('Sistema movimiento y frenado', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check2_pru_car')
    check3_pru_car = RadioField('Estado de los estabilizadores', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3_pru_car')
    check4_pru_car = RadioField('Condiciones de estabilidad de la máquina', choices=[(
        'S', 'Satisfactorio'), ('DG', 'Defecto Grave')], default='S', render_kw={}, id='check3_pru_car')
    conforme = RadioField('', choices=[
                          ('c', 'Conforme'), ('nc', 'No Conforme')], render_kw={}, id='conforme')

    submit = SubmitField('Grabar')


class datos_reporte(FlaskForm):
    empresa = StringField('EMPRESA', validators=[DataRequired()], render_kw={
                          "placeholder": "EMPRESA"})
    fec_inpec = DateField('FECHA DE INSPECCIÓN', validators=[
                          DataRequired()], default='', render_kw={"placeholder": "FECHA DE INSPECCIÓN"})
    fec_emision = DateField('FECHA DE EMISIÓN', validators=[
                            DataRequired()], render_kw={"placeholder": "FECHA DE EMISIÓN"})
    fec_expiracion = DateField('FECHA DE EXPIRACIÓN', validators=[
                               DataRequired()], render_kw={"placeholder": "FECHA DE EXPIRACIÓN"})
    lugar_inpec = StringField('LUGAR INSPECCIÓN', validators=[
                              DataRequired()], render_kw={"placeholder": "LUGAR INSPECCIÓN"})
    nom_inspec = SelectField('NOMBRE DEL INSPECTOR:', choices=[('DIEGO COLLAGUAZO', 'DIEGO COLLAGUAZO'), (
        'RAMIRO LOPEZ PEREZ', 'RAMIRO LOPEZ PEREZ'), ('EDUARDO LOPEZ PEREZ', 'EDUARDO LOPEZ PEREZ')], render_kw={}, id='nom_insp')

    submit = SubmitField('Enviar')


class datos_lmi(FlaskForm):
    empresa = StringField('EMPRESA', validators=[DataRequired()], render_kw={
                          "placeholder": "EMPRESA"})
    num_reporte = StringField('NÚMERO REPORTE', validators=[
                              DataRequired()], render_kw={"placeholder": "NUMERO DE REPORTE"})
    fec_inpec = DateField('FECHA DE INSPECCIÓN', validators=[
                          DataRequired()], render_kw={"placeholder": "FECHA DE INSPECCIÓN"})
    fec_emision = DateField('FECHA DE EMISIÓN', validators=[
                            DataRequired()], render_kw={"placeholder": "FECHA DE EMISIÓN"})
    fec_expiracion = DateField('FECHA DE EXPIRACIÓN', validators=[
                               DataRequired()], render_kw={"placeholder": "FECHA DE EXPIRACIÓN"})
    lugar_inpec = StringField('LUGAR INSPECCIÓN', validators=[
                              DataRequired()], render_kw={"placeholder": "LUGAR INSPECCIÓN"})
    nom_inspec = StringField('NOMBRE DEL INSPECTOR', validators=[
                             DataRequired()], render_kw={"placeholder": "NOMBRE DEL INSPECTOR"})

    submit = SubmitField('Enviar')


class FormChangePassword(FlaskForm):
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Aceptar')


class UploadForm(FlaskForm):
    photo = FileField('selecciona imagen:', validators=[FileRequired()])
    submit = SubmitField('Submit')

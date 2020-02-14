#Citador APA
def Libro():
    print('Llena todos los espacios, si no te sabes un espacio pon un punto "."')
    LibroA=input('Autor(es):')
    LibroB=input('Año de publicación:')
    LibroC=input('Titulo del libro:')
    LibroD=input('Lugar de publicación:')
    LibroE=input('Editorial:')
    print(LibroA,'.(',LibroB,').',LibroC,'.',LibroD,':',LibroE,'.')

def Revista():
    print('Llena todos los espacios, si no te sabes un espacio pon un punto "."')
    RevistaA=input('Autor(es):')
    RevistaB=input('Fecha:')
    RevistaC=input('Titulo del artículo:')
    RevistaD=input('Nombre de la revista:')
    RevistaE=input('Volumen:')
    RevistaF=input('Páginas:')
    print(RevistaA,'.(',RevistaB,').',RevistaC,'.',RevistaD,',',RevistaE,',',RevistaF,'.')

def Periodico():
    print('Llena todos los espacios, si no te sabes un espacio pon un punto "."')
    PeriodicoA=input('Autor(es):')
    PeriodicoB=input('Año de publicación:')
    PeriodicoC=input('Titulo del artículo:')
    PeriodicoD=input('Titulo del periódico:')
    PeriodicoE=input('Páginas:')
    print(PeriodicoA,'.(',PeriodicoB,').',PeriodicoC,'.',PeriodicoD,',',PeriodicoE,'.')

def Enciclopedia():
    print('Llena todos los espacios, si no te sabes un espacio pon un punto "."')
    EnciclopediaA=input('Autor(es):')
    EnciclopediaB=input('Año de publicación:')
    EnciclopediaC=input('Titulo del artículo:')
    EnciclopediaD=input('Nombre de la enciclopedia:')
    EnciclopediaE=input('Volumen:')
    EnciclopediaF=input('Páginas:')
    EnciclopediaG=input('Lugar de publicación de la enciclopedia:')
    EnciclopediaH=input('Editorial:')
    print(EnciclopediaA,'.',EnciclopediaB,'.',EnciclopediaC,'. En ',EnciclopediaD,'(',EnciclopediaE,', ',EnciclopediaF,')',EnciclopediaG,':',EnciclopediaH,'.')

def Web():
    print('Llena todos los espacios, si no te sabes un espacio pon un punto "."')
    WebA=input('Autor(es):')
    WebB=input('Año de publicación:')
    WebC=input('Título del artículo:')
    WebD=input('Fecha de recuperación del documento:')
    WebE=input('Asociación que publica el artículo:')
    WebF=input('URL:')
    print(WebA,'.(',WebB,').',WebC,'.',WebD,',de ',WebE,' Sitio web:',WebF)

APA=input('''A) Libro\nB) Revista\nC) Periodico\nD) Enciclopedia\nE) Web\n¿A que formato deseas convertir?: ''')
if APA==('A') or ('a'):
    print(Libro())
if APA==('B') or ('b'):
    print(Revista())
if APA==('C') or ('c'):
    print(Periodico())
if APA==('D') or ('d'):
    print(Enciclopedia())
if APA==('E') or ('e'):
    print(Web())

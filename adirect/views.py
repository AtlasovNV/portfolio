from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from urllib3 import request
from .processors import modifier, counter, generator, lemma, cityremover, trim_utm, synonym, crossminus, declension


def adirect(request):
    return render(request, 'adirect/index.html', )


def team(request):
    return render(request, 'adirect/team.html')



def Generator(request):
    return render(request, 'adirect/keyword/generator.html')


def ServiceGenerator(request):
    colamn = []
    colamn.append(modifier(request.form["colamn0"], 'all'))
    colamn.append(modifier(request.form["colamn1"], 'all'))
    colamn.append(modifier(request.form["colamn2"], 'all'))
    colamn.append(modifier(request.form["colamn3"], 'all'))
    colamn.append(modifier(request.form["colamn4"], 'all'))
    colamn.append(modifier(request.form["colamn5"], 'all'))
    colamn.append(modifier(request.form["colamn6"], 'all'))

    words = generator(colamn)
    print(words)
    return render(request, 'adirect/keyword/generator/submit', methods=['GET', 'POST'], result=words)

def inclinator(request):
    return render(request, 'adirect/keyword/inclinator.html')

def CrossMinus(request):
    return render(request, 'adirect/keyword/crossminus.html')

def lemmatizer(request):
    return render(request, 'adirect/keyword/lemmatizer.html')

def synonymizer(request):
    return render(request, 'adirect/keyword/synonymizer.html')

def wordcount(request):
    return render(request, 'adirect/keyword/wordcount.html')

def TrimUtm(request):
    return render(request, 'adirect/keyword/trimutm.html')

def CityRemover(request):
    return render(request, 'adirect/keyword/cityremover.html')






#
# @application.route('/keyword/crossminus/submit', methods=['GET', 'POST'])  # принимает текст
# def ServiceCrossminus():
#     words = crossminus(modifier(request.form["words"], 'all'))
#
#     return render('/keyword/crossminus.html', title='Кросс-минусовка фраз', ServiceName='Кросс-минусовка фраз',
#                            result=words)


# @application.route('/keyword/inclinator/submit', methods=['GET', 'POST'])  # принимает текст
# def ServiceInclinator():
#     words = declension(modifier(request.form["words"], 'all'))
#
#     return render('/keyword/inclinator.html', title='Склонятор', ServiceName='Склонение ключевых слов',
#                            result='\n'.join(words))
#



#
# @application.route('/keyword/lemmatizer/submit', methods=['GET', 'POST'])  # принимает текст
# def inclinatorLemmatizer():
#     words = lemma(modifier(request.form["words"], 'all'))
#
#     return render('/keyword/lemmatizer.html', title='Лемматизатор', ServiceName='Лемматизатор', result=words)
#





# @application.route('/keyword/synonymizer/submit', methods=['GET', 'POST'])  # принимает текст
# def ServiceSynonymizer():
#     words = synonym(request.form["words"])
#
#     return render('/keyword/synonymizer.html', title='Синонимайзер', ServiceName='Синонимайзер', result=words)
#
#



# @application.route('/keyword/wordcount/submit', methods=['GET', 'POST'])  # принимает текст
# def ServiceWordcount():
#     words = counter(modifier(request.form["words"], 'allpasswrap'))
#
#     return render('/keyword/wordcount.html', title='Считалка слов', ServiceName='Считалка слов', result=words)
#



#
# @application.route('/keyword/trimutm/submit', methods=['GET', 'POST'])  # принимает текст
# def ServiceTrimUtm():
#     words = trim_utm(request.form["words"])
#
#     return render('/keyword/trimutm.html', title='Удаление UTM меток', ServiceName='Удаление UTM меток',
#                            result=words)
#


#
# @application.route('/keyword/cityremover/submit', methods=['GET', 'POST'])  # принимает текст
# def ServiceCityRemover():
#     words = cityremover(modifier(request.form["words"], 'all'))
#
#     return render('/keyword/cityremover.html', title='Удаление городов', ServiceName='Удаление городов',
#                            result=words)
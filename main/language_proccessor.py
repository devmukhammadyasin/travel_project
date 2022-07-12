from locals import lang_pack

def get_language(request):
    url =  request.get_full_path()  #"/ru/about/12/"
    lang = url.strip('/').split('/')[0]
    # lang = request.session.get('lang') # ru , uz , en  , None
    if lang is not None and lang in  ['uz','ru','en']:
        if request.session.get('lang') != lang:
            request.session['lang'] = lang
        return lang_pack[lang]
    else:    
        request.session['lang'] = 'uz'
        return lang_pack['uz']



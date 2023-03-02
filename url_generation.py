# input fields for searching
search = {
    'free': '',
    'title': 'Python',
    'publisher': '',
    'subject': '',
    'isbn': '',
    'lccn': '',
    'oclc': '',
    'language': 'ja',
    'sort': '',
}

def url_q():
    title_q = '' if search['title']=='' else 'intitle:'+search['title']
    publisher_q = '' if search['publisher']== '' else 'inpublisher:'+search['publisher']
    subject_q = '' if search['subject']== '' else 'subject:'+search['subject']
    isbn_q = '' if search['isbn']== '' else 'isbn:'+search['isbn']
    lccn_q = '' if search['lccn']== '' else 'lccn:'+search['lccn']
    oclc_q = '' if search['oclc']== '' else 'oclc:'+search['oclc']
    q_list = [search['free'], title_q, publisher_q, subject_q, isbn_q, lccn_q, oclc_q]
    q_list_none = list(filter(None, q_list))
    url_q = 'q=' + '+'.join(q_list_none)
    return url_q

def url_generation():
    base_url = 'https://www.googleapis.com/books/v1/volumes?'
    url_lnag = '' if search['language'] == '' else 'langRestrict='+search['language']
    url_sort = '' if search['sort'] == '' else 'orderBy='+search['sort']
    url_list = [url_q(), url_lnag, url_sort]
    url_list_none = list(filter(None, url_list))
    url = base_url + '&'.join(url_list_none)
    return url


